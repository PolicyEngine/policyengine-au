"""
API imports for PolicyEngine Australia model development.

This module provides convenient imports for developing variables,
parameters, and reforms for the Australian tax-benefit system.
"""

# Import from policyengine_core
from policyengine_core.model_api import *

# Import Australian-specific entities
from policyengine_au.entities import (
    Person,
    TaxUnit,
    BenefitUnit,
    Family,
    Household,
)

# Currency unit
AUD = "currency-AUD"

# Import commonly used functions from core
from policyengine_core.model_api import *

# Common functions for Australian calculations
def add(entity, period, variables, options=None):
    """Sum multiple variables for an entity in a period."""
    return sum(
        entity(variable, period, options) 
        for variable in variables
    )


def subtract(entity, period, variables, options=None):
    """Subtract variables (first minus rest) for an entity in a period."""
    result = entity(variables[0], period, options)
    for variable in variables[1:]:
        result = result - entity(variable, period, options)
    return result


def multiply(entity, period, variables, options=None):
    """Multiply variables together for an entity in a period."""
    result = entity(variables[0], period, options)
    for variable in variables[1:]:
        result = result * entity(variable, period, options)
    return result