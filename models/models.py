# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    partner_id = fields.Char('customer', compute="_Compute_partner_id")

    @api.depends('origin')
    def _Compute_partner_id(self):
        for move in self:
            if move.origin:
                if move.origin[0] == 'S':
                    move.partner_id=  move.env['sale.order'].search([('name', '=', move.origin)]).partner_id.name
                elif move.origin[0] == 'P':
                    move.partner_id =  move.env['purchase.order'].search([('name', '=', move.origin)]).partner_id.name
                else:
                    move.partner_id=""
            else: 
                move.partner_id = ""
        
            
    