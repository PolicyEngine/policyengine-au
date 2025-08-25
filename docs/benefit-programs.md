# Benefit Programs

Comprehensive documentation of Australian social security and family assistance programs.

## Age Pension

### Eligibility
- **Age**: 67 years (born after 1 January 1957)
- **Residence**: 10 years Australian residence, including 5 continuous years

### Payment Rates (March 2024)

| Category | Basic Rate | Pension Supplement | Energy Supplement | Total (fortnight) |
|----------|------------|-------------------|-------------------|-------------------|
| Single | $1,144.40 | $85.20 | $14.10 | $1,243.70 |
| Couple (each) | $862.60 | $64.20 | $10.60 | $937.40 |
| Couple separated (illness) | $1,144.40 | $85.20 | $14.10 | $1,243.70 |

### Means Testing

#### Income Test
- **Free Area**: $212/fortnight (single), $372/fortnight (couple combined)
- **Taper Rate**: 50 cents per dollar above free area
- **Work Bonus**: $300/fortnight employment income exempt (can accrue to $11,800)

#### Assets Test

| Category | Homeowner | Non-homeowner |
|----------|-----------|---------------|
| Single - Free area | $314,000 | $566,000 |
| Single - Cut-off | $695,500 | $947,500 |
| Couple - Free area | $470,000 | $722,000 |
| Couple - Cut-off | $1,045,500 | $1,297,500 |

- **Taper Rate**: $3.00 per fortnight per $1,000 above free area

**Reference**: [Age Pension](https://www.servicesaustralia.gov.au/age-pension)

## JobSeeker Payment

### Payment Rates (September 2024)

| Category | Rate (fortnight) |
|----------|------------------|
| Single, no children | $762.70 |
| Single, with dependent children | $824.60 |
| Single, principal carer | $1,015.70 |
| Partnered (each) | $695.00 |

### Income Test
- **Free Area**: $150/fortnight
- **Taper Rates**: 
  - 40 cents per dollar between $150-$256
  - 60 cents per dollar above $256
- **Working Credit**: Can accrue up to $11,800

**Reference**: [JobSeeker Payment](https://www.servicesaustralia.gov.au/jobseeker-payment)

## Family Tax Benefit

### Part A - Per Child Rates

| Age | Maximum Rate | Base Rate |
|-----|--------------|-----------|
| 0-12 years | $225.12/fortnight | $70.46/fortnight |
| 13-15 years | $292.18/fortnight | $70.46/fortnight |
| 16-19 years (studying) | $292.18/fortnight | $86.70/fortnight |

**Income Test**:
- Maximum rate: Family income up to $63,166/year
- Reduces by 20 cents per dollar to base rate
- Base rate: Cuts out at $111,038/year + $11,657 per additional child

### Part B - Family Payment

| Youngest Child Age | Maximum Rate (fortnight) |
|-------------------|-------------------------|
| Under 5 years | $189.78 |
| 5-18 years | $132.48 |

**Income Test**:
- Primary earner limit: $103,000/year (couples)
- Secondary earner free area: $6,716/year
- Taper: 20 cents per dollar

**Reference**: [Family Tax Benefit](https://www.servicesaustralia.gov.au/family-tax-benefit)

## Child Care Subsidy

### Subsidy Rates by Income (2024-25)

| Family Income | Subsidy Rate |
|---------------|--------------|
| Up to $79,163 | 90% |
| $79,163 - $89,163 | 90% tapering to 80% |
| $89,163 - $189,390 | 80% tapering to 50% |
| $189,390 - $204,390 | 50% tapering to 20% |
| $204,390 - $264,390 | 20% |
| $264,390 - $374,390 | 20% tapering to 0% |
| Above $374,390 | 0% |

### Hourly Rate Caps
- Centre-based day care: $14.32
- Family day care: $13.29
- Outside school hours care: $12.54

**Activity Test**: Hours of subsidised care based on activity level

**Reference**: [Child Care Subsidy](https://www.servicesaustralia.gov.au/child-care-subsidy)

## Disability Support Pension

### Payment Rates (March 2024)

| Category | Basic Rate | Supplement | Total (fortnight) |
|----------|------------|------------|-------------------|
| Single, 21+ | $1,173.90 | $89.90 | $1,277.90 |
| Single, under 21 (independent) | $841.80 | $89.90 | $945.80 |
| Couple (each) | $884.20 | $67.70 | $962.50 |

**Youth Disability Supplement**: $159.70/fortnight (under 21)

### Eligibility
- Permanent physical, intellectual or psychiatric impairment
- Unable to work 15+ hours per week
- Condition fully diagnosed, treated and stabilised

**Reference**: [Disability Support Pension](https://www.servicesaustralia.gov.au/disability-support-pension)

## Other Major Programs

### Parenting Payment
- **Single**: $1,015.70/fortnight
- **Partnered**: $713.00/fortnight
- Eligibility: Primary carer of child under 6 (partnered) or 8 (single)

### Youth Allowance
- Students and job seekers aged 16-24
- Rates vary by age, living situation, and study/work status
- Parental income test may apply

### Carer Payment
- For those providing full-time care
- Same rate as Age Pension
- Income and assets tested

### Rent Assistance
- Maximum rates vary by family situation
- Singles: Up to $184.80/fortnight
- Couples: Up to $173.86/fortnight
- Additional amounts for children

## Implementation Status

### Currently Implemented
✅ Age Pension (rates, income test, assets test)
✅ JobSeeker Payment (rates, income test)
✅ Family Tax Benefit Part A & B
✅ Child Care Subsidy
✅ Disability Support Pension

### Planned Implementation
⏳ Parenting Payment
⏳ Youth Allowance
⏳ Austudy/ABSTUDY
⏳ Carer Payment and Allowance
⏳ Rent Assistance
⏳ Various supplements and concession cards

## Testing Approach

All benefit calculations validated against:
- Services Australia payment calculators
- Published rate tables
- Real household scenarios
- Income test boundary conditions

See `tests/policy/baseline/` for comprehensive test coverage.