def is_power_greater_than_5000(base, exponent):
    result = base ** exponent
    return result > 5000  # Return True if result > 5000, else False

# Example usage:
print(is_power_greater_than_5000(5, 5))
print(is_power_greater_than_5000(10, 4))
