"""Age Pension eligibility determination."""

from policyengine_au.model_api import *


class age_pension_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Age Pension eligible"
    documentation = "Whether the person is eligible for Age Pension"
    reference = "https://www.servicesaustralia.gov.au/who-can-get-age-pension"

    def formula(person, period, parameters):
        age = person("age", period)
        p = parameters(period).gov.dss.age_pension

        # Check age eligibility (current threshold is 67)
        age_eligible = age >= p.eligibility.age_threshold

        # TODO: Add residence requirements check
        # For now, assume residence requirements are met
        residence_eligible = True

        return age_eligible & residence_eligible
