from policyengine_au.model_api import *


class state_payroll_tax(Variable):
    value_type = float
    entity = Household
    label = "State payroll tax (employer liability)"
    definition_period = YEAR
    unit = "AUD"
    documentation = (
        "Total employer payroll tax liability based on state/territory where wages are paid. "
        "This is a tax paid by employers on their total wage bill when it exceeds the threshold."
    )

    def formula(household, period, parameters):
        # Get household state and calculate appropriate tax
        state = household("household_state", period)

        # Map state to the appropriate payroll tax variable
        state_tax_map = {
            StateCode.NSW: "nsw_payroll_tax",
            StateCode.VIC: "vic_payroll_tax",
            StateCode.QLD: "qld_payroll_tax",
            StateCode.WA: "wa_payroll_tax",
            StateCode.SA: "sa_payroll_tax",
            StateCode.TAS: "tas_payroll_tax",
            StateCode.ACT: "act_payroll_tax",
            StateCode.NT: "nt_payroll_tax",
        }

        # Calculate tax for each state and select the appropriate one
        tax = zeros(household.count)
        for state_code, tax_variable in state_tax_map.items():
            is_state = state == state_code
            state_tax = household(tax_variable, period)
            tax = where(is_state, state_tax, tax)

        return tax
