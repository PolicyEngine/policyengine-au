# PolicyEngine Vectorization Checker

## Overview

This directory now includes automated checking for PolicyEngine's CRITICAL vectorization requirements. The checker automatically detects if-elif-else statements in formula methods, which violate PolicyEngine's mandatory performance requirements.

## Files Added/Updated

### 1. **REVIEWER_CHECKLIST.md** (Updated)
- Enhanced with prominent 🚨 CRITICAL REQUIREMENT #1 section
- Clear AUTO-FAIL examples and REQUIRED patterns 
- Mandatory review process order
- Specific examples of vectorized vs non-vectorized code

### 2. **check_vectorization.py** (New)
- Automated AST-based checker for vectorization violations
- Detects if-elif-else statements in formula methods
- Provides specific line numbers and fix suggestions
- Returns appropriate exit codes for CI integration

### 3. **Makefile** (Updated)
- Added `make check-vectorization` target
- Uses `uv run python` for consistency with project patterns

### 4. **GitHub Actions** (Updated)
- Added vectorization check to PR workflow (`pr.yaml`)
- Runs automatically on all pull requests
- Fails CI if critical violations are found

## Usage

### Manual Checking
```bash
# Check all variables
make check-vectorization

# Check specific file
uv run python check_vectorization.py path/to/file.py

# Check specific directory  
uv run python check_vectorization.py policyengine_au/variables/gov/ato
```

### Automated CI Checking
- Runs automatically on all PRs via GitHub Actions
- Fails CI if any critical vectorization violations found
- Allows warnings but blocks critical violations

## Violation Types

### CRITICAL (Auto-fail)
- `if-elif` statements in formula methods → Use `select()` with `default`
- `if-else` statements in formula methods → Use `where()` or boolean multiplication

### WARNING (Discouraged)
- Simple `if` statements without else → Consider vectorization

## Example Fixes

### Before (CRITICAL - Auto-fail)
```python
def formula(person, period, parameters):
    if income <= 10_000:
        rate = low_rate
    elif income <= 100_000:  
        rate = medium_rate
    else:
        rate = high_rate
    return income * rate
```

### After (REQUIRED - Pass)
```python  
def formula(person, period, parameters):
    rate = select(
        [income <= 10_000, income <= 100_000],
        [low_rate, medium_rate], 
        default=high_rate  # MUST use default
    )
    return income * rate
```

## Integration with Development Workflow

1. **Before Committing**: Run `make check-vectorization`
2. **During PR Review**: Automated check runs in CI
3. **CI Failure**: Fix violations before merge is allowed
4. **Manual Review**: Use REVIEWER_CHECKLIST.md for comprehensive review

## Exit Codes

- `0`: All files pass vectorization requirements
- `1`: Critical violations found (blocks CI)

## Current Status

The checker has detected existing violations in the codebase:
- 3 critical violations (auto-fail in CI)
- 4 warning violations (should be improved)

These existing violations will need to be fixed to enable the automated checking in CI.

## Benefits

1. **Automated Detection**: No more manual checking for vectorization violations
2. **Consistent Standards**: Enforces PolicyEngine performance requirements automatically  
3. **Clear Guidance**: Provides specific examples of how to fix violations
4. **CI Integration**: Prevents non-vectorized code from being merged
5. **Developer Education**: Teaches proper vectorization patterns through examples

This implementation ensures that the CRITICAL vectorization requirement is ALWAYS checked and any violations result in immediate review failure with clear guidance on how to fix them.