from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class LibraryPublisher(models.Model):
    _name = 'library.publisher'
    _description = '出版社'
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', '出版社名称必须唯一！'),
    ]

    name = fields.Char(string="PublisherName", required=True)
    book_ids = fields.Many2many(
        'library.book',
        'library_book_publisher_rel',
        'publisher_id',
        'book_id',
        string="Books"
    )
    book_count = fields.Integer(string="Book Count", compute="_compute_book_count", store=True)

    @api.depends('book_ids')
    def _compute_book_count(self):
        for publisher in self:
            publisher.book_count = len(publisher.book_ids)