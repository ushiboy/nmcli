# Release Process

This document describes the process for releasing a new version of nmcli.

## Current Release Flow (Phase 1: GitHub Release)

Currently, only GitHub Release automation is implemented. PyPI publishing automation will be added in the future.

## Pre-Release Checklist

- [ ] All tests pass (`python -m pytest tests`)
- [ ] Type checking passes (`python -m mypy nmcli`)
- [ ] Lint checks pass (`python -m pylint nmcli`)
- [ ] README.md Change Log is updated
- [ ] README.md API documentation is up to date
- [ ] README.md Compatibility table is up to date

## Release Steps

### 1. Determine Version Number

Follow semantic versioning:
- **MAJOR**: Incompatible API changes
- **MINOR**: Backwards-compatible functionality additions
- **PATCH**: Backwards-compatible bug fixes

Example: Current `1.6.0` → Next `1.7.0` (for feature additions)

### 2. Update pyproject.toml Version

```toml
[project]
version = "1.7.0"  # ← Update this
```

### 3. Update README.md Change Log

Add the new version's changes to the "Change Log" section in README.md:

```markdown
### 1.7.0

- Added support for `connection.show_all` with active filtering
- Added support for `device.up` and `device.down` commands
- Added support for `general.reload` with configuration flags
```

### 4. Commit Changes

```bash
git add pyproject.toml README.md
git commit -m "Release v1.7.0"
```

### 5. Create and Push Tag

```bash
# Push to main branch
git push origin main

# Create tag
git tag v1.7.0

# Push tag (this triggers GitHub Actions)
git push origin v1.7.0
```

### 6. Verify GitHub Actions Completion

1. Check workflow execution status at https://github.com/ushiboy/nmcli/actions
2. Verify all tests pass
3. Verify build succeeds

### 7. Edit and Publish Draft Release

1. Go to https://github.com/ushiboy/nmcli/releases
2. Open the auto-created draft release
3. Edit release notes:
   - Review auto-generated content
   - Add main changes as bullet points in the "What's Changed" section
   - Clean up commit history if needed
4. Click "Publish release" to publish

### 8. Manual PyPI Publishing (Current)

PyPI publishing is currently done manually:

```bash
# Build (requires Python 3.10+)
python -m build

# Upload to PyPI
twine upload dist/nmcli-1.7.0*
```

## Troubleshooting

### Tag and Version Mismatch Error

```
Error: Package version (1.6.0) does not match tag version (1.7.0)
```

**Cause**: Forgot to update version in pyproject.toml

**Solution**:
1. Delete tag: `git tag -d v1.7.0 && git push origin :v1.7.0`
2. Fix pyproject.toml and commit
3. Create and push tag again

### Test Failures

**Solution**:
1. Delete tag (see above)
2. Fix tests and commit
3. Create and push tag again

### Build Failures

Recommended to verify locally before tagging:

```bash
# Clean build verification
rm -rf dist/
python -m build

# Check generated files
ls -lh dist/
```

## Future Extension (Phase 2: PyPI Auto-Publishing)

The following will be added in the future:

1. **PyPI Trusted Publishers Setup**
   - Register GitHub repository as a trusted publisher on PyPI
   - No token management needed, more secure

2. **Workflow Extension**
   - Automatically publish to PyPI after GitHub Release
   - Or make PyPI publishing optional at draft stage

3. **TestPyPI Validation**
   - Validate on TestPyPI before production release

## Release Checklist

Before releasing, verify:

- [ ] Updated pyproject.toml version
- [ ] Updated README.md Change Log
- [ ] All tests pass locally
- [ ] Committed changes
- [ ] Pushed to main
- [ ] Created and pushed tag
- [ ] Verified GitHub Actions completion
- [ ] Edited draft release
- [ ] Published release
- [ ] (Current) Manually uploaded to PyPI
