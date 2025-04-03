from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = '借阅记录'
    _order = 'date_borrowed desc'
    
    book_id = fields.Many2one('library.book', string="Book")
    member_id = fields.Many2one('library.member', string="Borrower")
    date_borrowed = fields.Date(string="Borrowed On", default=fields.Date.today)
    date_returned = fields.Date(string="Returned On")
    book_author = fields.Char(string="Book Author", store=False, readonly=True)

    @api.onchange('book_id')
    def _onchange_book_id(self):
        if self.book_id:
            self.book_author = self.book_id.author

    @api.constrains('date_borrowed', 'date_returned')
    def _check_(self):
        for record in self:
            if record.date_borrowed and record.date_returned:
                if record.date_borrowed > record.date_returned:
                    raise ValidationError("借阅日期不能在归还日期之后")

    