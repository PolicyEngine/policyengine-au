"""
Type definitions for PolicyEngine Australia.

This module provides type hints and type aliases used throughout
the Australian tax-benefit model.
"""

from typing import TYPE_CHECKING, Dict, Any, Union, List, Optional
from numpy.typing import ArrayLike
import numpy as np

if TYPE_CHECKING:
    from policyengine_core.entities import Entity
    from policyengine_core.parameters import ParameterNode
    from policyengine_core.periods import Period
    from policyengine_core.populations import Population
    from policyengine_core.simulations import Simulation
    from policyengine_core.variables import Variable


# Type aliases for common PolicyEngine types
Formula = Any  # Variable formula function
ParameterType = Union[float, int, bool, str]
ArrayType = Union[np.ndarray, ArrayLike]

# Australian-specific type aliases
StateCode = str  # NSW, VIC, QLD, SA, WA, TAS, NT, ACT
PostCode = str  # Australian postcode (4 digits)
TaxFileNumber = str  # Tax File Number
CentrelinkCRN = str  # Centrelink Customer Reference Number

# Income types
IncomeAmount = float
TaxAmount = float
BenefitAmount = float

# Time periods
FinancialYear = str  # e.g., "2023-24"
CalendarYear = int  # e.g., 2024
