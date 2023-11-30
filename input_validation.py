def validate_numeric_input(value):
    """Validate that the input is numeric."""
    try:
        float(value)
        return True
    except ValueError:
        return False