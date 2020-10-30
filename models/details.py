from odoo import models, fields

class StudentRecord1(models.Model):

    _name = "book.book"
    name = fields.Char(string='Book Name', required=True)
    author = fields.Char(string='Author', required=True)
    editor = fields.Char(string='Editor', required=True)
    year_of_edition = fields.Date(string='Year of Edition', required=True)
    isbn = fields.Integer(string='ISBN')