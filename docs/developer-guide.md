# Developer Guide

This guide explains how to contribute to PolicyEngine Australia and extend the model with new parameters, variables, and reforms.

## Development Approach

PolicyEngine Australia follows these key principles:

### 1. Test-Driven Development (TDD)
- Write tests first, then implementation
- Comprehensive test coverage for all calculations
- YAML-based policy tests for easy scenario creation

### 2. Government Source References
- All parameters linked to official sources
- Regular updates when rates change
- Clear documentation trail

### 3. Continuous Integration
- Automated testing on all pull requests
- Code formatting with Black (79 chars)
- Python 3.10-3.13 compatibility

### 4. Modern Python Tooling
- `uv` for fast package management
- `pytest` for testing
- `myst` (Jupyter Book 2.0) for documentation

## Setting Up Development Environment

### Prerequisites
- Python 3.10 or higher (3.13 recommended)
- Git
- uv (recommended) or pip

### Installation

```bash
# Clone the repository
git clone https://github.com/PolicyEngine/policyengine-au.git
cd policyengine-au

# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install the package in development mode
uv pip install --system -e .[dev]

# Or with pip
pip install -e .[dev]
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=policyengine_au

# Run specific test file
uv run pytest policyengine_au/tests/policy/baseline/test_income_tax.yaml

# Run only YAML policy tests
uv run pytest policyengine_au/tests/policy -v
```

### Code Formatting

```bash
# Format code
make format

# Or manually
black . -l 79
linecheck . --fix

# Check formatting (CI will fail if not formatted)
black . -l 79 --check
```

## Adding New Parameters

Parameters define values that change over time (rates, thresholds, amounts).

### 1. Create YAML Parameter File

```yaml
# policyengine_au/parameters/gov/dss/new_benefit/payment_rate.yaml
description: New Benefit payment rate
reference:
  - title: Official source title
    href: https://government-source-url.gov.au
metadata:
  unit: currency-AUD
  period: fortnight
  label: New Benefit rate
  uprating: gov.treasury.cpi  # Optional: automatic uprating
values:
  2023-07-01: 500.00
  2024-01-01: 515.00
  2024-07-01: 530.00
```

### 2. Parameter Organization

Place parameters in appropriate directory:
- `gov/ato/` - Tax parameters
- `gov/dss/` - Social services parameters
- `gov/treasury/` - Economic parameters
- `gov/states/` - State-specific parameters

## Adding New Variables

Variables calculate values based on parameters and other variables.

### 1. Create Variable File

```python
# policyengine_au/variables/gov/dss/new_benefit/new_benefit_payment.py
"""New Benefit payment calculation."""

from policyengine_au.model_api import *


class new_benefit_payment(Variable):
    value_type = float
    entity = Person  # or TaxUnit, Family, Household
    definition_period = YEAR  # or MONTH, FORTNIGHT
    label = "New Benefit payment"
    documentation = "Total New Benefit payment amount"
    reference = "https://official-source.gov.au"
    unit = AUD
    
    def formula(person, period, parameters):
        # Get eligibility
        eligible = person("new_benefit_eligible", period)
        
        # Get payment rate from parameters
        p = parameters(period).gov.dss.new_benefit
        payment_rate = p.payment_rate
        
        # Convert fortnight to year if needed
        annual_payment = payment_rate * 26  # 26 fortnights per year
        
        return eligible * annual_payment
```

### 2. Variable Best Practices

- One variable per file
- Clear, descriptive names
- Include documentation and references
- Handle edge cases
- Use vectorized operations (numpy)

## Writing Tests

### 1. YAML Policy Tests

```yaml
# policyengine_au/tests/policy/baseline/test_new_benefit.yaml
- name: Single person eligible for new benefit
  period: 2024
  input:
    people:
      person_1:
        age: 25
        employment_income: 0
        new_benefit_eligible: true
    households:
      household:
        members: [person_1]
  output:
    new_benefit_payment: 13_780  # $530 * 26 fortnights

- name: Person not eligible receives no benefit
  period: 2024
  input:
    people:
      person_1:
        age: 25
        employment_income: 50_000
        new_benefit_eligible: false
  output:
    new_benefit_payment: 0
```

