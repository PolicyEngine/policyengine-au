from policyengine_au.model_api import *


class qld_payroll_tax(Variable):
    value_type = float
    entity = Household
    label = "QLD payroll tax"
    definition_period = YEAR
    unit = "AUD"
    reference = "https://www.legislation.qld.gov.au/view/html/inforce/current/act-1971-062"

    def formula(household, period, parameters):
        # Get QLD payroll tax parameters
        params = parameters(period).gov.states.qld.payroll_tax

        # Aggregate wages at household level
        wages = household.sum(household.members("employment_income", period))

        # Calculate tax for QLD employers with tiered rates
        threshold = params.threshold
        rate = params.rate
        rate_large = params.rate_large
        large_employer_threshold = params.large_employer_threshold
        regional_discount = params.regional_discount

        # Calculate tax with tiered rates
        return where(
            wages <= threshold,
            0,
            where(
                wages <= large_employer_threshold,
                (wages - threshold) * rate,
                (large_employer_threshold - threshold) * rate
                + (wages - large_employer_threshold) * rate_large,
            ),
        )
