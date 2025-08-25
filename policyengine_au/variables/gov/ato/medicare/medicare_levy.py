"""Medicare levy calculation."""

from policyengine_au.model_api import *


class medicare_levy(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Medicare levy"
    documentation = "Medicare levy based on taxable income and family circumstances"
    reference = "https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy"
    unit = AUD
    
    def formula(person, period, parameters):
        taxable_income = person("taxable_income", period)
        p_medicare = parameters(period).gov.ato.medicare
        
        # Get basic levy rate (2%)
        levy_rate = p_medicare.levy_rate
        
        # Get low income thresholds
        thresholds = p_medicare.low_income_thresholds
        
        # For simplicity, assume single person initially
        # TODO: Add family status detection
        is_single = True
        
        if is_single:
            no_levy_threshold = thresholds.singles.no_levy_threshold
            full_levy_threshold = thresholds.singles.full_levy_threshold
        else:
            # Family thresholds would be used here
            no_levy_threshold = thresholds.families.no_levy_threshold
            full_levy_threshold = thresholds.families.full_levy_threshold
        
        # Calculate Medicare levy
        if taxable_income <= no_levy_threshold:
            # No Medicare levy for low income
            return 0
        elif taxable_income <= full_levy_threshold:
            # Shade-in range: 10% of income above threshold
            return (taxable_income - no_levy_threshold) * 0.10
        else:
            # Full Medicare levy (2% of taxable income)
            return taxable_income * levy_rate