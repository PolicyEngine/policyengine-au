"""Age variable for individuals."""

from policyengine_au.model_api import *


class age(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Age"
    documentation = "Age of the person in years"
    reference = "https://www.abs.gov.au/statistics/people"
    
    # Set default value for testing
    default_value = 30