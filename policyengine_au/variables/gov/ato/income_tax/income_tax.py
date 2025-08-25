"""Income tax calculation for Australian residents."""

from policyengine_au.model_api import *


class income_tax(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Income tax"
    documentation = "Total income tax liability before offsets and credits"
    reference = "https://www.ato.gov.au/tax-rates-and-codes/individual-income-tax-rates"
    unit = AUD
    
    def formula(person, period, parameters):
        taxable_income = person("taxable_income", period)
        p = parameters(period).gov.ato.income_tax
        
        # Get thresholds and rates
        thresholds = p.thresholds
        rates = p.rates
        
        # Calculate tax for each bracket
        tax = 0
        
        # Tax-free threshold (0%)
        tax_free = thresholds.thresholds.tax_free_threshold
        
        # Bracket 2: 19% on income from $18,201 to $45,000
        bracket_2_threshold = thresholds.thresholds.bracket_2
        bracket_2_upper = thresholds.thresholds.bracket_3
        bracket_2_rate = rates.rates.bracket_2
        
        if taxable_income > bracket_2_threshold:
            bracket_2_income = min_(taxable_income - bracket_2_threshold, 
                                   bracket_2_upper - bracket_2_threshold)
            tax += bracket_2_income * bracket_2_rate
        
        # Bracket 3: 32.5%/30% on income from $45,001 to $120,000/$135,000
        bracket_3_threshold = thresholds.thresholds.bracket_3
        bracket_3_upper = thresholds.thresholds.bracket_4
        bracket_3_rate = rates.rates.bracket_3
        
        if taxable_income > bracket_3_threshold:
            bracket_3_income = min_(taxable_income - bracket_3_threshold,
                                   bracket_3_upper - bracket_3_threshold)
            tax += bracket_3_income * bracket_3_rate
        
        # Bracket 4: 37% on income from $120,001/$135,001 to $180,000/$190,000
        bracket_4_threshold = thresholds.thresholds.bracket_4
        bracket_4_upper = thresholds.thresholds.bracket_5
        bracket_4_rate = rates.rates.bracket_4
        
        if taxable_income > bracket_4_threshold:
            bracket_4_income = min_(taxable_income - bracket_4_threshold,
                                   bracket_4_upper - bracket_4_threshold)
            tax += bracket_4_income * bracket_4_rate
        
        # Bracket 5: 45% on income above $180,000/$190,000
        bracket_5_threshold = thresholds.thresholds.bracket_5
        bracket_5_rate = rates.rates.bracket_5
        
        if taxable_income > bracket_5_threshold:
            bracket_5_income = taxable_income - bracket_5_threshold
            tax += bracket_5_income * bracket_5_rate
        
        return tax