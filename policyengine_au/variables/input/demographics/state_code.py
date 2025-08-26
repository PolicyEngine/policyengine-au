"""
Australian state and territory codes.
"""

from policyengine_core.model_api import Enum


class StateCode(Enum):
    NSW = "NSW"
    VIC = "VIC"
    QLD = "QLD"
    WA = "WA"
    SA = "SA"
    TAS = "TAS"
    ACT = "ACT"
    NT = "NT"