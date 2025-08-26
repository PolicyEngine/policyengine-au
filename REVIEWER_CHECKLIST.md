# PolicyEngine Code Review Checklist

## 🚨 CRITICAL REQUIREMENT #1: MANDATORY VECTORIZATION 🚨

**AUTOMATICALLY FAIL any code that contains if-elif-else statements in formula methods**

This is NON-NEGOTIABLE. PolicyEngine formulas MUST be vectorized for performance.

### AUTO-FAIL Examples:
```python
# ❌ AUTOMATIC FAILURE - Not vectorized
def formula(household, period, parameters):
    if wages > threshold:
        tax = wages * rate_high
    else:
        tax = wages * rate_low
    return tax

# ❌ AUTOMATIC FAILURE - elif chains
def formula(household, period, parameters):
    if income <= 10_000:
        rate = low_rate
    elif income <= 100_000:
        rate = medium_rate
    else:
        rate = high_rate
    return income * rate
```

### REQUIRED Patterns:
```python
# ✅ PASS - Properly vectorized using where
def formula(household, period, parameters):
    return where(wages > threshold, wages * rate_high, wages * rate_low)

# ✅ BETTER - Select rate first then multiply
def formula(household, period, parameters):
    rate = where(wages > threshold, rate_high, rate_low)
    return wages * rate

# ✅ BEST - Boolean multiplication for simple cases
def formula(household, period, parameters):
    return (wages > threshold) * wages * rate_high

# ✅ REQUIRED - Use select with default for multiple conditions
def formula(household, period, parameters):
    rate = select(
        [wages <= 10_000, wages <= 100_000],
        [low_rate, medium_rate],
        default=high_rate  # MUST use default for performance
    )
    return wages * rate
```

## Other Critical Performance Requirements

### 2. Additional Performance Optimizations
- Prefer `condition * value` over `where(condition, value, 0)`
- Always use `select()` with `default` parameter
- Use `defined_for` for state-specific variables when possible
- Return calculations directly instead of storing in variables
- Keep intermediate calculations (like `taxable_wages`) only for clarity

## Code Quality Standards

### 1. Statutory References (CRITICAL)
- **Primary**: Legislative acts (e.g., "Payroll Tax Act 2007")
- **Secondary**: Regulations
- **Tertiary**: Government websites
- **Never**: No references at all

### 2. Import Patterns
- Use `from policyengine_au.model_api import *` for AU files
- Don't import entities separately if using model_api
- StateCode should be in model_api

### 3. Variable Patterns
- One variable per file
- Include regulatory citations in comments
- Use numpy functions (np.ceil, not ceil)
- Variables should inherit from Variable class

### 4. Parameter Files (YAML)
- Use underscore thousands separators (1_000_000)
- Include legislative references
- Organize by government department
- Values should have dates (2024-01-01)

## Testing Requirements

### 1. Test Coverage
- Test below threshold scenarios
- Test above threshold scenarios  
- Test boundary conditions
- Test tiered rate structures
- Test edge cases (zero, negative if applicable)

### 2. Test Format
- Use YAML test format
- Include period-specific inputs:
  ```yaml
  employment_income:
    2024: 100_000
  ```

## Common Anti-Patterns to Flag

1. **Non-vectorized code** (if/elif/else in formulas)
2. **Missing statutory references**
3. **Incorrect thousands separators** (1000000 vs 1_000_000)
4. **Using where(condition, value, 0)** instead of `condition * value`
5. **Not using select() default parameter**
6. **Creating new files instead of modifying existing ones**
7. **Forgetting to run formatters** (Black for Python)

## Review Process

**MANDATORY ORDER - Check in this sequence:**

1. 🚨 **FIRST: Check for if-elif-else (AUTOMATIC FAILURE)**
   - Any if-elif-else in formula methods = IMMEDIATE REJECTION
   - Provide clear explanation of vectorization requirements
   - Show specific examples of how to fix the code

2. ✅ **THEN: Check other requirements:**
   - Statutory references exist (Acts > Regulations > Websites)
   - Tests pass and cover edge cases
   - Code follows performance patterns
   - Formatting (Black with 79-char lines)
   - No duplicate files (_v2, _new versions)
   - Thousands separators with underscores (1_000_000)

**Remember: The vectorization requirement is MANDATORY and any violation should result in immediate review failure with clear explanation of how to fix it.**