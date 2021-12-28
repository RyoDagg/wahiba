from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Client'

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


    published_book_ids = fields.One2many(
        string="Published Books",
        comodel_name="library.book",
        inverse_name="publisher_id")

    authored_book_ids = fields.Many2many('library.book',
        string='Authered Books',
        #relation = '$relation_name'
        )
