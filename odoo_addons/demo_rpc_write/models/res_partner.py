from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    test_depends = fields.Char(
        compute="_compute_test_depends",
        store=True,
        readonly=True,
        help="This field is calculated whenever the name field changes, using api.depends.",
    )

    test_write = fields.Char(
        readonly=True,
        help="This field is written to using the write() method.",
    )

    def write(self, vals):

        if 'name' in vals:
            vals['test_write'] = f"Test write: {vals['name']}"

        return super().write(vals)

    @api.depends("name")
    def _compute_test_depends(self):
        for partner in self:
            partner.test_depends = f"Test depends: {partner.name}"