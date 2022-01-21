from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'User'

    nom = fields.Char("Nom")
    prenom = fields.Char("Prenom")
    cin = fields.Char(string="Numéro CIN")
    num_tel_1 = fields.Integer("Numéro de tel 1")
    num_tel_2 = fields.Integer("Numéro de tel 2")
    adresse = fields.Char(string="Adresse domicile")
    ville = fields.Char(string="Ville")
    date_naiss = fields.Char("Date de naissaince")
    voile = fields.Boolean(string="voilé")
    nbr_visite = fields.Integer(string="Nombre des visites")
