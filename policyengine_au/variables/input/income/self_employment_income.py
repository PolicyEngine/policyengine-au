"""Self-employment income variable."""

from policyengine_au.model_api import *


class self_employment_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Self-employment income"
    documentation = "Gross income from self-employment or business"
    reference = "https://www.ato.gov.au/individuals-and-families/income-and-deductions/income-you-must-declare/business-income"
    unit = AUD
    
    default_value = 0