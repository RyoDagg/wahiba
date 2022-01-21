from odoo import models, fields, api

class MatierePremier(models.Model):
    _name = 'matiere.premier'
    _description = "Matière Premier"
    _rec_name = 'nom'

    # _sql_constraints = []

    # ref = fields.Char(
    #     string = 'Reference',
    #     compute = '_generate_ref',
    #     # required = True,
    #     store = True
    #     )

    photo = fields.Binary()
    nom = fields.Char(string="Nom")

    unite_id = fields.Many2one(
        string = "Unité de mesure",
        comodel_name = "unite.mesure"
        )

    description = fields.Text('Description du Produit')

    prix_unit = fields.Float(string="Prix unitaire")

    stock = fields.Integer("Stock")


    #Overriding create
    #
    # @api.depends('type')
    # def _generate_ref(self):
    #     for robe in self:
    #         robe.ref = str(robe.type).upper() + '#' + str(id(robe.id)).upper()
