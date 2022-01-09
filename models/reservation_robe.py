from odoo import models, fields, api
from datetime import timedelta

class ReservationRobe(models.Model):
    _name = 'reservation.robe'
    _description = 'Reservation'

    client_id = fields.Many2one(
        comodel_name = "res.partner",
        string = "Client"
    )

    avance = fields.Float("Avance")

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

    @api.constrains('date_location')
    def check_date_future(self):
        for record in self:
            if record.date_location and record.date_location < fields.date.today():
                raise models.ValidationError('Reservation date must not be in the past')

    @api.constrains('date_location')
    def _check_date_collision(self):
        query = "SELECT date_location FROM reservation_robe WHERE id<>%s AND robe_id=%s" %(self.id, self.robe_id.id)
        self.env.cr.execute(query)
        l = self.env.cr.fetchall()
        for item in l:
            if(self.date_location==item[0]):
                raise models.ValidationError('Déja reservée')
