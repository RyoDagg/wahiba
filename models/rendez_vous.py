from odoo import models, fields, api

class RendezVous(models.Model):
    _name="rendez.vous"
    _description="Gestion des Rendez-Vous"
    _order = 'date_rdv'

    # Model's fields :

    date_rdv = fields.Datetime(string="Date et heure du rendev vous")

    services_ids = fields.Many2many( #pack de beauté
        string="Services",
        comodel_name="service.esthetique")

    date_event = fields.Datetime(string="Date-heure d'evenment")

    reservation_id = fields.Many2one(
        string="Reservation accosié a ce Rendez-Vous.",
        comodel_name="reservation.robe")

    avance = fields.Float(string="Avance de payement")
    prix_total = fields.Float(
        compute = '_calc_prix_tot',
        string = 'Prix Totale')

    reste_payer = fields.Float(
        compute = '_clac_reste_paye',
        string = 'Reste à payer')

    nom_client = fields.Char(
        string = "Nom du client",
        compute = "_get_nom_client")

    @api.depends('services_ids', 'reservation_id.robe_id')
    def _calc_prix_tot(self):
        for record in self:
            record.prix_total = sum(record.mapped('services_ids.prix')) + record.reservation_id.robe_id.prix_location

    @api.depends('prix_total', 'avance', )
    def _clac_reste_paye(self):
        for record in self:
            record.reste_payer = record.prix_total - record.avance

    @api.model
    def _get_nom_client(self):
        for record in self:
            record.nom_client = "%s" %(record.reservation_id.client_id.name)
            # record.nom_client = "%s %s" %(record.reservation_id.client_id.nom, record.reservation_id.client_id.prenom)
