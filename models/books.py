from odoo import models, fields

class StudentRecord(models.Model):

    _name = "student.student"
    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    photo = fields.Binary(string='Photo')
    student_dob = fields.Date(string="Date of Birth")
    student_address = fields.Char(string='Address')
    student_gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender')

    #student_book = fields.Selection(
    #[('A', 'Book_A'), ('B', 'Book_B'), ('C', 'Book_C'), ('D', 'Book_D')],
    #string='Book')

    student_book = fields.Many2one('book.book', 'Book Name')
    student_return_date = fields.Date(string="Return date")