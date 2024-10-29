from odoo import models, fields

class Emprunteur(models.Model):
    _name = 'gestion.bibliotheque.emprunteur'
    _description = 'Emprunteur'
    _rec_name='nom'

    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    date_naissance = fields.Date(string='Date de Naissance', required=True)
    state = fields.Char(string='State', required=True)
    sexe = fields.Selection([('homme', 'Homme'), ('femme', 'Femme')], string='Sexe', required=True)
    emprunt_ids = fields.One2many('gestion.bibliotheque.emprunt', 'emprunteur_id', string='Emprunts')
    emprunt_lignes_id=fields.one2Many('gestion.bibliotheque.emprunt_lignes',string="emprunt lignes")
