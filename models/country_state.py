# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2017 Serpent Consulting Services Pvt. Ltd.
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import fields, models


class ResCountryState(models.Model):
    _inherit = "res.country.state"

    country_id = fields.Many2one(
        'res.country', string='Country', required=False)
    name = fields.Char(string='State Name', required=True,
                       help='Administrative divisions of a country.'
                       'E.g. Fed. State, Departement, Canton')
    code = fields.Char(string='State Code',
                       help='The state code.', required=False)
