# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CrossoveredBudgetLines_inherit(models.Model):
    _inherit = "crossovered.budget.lines"

    @api.multi
    def _compute_percentage(self):
        for line in self:
            if line.practical_amount != 0.00:
                line.percentage = float(((line.practical_amount)*100) / line.planned_amount)
            else:
                line.percentage = 0.00