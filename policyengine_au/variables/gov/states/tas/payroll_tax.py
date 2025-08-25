from policyengine_au.model_api import *


class tas_payroll_tax(Variable):
    value_type = float
    entity = Household
    label = "TAS payroll tax"
    definition_period = YEAR
    unit = "AUD"
    reference = "https://www.legislation.tas.gov.au/view/html/inforce/current/act-2008-016"

    def formula(household, period, parameters):
        # Get TAS payroll tax parameters
        params = parameters(period).gov.states.tas.payroll_tax

        # Aggregate wages at household level
        wages = household.sum(household.members("employment_income", period))

        # Calculate tax for TAS employers with tiered rates
        threshold = params.threshold
        large_employer_threshold = params.large_employer_threshold
        rate_small = params.rate_small
        rate_standard = params.rate_standard

        # Calculate taxable wages
        taxable_wages = max_(wages - threshold, 0)

        # Select appropriate rate based on employer size
        effective_rate = where(
            wages <= large_employer_threshold,
            rate_small,  # Small employer rate
            rate_standard,  # Large employer rate
        )

        return where(wages <= threshold, 0, taxable_wages * effective_rate)
