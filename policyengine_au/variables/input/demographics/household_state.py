"""
Household state of residence variable for Australian jurisdictions.
"""

from policyengine_au.model_api import *
from policyengine_au.variables.input.demographics.state import StateCode


class household_state(Variable):
    value_type = Enum
    possible_values = StateCode
    default_value = StateCode.NSW
    entity = Household
    definition_period = YEAR
    label = "Household state or territory of residence"
    documentation = "The Australian state or territory where the household resides (based on household head)"

    def formula(household, period, parameters):
        # Use the state of the household head (first person)
        return household.value_from_first_person(
            household.members("state", period)
        )
