from odoo import models, fields, api

class RobeOccasion(models.Model):
    _name = 'robe.occasion'
    _description = 'Robe d\'occasion.'

    ref_robe = fields.Char(
        string = 'Reference',
        compute = '_generate_ref',
        # required = True,
        store = True
        )

    active = fields.Boolean(
        default = True,
        compute = '_check_validity',
        store = True)

    nom = fields.Char("Nom du robe")

    model_id = fields.Many2one(
        string = "Modèle du Robe",
        comodel_name = "robe.model"
    )

    reservation_ids = fields.One2many(
        comodel_name = "reservation.robe",
        inverse_name = "robe_id"
    )

    nbr_amort = fields.Integer(
        string = "Nombre d'mortissement",
        default = 0,
        compute = '_calc_nbr_amort'
    )

    @api.depends('reservation_ids')
    def _calc_nbr_amort(self):
        for record in self:
            if record.reservation_ids:
                count = 0
                for res in record.reservation_ids:
                    if(res.etats == 'Confirme'):
                        count += 1
                record.nbr_amort = count
            else:
                record.nbr_amort = 0

    @api.depends('nbr_amort')
    def _check_validity(self):
        for record in self:
            max = record.model_id.nbr_amort_max
            if record.nbr_amort >= max :
                record.active = False
            else:
                record.active = True

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s" %(record.nom)
            result.append((record.id, rec_name))
        return result
