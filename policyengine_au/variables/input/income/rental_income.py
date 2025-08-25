"""Rental income variable."""

from policyengine_au.model_api import *


class rental_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Rental income"
    documentation = "Net rental income from investment properties"
    reference = "https://www.ato.gov.au/individuals-and-families/income-and-deductions/income-you-must-declare/rental-income"
    unit = AUD
    
    default_value = 0