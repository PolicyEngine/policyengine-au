from policyengine_au.model_api import *


class sa_payroll_tax(Variable):
    value_type = float
    entity = Household
    label = "SA payroll tax"
    definition_period = YEAR
    unit = "AUD"
    reference = "https://www.legislation.sa.gov.au/LZ/C/A/Payroll%20Tax%20Act%202009.aspx"

    def formula(household, period, parameters):
        # Get SA payroll tax parameters
        params = parameters(period).gov.states.sa.payroll_tax

        # Aggregate wages at household level
        wages = household.sum(household.members("employment_income", period))

        # Calculate tax for SA employers with tiered rates
        threshold = params.threshold
        small_employer_limit = params.small_employer_limit
        rate_small = params.rate_small
        rate_standard = params.rate_standard

        # Calculate taxable wages
        taxable_wages = max_(wages - threshold, 0)

        # Select appropriate rate based on employer size
        effective_rate = where(
            wages <= small_employer_limit,
            rate_small,  # Small employer rate
            rate_standard,  # Standard rate
        )

        # Note: Deduction only applies to SA-only employers
        # Not implementing deduction as it requires multi-state check

        return where(wages <= threshold, 0, taxable_wages * effective_rate)
