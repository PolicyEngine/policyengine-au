# PolicyEngine Australia

Welcome to PolicyEngine Australia - a comprehensive microsimulation model of Australia's tax and benefit system.

## Overview

PolicyEngine Australia models the Australian tax-benefit system, including:
- Personal income tax with progressive brackets
- Medicare levy and surcharge
- HECS-HELP student loan repayments
- Superannuation system
- Age Pension with means testing
- JobSeeker Payment
- Family Tax Benefits (Parts A and B)
- Child Care Subsidy
- Disability Support Pension
- And many more programs

## Key Features

- **Comprehensive Coverage**: Models all major federal taxes and benefits
- **Up-to-date Parameters**: Includes latest tax rates and benefit amounts
- **Government Sources**: All parameters referenced to official sources
- **Test-Driven Development**: Comprehensive test suite ensures accuracy
- **Open Source**: AGPL-3.0 licensed for transparency

## Quick Start

```python
from policyengine_au import AustralianTaxBenefitSystem
from policyengine_core.simulations import Simulation

# Create the tax-benefit system
system = AustralianTaxBenefitSystem()

# Define a household
situation = {
    "people": {
        "person1": {
            "age": {"2024": 35},
            "employment_income": {"2024": 80000}
        }
    },
    "households": {
        "household": {
            "members": ["person1"]
        }
    }
}

# Run simulation
simulation = Simulation(
    tax_benefit_system=system,
    situation=situation
)

# Calculate income tax
income_tax = simulation.calculate("income_tax", "2024")
print(f"Income tax: ${income_tax[0]:,.2f}")
```

## Documentation Structure

- **[Overview](overview.md)**: Understanding the Australian tax-benefit system
- **[Tax Programs](tax-programs.md)**: Detailed documentation of tax calculations
- **[Benefit Programs](benefit-programs.md)**: Social security and family assistance
- **[Developer Guide](developer-guide.md)**: Contributing and extending the model
- **[API Reference](api-reference.md)**: Technical documentation

## Contributing

PolicyEngine Australia is open source and welcomes contributions. See our [Developer Guide](developer-guide.md) for information on:
- Setting up a development environment
- Adding new parameters or variables
- Writing tests
- Submitting pull requests

## License

PolicyEngine Australia is licensed under the GNU Affero General Public License v3.0.