from policyengine_au.model_api import *


class wa_payroll_tax(Variable):
    value_type = float
    entity = Household
    label = "WA payroll tax"
    definition_period = YEAR
    unit = "AUD"
    reference = "https://www.legislation.wa.gov.au/legislation/statutes.nsf/main_mrtitle_1736_homepage.html"

    def formula(household, period, parameters):
        # Get WA payroll tax parameters
        params = parameters(period).gov.states.wa.payroll_tax

        # Aggregate wages at household level
        wages = household.sum(household.members("employment_income", period))

        # Calculate effective threshold (diminishing for wages $1m-$7.5m)
        base_threshold = params.threshold
        lower_limit = params.diminishing_threshold_lower
        upper_limit = params.diminishing_threshold_upper
        reduction_rate = params.diminishing_threshold_rate

        # Vectorized threshold calculation
        reduction = (
            clip(wages - lower_limit, 0, upper_limit - lower_limit)
            * reduction_rate
        )
        effective_threshold = select(
            [wages <= lower_limit, wages <= upper_limit],
            [
                base_threshold,  # No reduction below $1M
                max_(base_threshold - reduction, 0),  # Diminishing threshold
            ],
            default=0,  # Default: No threshold above $7.5M
        )

        # Apply appropriate rate based on wages using select with default
        rate = select(
            [wages <= 100_000_000, wages <= 1_500_000_000],
            [
                params.rate,  # Standard rate
                params.rate_large,  # Large employer rate
            ],
            default=params.rate_very_large,  # Default: Very large employer rate
        )

        return max_(wages - effective_threshold, 0) * rate
