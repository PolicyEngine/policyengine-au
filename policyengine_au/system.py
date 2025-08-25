"""
Australian tax and benefit system implementation.

This module defines the main tax-benefit system class that loads all
parameters and variables for Australia's social and fiscal policies.
"""

from policyengine_core.taxbenefitsystems import TaxBenefitSystem
from policyengine_au.entities import entities
from pathlib import Path
import os


COUNTRY_DIR = Path(__file__).parent


class AustralianTaxBenefitSystem(TaxBenefitSystem):
    """
    The Australian tax and benefit system.
    
    This class represents the complete Australian tax and benefit system,
    including federal taxes, social security payments, family assistance,
    and state-level policies.
    """
    
    entities = entities
    parameters_dir = COUNTRY_DIR / "parameters"
    variables_dir = COUNTRY_DIR / "variables"
    auto_carry_over_input_variables = True
    basic_inputs = [
        "age",
        "employment_income", 
        "self_employment_income",
        "investment_income",
        "rental_income",
        "superannuation_contributions",
        "is_disabled",
        "is_carer",
        "is_student",
        "rent",
        "state",
        "postcode",
    ]
    
    def __init__(self, reform=None):
        """
        Initialize the Australian tax-benefit system.
        
        Args:
            reform: Optional reform to apply to the baseline system
        """
        super().__init__(entities)
        
        # Apply reform if provided
        if reform is not None:
            self.apply_reform(reform)
    
    # Entity properties are handled by parent class