### 2. Python Unit Tests

```python
# policyengine_au/tests/variables/test_new_benefit.py
import pytest
from policyengine_au import AustralianTaxBenefitSystem


def test_new_benefit_calculation():
    system = AustralianTaxBenefitSystem()
    simulation = system.new_simulation()
    
    # Set inputs
    simulation.set_input("age", 2024, [25])
    simulation.set_input("new_benefit_eligible", 2024, [True])
    
    # Calculate result
    result = simulation.calculate("new_benefit_payment", 2024)
    
    # Assert expected value
    assert result[0] == 13_780
```

## Creating Reforms

Reforms modify the baseline system for policy analysis.

### 1. Define Reform

```python
# policyengine_au/reforms/increase_jobseeker.py
from policyengine_au.model_api import *


def increase_jobseeker_by_50(parameters):
    """Increase JobSeeker payment by $50 per fortnight."""
    
    # Modify parameter
    p = parameters.gov.dss.jobseeker.payment_rates
    
    # Increase all rates by $50
    p.single.no_children.update(
        value=lambda v: v + 50,
        period="2024-01-01"
    )
    
    return parameters


# Create reform object
increase_jobseeker_reform = Reform(
    name="Increase JobSeeker by $50",
    parameter_reforms=[increase_jobseeker_by_50],
    country_id="au"
)
```

### 2. Test Reform

```python
def test_jobseeker_reform():
    # Apply reform to system
    baseline = AustralianTaxBenefitSystem()
    reformed = AustralianTaxBenefitSystem(
        reform=increase_jobseeker_reform
    )
    
    # Compare results
    # ... test implementation
```

## Documentation

### 1. Update Program Documentation

When adding new programs, update:
- `docs/tax-programs.md` for tax changes
- `docs/benefit-programs.md` for benefit changes
- Include rates, thresholds, eligibility

### 2. Build Documentation

```bash
# Build with MyST (Jupyter Book 2.0)
myst build docs

# View locally
open docs/_build/index.html
```

## CI/CD Pipeline

### Pull Request Checks
1. **Formatting**: Black and linecheck
2. **Tests**: All Python versions (3.10-3.13)
3. **Coverage**: Maintained above threshold
4. **Documentation**: Builds successfully

### Main Branch
- Runs full test suite
- Deploys documentation to GitHub Pages
- Prepares for PyPI release (when enabled)

## Contributing Checklist

Before submitting a PR:

- [ ] Code formatted with `make format`
- [ ] Tests written and passing
- [ ] Documentation updated
- [ ] Government sources referenced
- [ ] Changelog entry added
- [ ] PR description explains changes

## Common Patterns

### Income Testing

```python
def formula(person, period, parameters):
    income = person("assessable_income", period)
    p = parameters(period).gov.dss.payment
    
    free_area = p.income_test.free_area
    taper_rate = p.income_test.taper_rate
    max_payment = p.payment_rate
    
    reduction = max_(0, income - free_area) * taper_rate
    payment = max_(0, max_payment - reduction)
    
    return payment
```

### Age-Based Eligibility

```python
def formula(person, period, parameters):
    age = person("age", period)
    min_age = parameters(period).gov.program.min_age
    max_age = parameters(period).gov.program.max_age
    
    return (age >= min_age) & (age <= max_age)
```

### Period Conversion

```python
# Convert annual to fortnightly
fortnightly_amount = annual_amount / 26

# Convert monthly to annual
annual_amount = monthly_amount * 12
```

## Getting Help

- GitHub Issues: Bug reports and feature requests
- Discussions: Questions and ideas
- Documentation: This guide and API reference
- Examples: Test files show usage patterns