"""Income tax calculation for Australian residents."""

from policyengine_au.model_api import *


class income_tax(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Income tax"
    documentation = "Total income tax liability before offsets and credits"
    reference = "https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents"
    unit = AUD

    def formula(person, period, parameters):
        taxable_income = person("taxable_income", period)
        p = parameters(period).gov.ato.income_tax.tax_scale

        # Handle negative taxable income (tax losses)
        # Per ATO rules: tax losses are carried forward to future years
        # No tax is payable on negative taxable income
        # Reference: https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/losses/losses/what-is-a-tax-loss
        positive_income = max_(0, taxable_income)

        # Use the marginal_rate_tax function with the scale parameter
        # The scale parameter should define brackets and rates
        return p.calc(positive_income)
