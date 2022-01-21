from odoo import models, fields, api

class ProduitPrototype(models.Model):
    _name = 'produit.prototype'
    _description = "Prototype d'un produit."
    _rec_name = 'nom'

    matiere_ids = fields.One2many(
        string = "Matiéres Premiers",
        comodel_name = "produit.matiere",
        inverse_name = "produit_id"
    )

    photo = fields.Binary()
    nom = fields.Char(string="Field name")

    description = fields.Text('Description du Produ****it')

    stock = fields.Integer(string="Stock")

    #Overriding create
    #
    # @api.depends('type')
    # def _generate_ref(self):
    #     for robe in self:
    #         robe.ref = str(robe.type).upper() + '#' + str(id(robe.id)).upper()
