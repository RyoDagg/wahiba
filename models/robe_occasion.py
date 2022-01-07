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

    robe_model_id = fields.Many2one(
        string="Modèle du Robe",
        comodel_name="robe.model"
    )

    reservation_ids = fields.One2many(
        comodel_name="reservation.robe",
        inverse_name="robe_id"
    )

    nbr_amort = fields.Integer(
        string="Nombre d'mortissement"
        # default = 0,
        # compute = 'calc_nbr_amort'
    )

    #
    # def _generate_ref(self):
    #     for robe in self:
    #         # code = str(self.env.search_count([('', '=', 'entry')]))
    #         robe.ref = str(robe.type).upper() + '#' + str(robe.id).upper()

    # @api.depends('reservation_ids')
    # def calc_nbr_amort(self):
    #     for record in self:
    #         if record.reservation_ids:
    #             record.nbr_amort = len(record.reservation_ids)
    #         else:
    #             record.nbr_amort = 0

    # def name_get(self):
    #     result = []
    #     for record in self:
    #         rec_name = "%s" %(record.nom)
    #         result.append((record.id, rec_name))
    #     return result

    # @api.model
    # def create(self, vals):
    #     # print(vals)
    #     print(super(RobeOccasion, self).create({'robe_model_id': 26, 'reservation_ids': [], 'nbr_amort' : 5}))
    #     return super(RobeOccasion, self).create(vals)

    def _test():
        print("--------------------------------------")
        print("--------------------------------------")
        print("--------------------------------------")
        print("--------------------------------------")
        print("--------------------------------------")
        print("--------------------------------------")
