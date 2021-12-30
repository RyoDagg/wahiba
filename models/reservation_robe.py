from odoo import models, fields

class ReservationRobe(models.Model):
    _name = 'reservation.robe'
    _description = 'Reservation'

    # nbr_jours = fields.Integer(default = 1,string="Nombres des jours.")

    client_id = fields.Many2one(
        comodel_name = "res.partner",
        string = "Client"
    )

    etats = fields.Selection(
        string="Etats",
        selection=[
            ('attente', 'Attente'),
            ('Confirme', 'Confirmé'),
            ('annule', 'Annulé')],
        default = 'attente')

    robe_id = fields.Many2one(
        string="Robe à louer",
        comodel_name="robe.occasion")

    date_location = fields.Date(string="Date de location")
    duree = fields.Integer(default=1, string="Durée de location")
