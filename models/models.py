# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    partner_id = fields.Many2one(string='Partner', related="picking_id.partner_id",store=True)

    
        
            
    
