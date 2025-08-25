# PolicyEngine Development Approach

This document outlines the systematic approach used to build PolicyEngine microsimulation models for different countries, based on the implementation of PolicyEngine Australia, Israel, and New Zealand.

## Core Development Principles

### 1. Test-Driven Development (TDD)
- Write comprehensive test cases before implementation
- Use YAML-based tests for policy scenarios
- Validate against official government calculators
- Ensure edge cases are covered

### 2. Government Source References
- Every parameter must reference official sources
- Use primary legislation and government websites
- Include URLs for traceability
- Update when policies change

### 3. Modern Python Tooling
- Use `uv` for fast package management
- Python 3.13 as primary version (3.10+ supported)
- Black formatter with 79-character line length
- Type hints where beneficial

### 4. Continuous Integration
- GitHub Actions for CI/CD
- Test on multiple Python versions
- Automated formatting checks
- Coverage tracking with codecov

### 5. Documentation with Jupyter Book 2.0
- Use MyST-NB (next.jupyterbook.org) not legacy JB
- Focus on program coverage documentation
- Clear input/output specifications
- Year coverage tracking

## Country Implementation Process

### Phase 1: Foundation (Day 1)
1. **Project Structure**
   ```
   policyengine-{country}/
   ├── policyengine_{country}/
   │   ├── entities.py          # Define tax units, families, households
   │   ├── system.py            # Main system class
   │   ├── model_api.py        # Common imports
   │   ├── parameters/          # YAML parameter files
   │   │   └── gov/            # Organized by agency
   │   ├── variables/          # Python calculation files
   │   │   └── gov/            # Mirror parameter structure
   │   └── tests/              # Comprehensive test suite
   ├── docs/                   # Jupyter Book documentation
   ├── .github/workflows/      # CI/CD configuration
   ├── pyproject.toml         # Modern Python packaging
   ├── Makefile               # Development commands
   └── README.md              # Comprehensive documentation
   ```

2. **Entity Definitions**
   - Person (individual)
   - TaxUnit (tax filing unit)
   - Family/BenefitUnit (benefit assessment unit)
   - Household (physical residence)

3. **Core Configuration**
   - pyproject.toml with hatchling build system
   - GitHub Actions for CI/CD
   - Black formatting configuration
   - pytest setup

### Phase 2: Tax System (Days 2-3)
1. **Income Tax**
   - Progressive tax brackets
   - Tax-free thresholds
   - Credits and offsets

2. **Social Insurance**
   - Health insurance levies
   - Social security contributions
   - Pension contributions

3. **Other Taxes**
   - Consumption taxes (VAT/GST)
   - Property taxes
   - State/regional taxes

### Phase 3: Benefit System (Days 3-4)
1. **Social Security**
   - Unemployment benefits
   - Disability support
   - Age pensions

2. **Family Support**
   - Child benefits
   - Childcare subsidies
   - Parental leave

3. **Means Testing**
   - Income tests
   - Asset tests
   - Taper rates

### Phase 4: Testing & Documentation (Day 5)
1. **Test Coverage**
   - Unit tests for each variable
   - YAML scenario tests
   - Cross-validation with official calculators

2. **Documentation**
   - Program coverage tables
   - Input/output specifications
   - Developer guide
   - API reference

## Country-Specific Considerations

### Australia
- Complex means-testing with income and asset tests
- Fortnightly payment periods
- State variations in taxes
- Superannuation system integration

### Israel  
- Bituach Leumi (National Insurance)
- Points-based tax credits
- Child allowances by number of children
- Military service considerations

### New Zealand
- Simple tax system (few deductions)
- Working for Families tax credits
- Accommodation Supplement
- KiwiSaver integration

## Parameter Organization

### Structure by Government Agency
```yaml
parameters/
└── gov/
    ├── tax_authority/      # Tax parameters
    │   ├── income_tax/
    │   ├── vat_gst/
    │   └── credits/
    ├── social_security/    # Benefit parameters
    │   ├── pensions/
    │   ├── unemployment/
    │   └── family/
    └── treasury/          # Economic parameters
        ├── cpi/
        └── thresholds/
```

### Parameter File Format
```yaml
description: Clear description of parameter
reference:
  - title: Official source name
    href: https://government-website.gov
metadata:
  unit: currency-XXX or /1 for rates
  period: year/month/fortnight
  uprating: gov.treasury.cpi  # Optional
values:
  2023-01-01: 1000
  2024-01-01: 1050
```

## Variable Implementation

### Standard Pattern
```python
from policyengine_{country}.model_api import *

class variable_name(Variable):
    value_type = float
    entity = Person  # or TaxUnit, Family, Household
    definition_period = YEAR  # or MONTH, FORTNIGHT
    label = "Human-readable label"
    documentation = "Detailed description"
    reference = "https://official-source.gov"
    unit = "currency-XXX"
    
    def formula(person, period, parameters):
        # Get inputs
        income = person("income_variable", period)
        
        # Get parameters
        p = parameters(period).gov.agency.program
        threshold = p.threshold
        rate = p.rate
        
        # Calculate result
        return income * rate
```

## Testing Strategy

### YAML Test Format
```yaml
- name: Descriptive test name
  period: 2024
  input:
    people:
      person_1:
        age: 30
        employment_income: 50000
    households:
      household:
        members: [person_1]
  output:
    income_tax: 7500
    net_income: 42500
```

### Test Categories
1. **Baseline Tests**: Standard scenarios
2. **Edge Cases**: Boundary conditions
3. **Reform Tests**: Policy changes
4. **Integration Tests**: Complex households

