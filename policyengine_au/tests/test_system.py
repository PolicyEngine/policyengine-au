"""Test the Australian tax-benefit system initialization."""

import pytest
from policyengine_au import AustralianTaxBenefitSystem


def test_system_initialization():
    """Test that the system initializes correctly."""
    system = AustralianTaxBenefitSystem()
    assert system is not None
    assert hasattr(system, "entities")
    assert hasattr(system, "parameters")
    assert hasattr(system, "variables")


def test_entities_loaded():
    """Test that all entities are properly loaded."""
    system = AustralianTaxBenefitSystem()

    # Check all expected entities exist
    expected_entities = [
        "person",
        "tax_unit",
        "benefit_unit",
        "family",
        "household",
    ]
    entity_keys = {entity.key for entity in system.entities}

    for entity_name in expected_entities:
        assert (
            entity_name in entity_keys
        ), f"Entity {entity_name} not found in {entity_keys}"

    # Check that person_entity is accessible (main entity)
    assert system.person_entity is not None
    assert system.person_entity.key == "person"


def test_parameters_loaded():
    """Test that parameters are loaded from YAML files."""
    system = AustralianTaxBenefitSystem()
    parameters = system.parameters

    # Test that key parameter nodes exist
    assert hasattr(parameters, "gov")
    assert hasattr(parameters.gov, "ato")
    assert hasattr(parameters.gov, "dss")

    # Test specific parameter values for 2024
    period = "2024-07-01"
    p_2024 = parameters(period)

    # Test income tax parameters
    assert (
        p_2024.gov.ato.income_tax.thresholds.thresholds.tax_free_threshold
        == 18_200
    )
    assert p_2024.gov.ato.income_tax.rates.rates.bracket_2 == 0.19

    # Test Medicare levy
    assert p_2024.gov.ato.medicare.levy_rate == 0.02
