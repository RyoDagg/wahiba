from odoo import models, fields, api

class UniteMesure(models.Model):
    _name = 'unite.mesure'
    _description = "Unite de mesure du matière"

    nom = fields.Char(string="Nom")
    symbole = fields.Char(string="Symbole")

    # Overriding name_get
    def name_get(self):
        result = []
        for rec in self:
            name = "%s(%s)." %(rec.nom, rec.symbole)
            result.append((rec.id, name))
        return result
