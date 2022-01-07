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


    #Overriding create
    @api.model
    def create(self, vals):
        res = super(RobeModel, self).create(vals)
        print("--------------------------------------")
        print(res)
        print("--------------------------------------")
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
        print(res.nom)
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
        for i in range(vals["quant"]):
            super(rboc.RobeOccasion, self.env['robe.occasion']).create({
                'robe_model_id': res.id,
                'ref_robe' : "%s_%s" %(res.ref,i+1),
                'nom' : "%s #%s" %(res.nom,i+1)
            })
        return res

    @api.depends('type')
    def _generate_ref(self):
        for robe in self:
            # print('New Type assigned', robe.type, robe.quant) #self <-- values test message
            # code = str(self.env.search_count([('', '=', 'entry')]))
            robe.ref = str(robe.type).upper() + '#' + str(id(robe.id)).upper()

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s" %(record.nom)
            result.append((record.id, rec_name))
        return result
