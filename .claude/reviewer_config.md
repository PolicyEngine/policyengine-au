# PolicyEngine Reviewer Configuration

When reviewing PolicyEngine code, ALWAYS check for these CRITICAL issues:

## 🚨 MANDATORY VECTORIZATION 🚨
**FAIL any code that uses if-elif-else in formula methods**

### Examples of FAILURES:
```python
# ❌ FAIL - Not vectorized
def formula(household, period, parameters):
    if wages > threshold:
        tax = wages * rate_high
    else:
        tax = wages * rate_low
    return tax
```

### Required patterns:
```python
# ✅ PASS - Properly vectorized
def formula(household, period, parameters):
    return where(wages > threshold, wages * rate_high, wages * rate_low)

# ✅ BETTER - Select rate first
def formula(household, period, parameters):
    rate = where(wages > threshold, rate_high, rate_low)
    return wages * rate

# ✅ BEST - For simple conditions
def formula(household, period, parameters):
    return (wages > threshold) * wages * rate_high
```

## Other Critical Checks:
1. Statutory references (Acts > Regulations > Websites)
2. Thousands separators with underscores (1_000_000)
3. Use select() with default parameter for performance
4. Tests use correct period format (2024: value)

## Auto-fail conditions:
- Any if/elif/else in formula methods
- No statutory references
- Creating duplicate files (_v2, _new, etc.)