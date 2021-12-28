from odoo import models, fields

class ServiceEsthetique(models.Model):
    _name="service.esthetique"
    _description="Service esthetique d'Espace Wahiba"
    # _order = 'score

    # _sql_constraints = [
    #     ('unique_tag_name',
    #     'UNIQUE (name)',
    #     'Ce #TAG existe déjà.')]

    # Model's fields :
    nom = fields.Char(required=True)
    description = fields.Text(string="Description")
    prix = fields.Float(string="Prix de service")
