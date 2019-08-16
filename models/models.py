# -*- coding: utf-8 -*-

from odoo import models, fields, api
class AcOrder(models.Model):
    #ตั้งชื่อ
    _name = 'ac_order'
    
    #กำหนดตัวแปร
    name = fields.Char('Name')
    customer = fields.Many2one(comodel_name='res.partner',string='Customer')
    date = fields.Datetime('Date',required=True)
    #สร้างตัวแปร order_line รับค่าจาก class AcOrderLine
    order_line = fields.One2many(comodel_name='ac_order_line',inverse_name='name_or',string = 'OrderLine')

class AcOrderLine(models.Model):
    _name = 'ac_order_line'
    #สร้างตัวแปร name_or เพื่อส่งค่าไป classAcOrder
    name_or= fields.Many2one(comodel_name='ac_order', string = 'Oderr')
    #กำหนดตัวแปร
    product = fields.Many2one(comodel_name='product.product',string='Product')
    description = fields.Text(string='Description')
    uom = fields.Selection([['unit','Unit'],['n','ชิ้้น'],['j','ชุด']],string='UoM')
    unit_price = fields.Integer(string='Unit Price')
    
