from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate_property"
    _description = " Estate Property"

    name = fields.Char(help("Estate Property"), required=True)
    description = fields.Text()
    postcode = fields.Char()
    data_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Type',
        selection=[
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West')
        ]
    )
