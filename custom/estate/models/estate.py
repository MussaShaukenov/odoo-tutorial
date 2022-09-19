from odoo import models, fields
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Estate(models.Model):
    # name of the module
    _name = 'estate.property'
    _description = "estate property model"

    date_in_three_months = datetime.now() + relativedelta(months=3)

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    data_availability = fields.Date(copy=False, default=date_in_three_months)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([("north", "North"), ("east", "East"), ("south", "South"), ("west", "West")])
    state = fields.Selection(
        [("new", "New"), ("offer_received", "Offer Received"), ("offer_accepted", "Offer Accepted"), ("sold", "Sold"),
         ("canceled", "Canceled"), ],
        string="Status",
        required=True,
        copy=False,
        default="New",
        )
    active = fields.Boolean("Active", default=True)
