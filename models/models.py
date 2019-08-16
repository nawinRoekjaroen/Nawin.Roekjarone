# -*- coding: utf-8 -*-

from odoo import models, fields, api
class AcOrder(models.Model):
    _name = 'ac_order'

    name = fields.Char('Name')
    customer = fields.Many2one(comodel_name='res.partner',string='Customer')
    date = fields.Datetime('Date',required=True)
    order_line = fields.One2many(comodel_name='ac_order_line',inverse_name='name_or',string = 'OrderLine')

class AcOrderLine(models.Model):
    _name = 'ac_order_line'
     
    name_or= fields.Many2one(comodel_name='ac_order', string = 'Oderr')
    product = fields.Many2one(comodel_name='product.product',string='Product')
    description = fields.Text(string='Description')
    uom = fields.Selection([['unit','Unit'],['n','ชิ้้น'],['j','ชุด']],string='UoM')
    unit_price = fields.Integer(string='Unit Price')
    
