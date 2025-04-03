from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = '书'
    _order = 'date_published desc'
    _rec_name = 'name'
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', '书名必须唯一！'),
    ]

    name = fields.Char(string="Title", required=True, help="每本书的标题必须唯一")
    author = fields.Char(string="Author")
    description = fields.Text(string="Description")
    cover_image = fields.Binary(string="Images")
    date_published = fields.Date(string="Publication Date")
    pages = fields.Integer(string="Number of Pages")
    total_loan_count = fields.Integer(string="Total Loan Count", compute="_compute_total_loan_count", store=True)

    publisher_ids = fields.Many2many(
        'library.publisher',
        'library_book_publisher_rel',
        'book_id',
        'publisher_id',
        string="Publishers"
    )    
    
    loan_ids = fields.One2many('library.loan', 'book_id', string="Loans")

    @api.depends('loan_ids')
    def _compute_total_loan_count(self):
        for book in self:
            book.total_loan_count = len(book.loan_ids)

    @api.constrains('pages')
    def _check_(self):
        for record in self:
            if record.pages < 0:
                raise ValidationError("页数不能为负数")

    
            
    

