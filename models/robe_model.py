from odoo import models, fields, api

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

    prix_achat = fields.Float(string="Prix d\'achat")
    prix_location = fields.Float(string="Prix de location")
    quant = fields.Integer(string="Qauntité")

    tag_ids = fields.Many2many(
        string="tags",
        comodel_name="robe.tag")

    # foreign keys    @api.depends('type')
    def _generate_ref(self):
        for robe in self:
            # code = str(self.env.search_count([('', '=', 'entry')]))
            robe.ref = str(robe.type).upper() + '#' + str(robe.id).upper()


    @api.depends('type')
    def _generate_ref(self):
        for robe in self:
            # code = str(self.env.search_count([('', '=', 'entry')]))
            robe.ref = str(robe.type).upper() + '#' + str(id(robe.id)).upper()

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s" %(record.nom)
            result.append((record.id, rec_name))
        return result
