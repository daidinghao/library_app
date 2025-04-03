from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class LibraryMember(models.Model):
    _name = 'library.member'
    _description = '读者'
    _order = 'name'

    name = fields.Char(string="Member_Name", required=True)
    loan_ids = fields.One2many('library.loan', 'member_id', string="Loans")
    loan_count = fields.Integer(string="Books Count", compute='_compute_loan_count', store=True)
    unreturned_count = fields.Integer(string="Unreturned Count", compute="_compute_unreturned_count", store=True)

    @api.depends('loan_ids.date_returned')
    def _compute_unreturned_count(self):
        for member in self: 
            member.unreturned_count = len([
                loan for loan in member.loan_ids if not loan.date_returned
            ])

    @api.depends('loan_ids')
    def _compute_loan_count(self):
        for member in self:
            member.loan_count = len(member.loan_ids)

    