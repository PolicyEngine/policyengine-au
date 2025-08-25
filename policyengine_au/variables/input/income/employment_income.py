"""Employment income variable."""

from policyengine_au.model_api import *


class employment_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Employment income"
    documentation = "Gross income from employment including wages and salaries"
    reference = "https://www.ato.gov.au/individuals-and-families/income-and-deductions/income-you-must-declare/employment-income"
    unit = AUD
    
    default_value = 0