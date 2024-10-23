from odoo import models, fields


class Emprunt(models.Model):
    _name = 'gestion.bibliotheque.emprunt'
    _description = 'Emprunt'

    date_debut = fields.Date(string='Date Début', required=True)
    date_fin = fields.Date(string='Date Fin', required=True)
    rendu = fields.Selection([('oui', 'Oui'), ('non', 'Non')], string='Rendu', required=True)
    livre_id = fields.Many2one('gestion.bibliotheque.livre', string='Livre', required=True)
    emprunteur_id = fields.Many2one('gestion.bibliotheque.emprunteur', string='Emprunteur', required=True)
