"""
State of residence variable for Australian jurisdictions.
"""

from policyengine_au.model_api import *


class StateCode(Enum):
    NSW = "NSW"
    VIC = "VIC"
    QLD = "QLD"
    WA = "WA"
    SA = "SA"
    TAS = "TAS"
    ACT = "ACT"
    NT = "NT"


class state(Variable):
    value_type = Enum
    possible_values = StateCode
    default_value = StateCode.NSW
    entity = Person
    definition_period = YEAR
    label = "State or territory of residence"
    documentation = (
        "The Australian state or territory where the person resides"
    )
    reference = "https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3"
