# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DesignClient(models.Model):
	_name = 'design.client'

	f_name = fields.Char('Votre nom', required=True)
	l_name = fields.Char('Votre prenom', required=True)
	phone = fields.Char(required=True,)
	email = fields.Char()
	choix_service = fields.Selection([
		('choix01', 'Design applications mobile ou web'),
		('choix02', 'Création de site web'),
		('choix03', 'Design de logo, brochure, flyer, etc'),
		('choix04', 'Montage vidé, Conception de pubs'),
		('choix05', 'Gestion de blog, page sociales, rédaction de contenus'),
		('choix06', 'Création de personnages et/ou environnements (2D) pour jeu vidéo'),
		('choix07', 'Autre(s) projet(s)')
	])
	description = fields.Text()
	# date_soumission = fields.DateTime()