## CI/CD Configuration

### Pull Request Workflow
```yaml
name: PR
on: [pull_request]
jobs:
  lint:
    # Black formatting check
  test:
    # pytest on Python 3.10-3.13
  documentation:
    # Build Jupyter Book
```

### Main Branch Workflow
- Full test suite
- Documentation deployment
- Package building
- Optional PyPI publishing

## Documentation Requirements

### Essential Documentation
1. **README.md**: Overview, installation, quick start
2. **Tax Programs**: All tax calculations with rates
3. **Benefit Programs**: All benefits with eligibility
4. **Developer Guide**: Contributing instructions
5. **API Reference**: Technical documentation

### Documentation Standards
- Government source references
- Current rates and thresholds
- Implementation status tracking
- Examples and use cases

## Common Pitfalls to Avoid

1. **Missing Variables**: Add all input variables even if defaulting to 0
2. **Period Mismatches**: Ensure correct period conversions
3. **Parameter Dating**: Use correct date formats (YYYY-MM-DD)
4. **Test Coverage**: Test edge cases and boundaries
5. **Documentation**: Keep docs synchronized with code

## Validation Checklist

Before considering a country model complete:

- [ ] All major taxes implemented
- [ ] Core benefit programs covered
- [ ] Comprehensive test suite passing
- [ ] Documentation complete
- [ ] CI/CD pipeline green
- [ ] Government sources referenced
- [ ] Code formatted with Black
- [ ] README with clear examples

## Extension Guidelines

### Adding New Programs
1. Research official sources
2. Create parameter files
3. Write tests first (TDD)
4. Implement variables
5. Update documentation
6. Validate against official calculators

### Handling Complexity
- Start with simple cases
- Add complexity incrementally
- Test each addition
- Document assumptions

## Performance Considerations

- Use vectorized NumPy operations
- Cache expensive calculations
- Optimize parameter lookups
- Profile before optimizing

## Future Enhancements

### Planned Features
- Behavioral responses
- Dynamic scoring
- Microsimulation datasets
- Web API integration
- Regional variations

### Integration Points
- PolicyEngine web application
- PolicyEngine API
- Country-specific datasets
- Reform analysis tools

---

This approach ensures consistent, high-quality implementations across all countries while allowing for country-specific adaptations.

## Coverage Summary

### PolicyEngine Australia (AU)
**Tax Programs:**
- ✅ Personal Income Tax (progressive brackets with Stage 3 cuts)
- ✅ Medicare Levy (2% with low-income thresholds)
- ✅ Medicare Levy Surcharge (high earners without private insurance)
- ✅ HECS-HELP Student Loan Repayments (18 bands)
- ✅ Superannuation Guarantee (11.5% rising to 12%)
- ⏳ Capital Gains Tax
- ⏳ GST (10%)

**Benefit Programs:**
- ✅ Age Pension (income/assets tested)
- ✅ JobSeeker Payment
- ✅ Disability Support Pension
- ✅ Family Tax Benefit Parts A & B
- ✅ Child Care Subsidy
- ⏳ Youth Allowance
- ⏳ Parenting Payment
- ⏳ Rent Assistance

### PolicyEngine Ireland (IE)
**Tax Programs:**
- ✅ Income Tax (20% standard, 40% higher)
- ✅ USC (4 bands: 0.5%, 2%, 4%, 8%)
- ✅ PRSI (4.1% employee, 8.9%/11.15% employer)
- ✅ Tax Credits (personal, PAYE, age, rent)
- ⏳ VAT (23% standard, 13.5%/9% reduced)
- ⏳ Capital Acquisitions Tax

**Benefit Programs:**
- ✅ Jobseeker's Allowance
- ✅ State Pension (Contributory/Non-Contributory)
- ✅ Child Benefit
- ✅ Working Family Payment
- ✅ Disability Allowance
- ✅ Housing Assistance Payment (HAP)
- ⏳ One-Parent Family Payment
- ⏳ Carer's Allowance

### PolicyEngine New Zealand (NZ)
**Tax Programs:**
- ✅ Income Tax (5 brackets: 10.5%-39%)
- ✅ ACC Earner's Levy (1.67%)
- ✅ KiwiSaver (3% minimum)
- ⏳ GST (15%)
- ⏳ Fringe Benefit Tax

**Benefit Programs:**
- ✅ Working for Families Tax Credits
- ✅ Best Start Tax Credit
- ✅ In-Work Tax Credit
- ✅ Jobseeker Support
- ✅ NZ Superannuation (universal at 65)
- ✅ Accommodation Supplement
- ⏳ Sole Parent Support
- ⏳ Supported Living Payment
- ⏳ Winter Energy Payment

## Implementation Status

| Country | Core Structure | Tax System | Benefits | Tests | CI/CD | Documentation |
|---------|---------------|------------|----------|-------|-------|---------------|
| Australia | ✅ Complete | 80% | 70% | ✅ | ✅ | ✅ |
| Ireland | ✅ Complete | 85% | 75% | ✅ | ✅ | ✅ |
| New Zealand | ✅ Complete | 75% | 80% | ✅ | ✅ | ✅ |

## Known Issues and TODOs

### Critical Fixes Applied
- ✅ Fixed linecheck dependency version
- ✅ Added missing currency definitions
- ✅ Created missing input variables
- ✅ Fixed parameter structure mismatches

### Remaining Enhancements
- Add microsimulation datasets
- Implement behavioral responses
- Complete state/regional variations
- Add consumption tax modeling
- Integrate with PolicyEngine web app