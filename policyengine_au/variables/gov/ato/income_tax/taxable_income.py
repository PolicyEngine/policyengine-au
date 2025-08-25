"""Taxable income calculation."""

from policyengine_au.model_api import *


class taxable_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Taxable income"
    documentation = "Total taxable income for income tax purposes"
    reference = "https://www.ato.gov.au/individuals-and-families/income-and-deductions/income-you-must-declare"
    unit = AUD
    
    def formula(person, period, parameters):
        employment = person("employment_income", period)
        self_employment = person("self_employment_income", period)
        investment = person("investment_income", period)
        rental = person("rental_income", period)
        
        # Sum all income sources
        total_income = employment + self_employment + investment + rental
        
        # Apply deductions (simplified for now)
        deductions = person("total_deductions", period)
        
        return max_(0, total_income - deductions)