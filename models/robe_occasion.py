from odoo import models, fields, api

class RobeOccasion(models.Model):
    _name = 'robe.occasion'
    _description = 'Robe d\'occasion.'
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
    nbr_amort = fields.Integer(string="Nombre d'mortissement")
    prix_location = fields.Float(string="Prix de location")
    quant = fields.Integer(string="Qauntité")

    tag_ids = fields.Many2many(
        string="tags",
        comodel_name="robe.tag")

    # state = fields.Selection(
    #     string="Etats",
    #     selection=[
    #             ('value1', 'description1'),
    #             ('value2', 'description2'),
    #     ],
    # )

    # foreign keys    @api.depends('type')
    def _generate_ref(self):
        for robe in self:
            # code = str(self.env.search_count([('', '=', 'entry')]))
            robe.ref = str(robe.type).upper() + '#' + str(robe.id).upper()

    resrvation_ids = fields.One2many(
        comodel_name="reservation.robe",
        inverse_name="robe_id"
    )

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
