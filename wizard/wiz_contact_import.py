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
import base64
import StringIO
import csv
from odoo import api, fields, models


class WizContactImport(models.TransientModel):
    _name = 'wiz.contact.import'

    csv_file = fields.Binary('Data', required=1)

    @api.multi
    def contact_import(self):
        state_list = []
        prefix_list = []
        partner_obj = self.env['res.partner']
        partner_title_obj = self.env['res.partner.title']
        country_state_obj = self.env['res.country.state']
        for rec in self:
            datafile = rec.csv_file
            if datafile:
                csv_data = base64.decodestring(datafile)
                file_data = StringIO.StringIO(csv_data)
                reader = list(csv.reader(file_data, delimiter=','))
                val_list = reader[1:]
                for prefix_data in val_list:
                    if not partner_title_obj.search(
                            [('name', '=', prefix_data[0])]):
                        prefix_list.append(prefix_data[0])
                if prefix_list:
                    for prefix_data in set(prefix_list):
                        partner_title_obj.create({'name': prefix_data})
                for state_data in val_list:
                    if not country_state_obj.search(
                            [('name', '=', state_data[11])]):
                        state_list.append(state_data[11])
                if state_list:
                    for state_data in set(state_list):
                        country_state_obj.create({'name': state_data})

                for contact_data in val_list:
                    partner_data = partner_obj.search([
                        ('name', '=', contact_data[1]),
                        ('prename', '=', contact_data[2]),
                        ('name_1', '=', contact_data[3]),
                        ('name_2', '=', contact_data[4]),
                        ('name_3', '=', contact_data[5]),
                        ('name_4', '=', contact_data[6])])
                    if not partner_data:
                        partner_title_id = partner_title_obj.search(
                            [('name', '=', contact_data[0])]).id
                        country_state_id = country_state_obj.search(
                            [('name', '=', contact_data[11])]).id
                        partner_obj.create({
                            'title': partner_title_id,
                            'name': contact_data[1],
                            'prename': contact_data[2],
                            'name_1': contact_data[3],
                            'name_2': contact_data[4],
                            'name_3': contact_data[5],
                            'name_4': contact_data[6],
                            'mailbox': contact_data[7],
                            'street': contact_data[8],
                            'zip': contact_data[9],
                            'city': contact_data[10],
                            'state_id': country_state_id,
                            'phone': contact_data[12],
                            'phone_2': contact_data[13],
                            'fax': contact_data[14],
                            'mobile': contact_data[15],
                            'email': contact_data[16],
                            'website': contact_data[17],
                        })
