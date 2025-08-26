"""Medicare levy calculation."""

from policyengine_au.model_api import *


class medicare_levy(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Medicare levy"
    documentation = (
        "Medicare levy based on taxable income and family circumstances"
    )
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
        # Use singles thresholds for now
        no_levy_threshold = thresholds.singles.no_levy_threshold
        full_levy_threshold = thresholds.singles.full_levy_threshold

        # Calculate Medicare levy using vectorized operations
        # No levy below threshold
        no_levy = taxable_income <= no_levy_threshold
        
        # Shade-in range: 10% of income above threshold
        shade_in_range = (taxable_income > no_levy_threshold) & (taxable_income <= full_levy_threshold)
        shade_in_amount = (taxable_income - no_levy_threshold) * 0.10
        
        # Full levy: 2% of taxable income
        full_levy_amount = taxable_income * levy_rate
        
        # Select appropriate levy amount based on income
        return select(
            [no_levy, shade_in_range],
            [0, shade_in_amount],
            default=full_levy_amount
        )
