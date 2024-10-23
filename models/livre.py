from odoo import models, fields

class Livre(models.Model):
    _name = 'gestion.bibliotheque.livre'
    _description = 'Livre'
    _rec_name='titre'

    titre = fields.Char(string='Titre', required=True)
    langue_livre = fields.Selection([('francais', 'Français'), ('arabe', 'Arabe'), ('anglais', 'Anglais')], string='Langue du Livre', required=True)
    isbn = fields.Char(string='ISBN', required=True)
    nbre_pages = fields.Integer(string='Nombre de Pages', required=True)
    image_livre = fields.Binary(string='Image du Livre')
    auteur_id = fields.Many2one('gestion.bibliotheque.auteur', string='Auteur')
