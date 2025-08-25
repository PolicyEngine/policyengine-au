from policyengine_au.model_api import *


class act_payroll_tax(Variable):
    value_type = float
    entity = Household
    label = "ACT payroll tax"
    definition_period = YEAR
    unit = "AUD"
    reference = "https://www.legislation.act.gov.au/a/2011-18"

    def formula(household, period, parameters):
        # Get ACT payroll tax parameters
        params = parameters(period).gov.states.act.payroll_tax

        # Aggregate wages at household level
        wages = household.sum(household.members("employment_income", period))

        # Calculate tax for ACT employers
        threshold = params.threshold
        rate = params.rate

        taxable_wages = max_(wages - threshold, 0)

        return taxable_wages * rate
