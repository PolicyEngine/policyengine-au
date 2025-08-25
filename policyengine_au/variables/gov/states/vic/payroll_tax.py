from policyengine_au.model_api import *


class vic_payroll_tax(Variable):
    value_type = float
    entity = Household
    label = "VIC payroll tax"
    definition_period = YEAR
    unit = "AUD"
    reference = (
        "https://www.legislation.vic.gov.au/in-force/acts/payroll-tax-act-2007"
    )

    def formula(household, period, parameters):
        # Get VIC payroll tax parameters
        params = parameters(period).gov.states.vic.payroll_tax

        # Aggregate wages at household level
        wages = household.sum(household.members("employment_income", period))

        # Calculate tax for VIC employers
        threshold = params.threshold
        rate = params.rate
        regional_rate = params.regional_rate

        # Base payroll tax
        base_tax = max_(wages - threshold, 0) * rate

        # Mental health levy for large employers
        mental_health_levy_rate = select(
            [wages <= 10_000_000, wages <= 100_000_000],
            [
                0,  # No levy below $10M
                params.mental_health_levy_10m,  # 1% for $10M-$100M
            ],
            default=params.mental_health_levy_100m,  # Default: 2% for over $100M
        )

        return base_tax + (wages * mental_health_levy_rate)
