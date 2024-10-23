from odoo import models, fields

class Auteur(models.Model):
    _name = 'gestion.bibliotheque.auteur'
    _rec_name='prenom'

    _description = 'Auteur'
    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    date_naissance = fields.Date(string='Date de Naissance', required=True)
    nationalite = fields.Char(string='Nationalité', default='Algérienne')
    sexe = fields.Selection([('homme', 'Homme'), ('femme', 'Femme')], string='Sexe', required=True)
    livre_ids = fields.One2many('gestion.bibliotheque.livre', 'auteur_id', string='Livres')
