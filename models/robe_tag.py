from odoo import models, fields

class RobeTag(models.Model):
    _name="robe.tag"
    _description="tags"
    _order = 'name'

    _sql_constraints = [
        ('unique_tag_name',
        'UNIQUE (name)',
        'Ce #TAG existe déjà.')]

    # Model's fields :
    name = fields.Char(required=True)
    color = fields.Integer()
