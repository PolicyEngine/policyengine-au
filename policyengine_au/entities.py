"""
Entity definitions for the Australian tax and benefit system.

References:
- Australian Taxation Office: https://www.ato.gov.au/
- Services Australia: https://www.servicesaustralia.gov.au/
- Department of Social Services: https://www.dss.gov.au/
"""

from policyengine_core.entities import build_entity


Person = build_entity(
    key="person",
    plural="people",
    label="Person",
    doc="""
    An individual person in Australia.
    
    This is the base entity for all individual-level calculations including
    income tax, Medicare levy, and individual social security payments.
    """,
    is_person=True,
)


TaxUnit = build_entity(
    key="tax_unit",
    plural="tax_units",
    label="Tax unit",
    doc="""
    An Australian tax filing unit.
    
    In Australia, individuals generally file taxes separately, but there are
    some provisions for couples (e.g., spouse rebates, family tax offsets).
    This entity represents a tax return filing unit.
    
    Reference: https://www.ato.gov.au/individuals-and-families/lodging-your-tax-return
    """,
    containing_entities=["household"],
    roles=[
        {
            "key": "primary",
            "plural": "primaries",
            "label": "Primary taxpayer",
            "doc": "The primary person filing the tax return",
        },
        {
            "key": "spouse",
            "plural": "spouses",
            "label": "Spouse",
            "doc": "The spouse of the primary taxpayer (if applicable)",
            "max": 1,
        },
        {
            "key": "dependent",
            "plural": "dependents",
            "label": "Dependent",
            "doc": "Dependent children or other dependents",
        },
    ],
)


BenefitUnit = build_entity(
    key="benefit_unit",
    plural="benefit_units",
    label="Benefit unit",
    doc="""
    A social security assessment unit for Centrelink payments.
    
    This represents the unit used to assess eligibility and calculate payments
    for Australian social security benefits. It typically includes a person,
    their partner (if applicable), and dependent children.
    
    Reference: https://www.servicesaustralia.gov.au/income-test-for-pensions
    """,
    containing_entities=["household"],
    roles=[
        {
            "key": "adult",
            "plural": "adults",
            "label": "Adult",
            "doc": "Adult member of the benefit unit",
            "max": 2,
        },
        {
            "key": "child",
            "plural": "children",
            "label": "Child",
            "doc": "Dependent child in the benefit unit",
        },
    ],
)


Family = build_entity(
    key="family",
    plural="families",
    label="Family",
    doc="""
    A family unit for family assistance payments.
    
    Used primarily for Family Tax Benefit, Child Care Subsidy, and other
    family assistance programs. Includes parents/guardians and dependent children.
    
    Reference: https://www.servicesaustralia.gov.au/family-tax-benefit
    """,
    containing_entities=["household"],
    roles=[
        {
            "key": "parent",
            "plural": "parents",
            "label": "Parent",
            "doc": "Parent or guardian in the family",
            "max": 2,
        },
        {
            "key": "child",
            "plural": "children",
            "label": "Child",
            "doc": "Dependent child in the family",
        },
    ],
)


Household = build_entity(
    key="household",
    plural="households",
    label="Household",
    doc="""
    A physical household in Australia.
    
    This represents all people living at the same address, used for
    household-level calculations such as rent assistance and some
    means testing provisions.
    
    Reference: https://www.abs.gov.au/statistics/people/housing
    """,
    roles=[
        {
            "key": "member",
            "plural": "members",
            "label": "Member",
            "doc": "A person living in the household",
        },
    ],
)


entities = [Person, TaxUnit, BenefitUnit, Family, Household]
