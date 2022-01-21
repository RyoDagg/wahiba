from odoo import models, fields, api

class Production(models.Model):
    _name = 'production.produit'
    _description = "Production"

    produit_id = fields.Many2one(
        string="Produit",
        comodel_name="produit.prototype"
    )

    quantite = fields.Integer(string="Quantité")

    status = fields.Selection(
        string="Status de Production",
        selection=[
                ('attente', 'En attente'),
                ('en_cours', 'En cours de Production'),
                ('termine', 'Terminé'),
                ('annule', 'Annulé'),
        ],
        default = 'attente'
    )

    def lancer_production(self):
        self.ensure_one()
        self.status = 'en_cours'

    def terminer_production(self):
        self.ensure_one()
        self.status = 'termine'

    def annuler_production(self):
        self.ensure_one()
        self.status = 'annule'
