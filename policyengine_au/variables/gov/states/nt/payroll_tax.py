from policyengine_au.model_api import *


class nt_payroll_tax(Variable):
    value_type = float
    entity = Household
    label = "NT payroll tax"
    definition_period = YEAR
    unit = "AUD"
    reference = (
        "https://legislation.nt.gov.au/en/Legislation/PAYROLL-TAX-ACT-2009"
    )

    def formula(household, period, parameters):
        # Get NT payroll tax parameters
        params = parameters(period).gov.states.nt.payroll_tax

        # Aggregate wages at household level
        wages = household.sum(household.members("employment_income", period))

        # Calculate tax for NT employers
        threshold = params.threshold
        rate = params.rate

        taxable_wages = max_(wages - threshold, 0)

        return taxable_wages * rate
