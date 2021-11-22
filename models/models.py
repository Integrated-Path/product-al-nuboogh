# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    partner_id = fields.Char('customer', compute="_Compute_partner_id")

    @api.depends('origin')
    def _Compute_partner_id(self):
        for move in self:
            for line in move:
                if line.origin:
                    if line.origin[0] == 'S':
                        line.partner_id=  line.env['sale.order'].search([('name', '=', line.origin)]).partner_id.name
                    elif line.origin[0] == 'P':
                        line.partner_id =  line.env['purchase.order'].search([('name', '=', line.origin)]).partner_id.name
                    else:
                        line.partner_id=""
                else: 
                    line.partner_id = ""
        
            
    