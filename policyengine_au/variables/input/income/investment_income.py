"""Investment income variable."""

from policyengine_au.model_api import *


class investment_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Investment income"
    documentation = "Income from investments including dividends and interest"
    reference = "https://www.ato.gov.au/individuals-and-families/income-and-deductions/income-you-must-declare/investment-income"
    unit = AUD

    default_value = 0
