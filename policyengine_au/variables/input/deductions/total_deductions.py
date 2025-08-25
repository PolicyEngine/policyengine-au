"""Total tax deductions variable."""

from policyengine_au.model_api import *


class total_deductions(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Total deductions"
    documentation = "Total allowable tax deductions"
    reference = "https://www.ato.gov.au/individuals-and-families/income-and-deductions/deductions-you-can-claim"
    unit = AUD

    default_value = 0
