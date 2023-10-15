def check_option(opcija: str) -> bool:
    """
    Check if the option is valid(1  to 5)

    Args: opcija(str): opcija

    Returns:
           bool: True if opcija is valid , False otherwise
    """
    try:
        if int(opcija) < 1 or int(opcija) > 5:
            print("\npogresan izbor\n")
            return False

        else:
            print(f"\nopcija:{opcija}\n")
            return True

    except Exception:
        print("\npogresan izbor\n")


