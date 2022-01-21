from odoo import models, fields, api

class ProduitMatiere(models.Model):
    _name = 'produit.matiere'
    _description = "Produit Matière"
    _rec_name = 'matiere_id'

    produit_id = fields.Many2one(
        string ="Produit",
        comodel_name = "produit.prototype",
        default=lambda self:self.env['produit.prototype'].search([]).id
    )

    matiere_id = fields.Many2one(
        string ="Matiére à utiliser",
        comodel_name = "matiere.premier"
    )

    quantite = fields.Float(string="Quantité necessaire")
    # depense =
