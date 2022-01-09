from odoo import models, fields, api
from . import robe_occasion as rboc

class RobeModel(models.Model):
    _name = 'robe.model'
    _description = 'Modele du robe.'
    _sql_constraints = [
        ('uniq_ref', 'UNIQUE (ref)', 'Reference must be unique.'),
        ('amort_max_positive', 'CHECK (nbr_amort_max>0)', 'Nombre Maximal des amortissement doit etre positive'),
        ('positive_quant', 'CHECK (quant>0)', 'Quantité doit etre positive')
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
        inverse_name="model_id"
    )

    nbr_amort_max = fields.Integer("Nombre D'amortissement Maximal")

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
        for i in range(vals["quant"]):
            super(rboc.RobeOccasion, self.env['robe.occasion']).create({
                'model_id': res.id,
                'ref_robe' : "%s_%s" %(res.ref,i+1),
                'nom' : "%s #%s" %(res.nom,i+1)
            })
        return res

    @api.depends('type')
    def _generate_ref(self):
        for robe in self:
            robe.ref = str(robe.type).upper() + '#' + str(id(robe.id)).upper()

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s" %(record.nom)
            result.append((record.id, rec_name))
        return result
