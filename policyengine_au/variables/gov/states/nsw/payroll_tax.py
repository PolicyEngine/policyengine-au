from policyengine_au.model_api import *


class nsw_payroll_tax(Variable):
    value_type = float
    entity = Household
    label = "NSW payroll tax"
    definition_period = YEAR
    unit = "AUD"
    reference = "https://www.legislation.nsw.gov.au/view/html/inforce/current/act-2007-021"

    def formula(household, period, parameters):
        # Get NSW payroll tax parameters
        params = parameters(period).gov.states.nsw.payroll_tax

        # Aggregate wages at household level
        wages = household.sum(household.members("employment_income", period))

        # Calculate tax for NSW employers
        threshold = params.threshold
        rate = params.rate

        return max_(wages - threshold, 0) * rate
