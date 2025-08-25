# PolicyEngine Australia

[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)](https://www.python.org/)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

PolicyEngine Australia is a free, open-source microsimulation model of Australia's tax and benefit system. It enables users to calculate taxes and benefits for individual households and analyze the distributional impacts of policy reforms.

## Features

### Comprehensive Tax Modeling
- Personal income tax with progressive brackets
- Medicare levy and surcharge
- HECS-HELP student loan repayments
- Superannuation contributions and tax treatment
- Capital gains tax (coming soon)
- GST modeling (coming soon)

### Social Security Benefits
- Age Pension with means testing
- JobSeeker Payment
- Disability Support Pension
- Family Tax Benefit (Parts A & B)
- Child Care Subsidy
- Youth Allowance (coming soon)
- Parenting Payment (coming soon)

### Key Capabilities
- **Up-to-date parameters**: Latest tax rates and benefit amounts
- **Government sources**: All parameters referenced to official sources
- **Test-driven development**: Comprehensive test coverage
- **Reform analysis**: Model policy changes and impacts
- **Open source**: Transparent and auditable

## Installation

### Requirements
- Python 3.10 or higher (3.13 recommended)
- pip or uv package manager

### Install from source

```bash
# Clone the repository
git clone https://github.com/PolicyEngine/policyengine-au.git
cd policyengine-au

# Install with uv (recommended)
uv pip install --system -e .

# Or with pip
pip install -e .
```

### Install from PyPI (coming soon)

```bash
pip install policyengine-au
```

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

# Calculate values
income_tax = simulation.calculate("income_tax", "2024")
medicare_levy = simulation.calculate("medicare_levy", "2024")

print(f"Income tax: ${income_tax[0]:,.2f}")
print(f"Medicare levy: ${medicare_levy[0]:,.2f}")
```

## Documentation

Full documentation is available at: [https://policyengine.github.io/policyengine-au](https://policyengine.github.io/policyengine-au)

- [Tax Programs](docs/tax-programs.md) - Detailed tax calculations
- [Benefit Programs](docs/benefit-programs.md) - Social security programs
- [Developer Guide](docs/developer-guide.md) - Contributing guide
- [API Reference](docs/api-reference.md) - Technical documentation

## Development

### Setting up development environment

```bash
# Install development dependencies
uv pip install --system -e .[dev]

# Run tests
uv run pytest

# Format code
make format

# Build documentation
myst build docs
```

### Running tests

```bash
# Run all tests with coverage
uv run pytest --cov=policyengine_au

# Run specific test file
uv run pytest policyengine_au/tests/policy/baseline/test_income_tax.yaml

# Run only unit tests
uv run pytest policyengine_au/tests -k "not yaml"
```

## Contributing

We welcome contributions! Please see our [Developer Guide](docs/developer-guide.md) for:
- Setting up your development environment
- Adding new parameters and variables
- Writing tests
- Submitting pull requests

### Key principles
1. **Test-driven development**: Write tests first
2. **Government sources**: Reference all parameters
3. **Code quality**: Format with Black (79 chars)
4. **Documentation**: Update docs with changes

## Data and Validation

PolicyEngine Australia is validated against:
- Australian Taxation Office calculators
- Services Australia payment calculators
- Published government rate tables
- Academic microsimulation models (STINMOD+, MITTS)

## License

PolicyEngine Australia is licensed under the [GNU Affero General Public License v3.0](LICENSE).

## Citation

If you use PolicyEngine Australia in your research, please cite:

```bibtex
@software{policyengine_australia,
  title = {PolicyEngine Australia},
  author = {PolicyEngine},
  year = {2024},
  url = {https://github.com/PolicyEngine/policyengine-au}
}
```

## Support

- **Issues**: [GitHub Issues](https://github.com/PolicyEngine/policyengine-au/issues)
- **Discussions**: [GitHub Discussions](https://github.com/PolicyEngine/policyengine-au/discussions)
- **Email**: hello@policyengine.org
- **Website**: [policyengine.org](https://policyengine.org)

## Acknowledgments

PolicyEngine Australia builds on:
- [OpenFisca](https://openfisca.org/) framework via PolicyEngine Core
- Australian government data and documentation
- Open source tax-benefit modeling community

## Roadmap

### Near-term (Q1 2025)
- Complete Youth Allowance implementation
- Add Parenting Payment
- Implement Rent Assistance
- Add state payroll taxes

### Medium-term (Q2-Q3 2025)
- GST modeling with consumption data
- Capital gains tax
- State stamp duties
- Integration with PolicyEngine web app

### Long-term
- Full state and territory tax systems
- Local government rates
- Behavioral responses
- Dynamic scoring capabilities

---

**Note**: This model is under active development. Parameters are updated regularly to reflect policy changes. Always verify calculations against official sources for critical applications.