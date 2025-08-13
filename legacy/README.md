# Legacy Files

This directory contains the original standalone scripts that were used before OrpheusDL was converted to a proper Python package.

## Files

- `orpheus.py` - Original standalone script for running OrpheusDL
- `moduletesting.py` - Original module testing script

## Migration Notice

These files are kept for reference only. The functionality has been moved to the proper package structure:

- **Instead of `python orpheus.py`**, use the installed commands:
  - `orpheus` (main command)
  - `orpheusdl` (alternative command)

- **Instead of importing from these files**, use the package imports:
  ```python
  import orpheusdl
  from orpheusdl import Orpheus, beauty_format_seconds
  ```

## Backward Compatibility

If you need to run the legacy script for any reason, you can still do so:

```bash
cd legacy
python orpheus.py --help
```

However, note that the legacy script now imports from the `orpheusdl` package, so the package must be installed for it to work.

## Recommendation

Use the modern package installation and commands instead of these legacy files:

```bash
# Install the package
pip install -e .

# Use the modern commands
orpheus --help
orpheusdl search qobuz track "your search"
```
