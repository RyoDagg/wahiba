from odoo import models, fields, api
from . import robe_occasion as rboc

class RobeModel(models.Model):
    _name = 'robe.model'
    _description = 'Modele du robe.'
    _sql_constraints = [
        ('uniq_ref', 'UNIQUE (ref)', 'Reference must be unique.')
        # ('uniq_ref', 'NOT NULL (ref)', 'Reference must be not null.')
    ]

    ref = fields.Char(
        string = 'Reference',
        compute = '_generate_ref',
        # required = True,
        store = True
        )

    photo = fields.Binary()
    nom = fields.Char(string="Field name")
    couleur = fields.Char(string="Couleur")
    type = fields.Selection(
        string="type",
        selection=[
            ('mrg', 'Mariage'),
            ('fnc', 'fiançailles'),
            ('wta', 'Wtia'),
            ('sdk', 'Sdek')],
            default = 'mrg',
            required = True)

    # Date_achat = fields.Date.today()

    robe_ids = fields.One2many(
        string="Liste des robe pour ce modèle",
        comodel_name="robe.occasion",
        inverse_name="robe_model_id"
    )

    prix_achat = fields.Float(string="Prix d\'achat")
    prix_location = fields.Float(string="Prix de location")
    quant = fields.Integer(string="Qauntité")

    tag_ids = fields.Many2many(
        string="tags",
        comodel_name="robe.tag")
    #
    # # foreign keys    @api.depends('type')
    # def _generate_ref(self):
    #     for robe in self:
    #         # code = str(self.env.search_count([('', '=', 'entry')]))
    #         robe.ref = str(robe.type).upper() + '#' + str(robe.id).upper()


    #Overriding create method

    @api.model
    def _test(self):
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
        print('111111111111111111111111111',self.quant)
        for rec in self:
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
            print('222222222222222222222222',rec.quant)
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-')

    @api.model
    def create(self, vals):
        res = super(RobeModel, self).create(vals)
        print("--------------------------------------")
        # print('1--------',self.nom) #self is empty here
        print(res)
        print("--------------------------------------")
        # print(_self.super(rboc.RobeOccasion, _self).create({'robe_model_id': 26, 'reservation_ids': [], 'nbr_amort' : 5}))
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
        print(res.nom)
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
        for i in range(vals["quant"]):
            super(rboc.RobeOccasion, self.env['robe.occasion']).create({'robe_model_id': res.id, 'ref_robe' : "%s_%s" %(vals['nom'],i+1)})
        return res

    @api.depends('type')
    def _generate_ref(self):
        for robe in self:
            # print('New Type assigned', robe.type, robe.quant) #self <-- values test message
            # code = str(self.env.search_count([('', '=', 'entry')]))
            robe.ref = str(robe.type).upper() + '#' + str(id(robe.id)).upper()
            # RobeModel._test(self)

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s" %(record.nom)
            result.append((record.id, rec_name))
        return result
