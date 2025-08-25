"""
PolicyEngine Australia microsimulation model.

This package implements Australia's tax and benefit system using the
PolicyEngine Core framework (based on OpenFisca).
"""

from policyengine_au.system import AustralianTaxBenefitSystem
from policyengine_au.model_api import *

__version__ = "0.1.0"
__all__ = ["AustralianTaxBenefitSystem", "Simulation"]
