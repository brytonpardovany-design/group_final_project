from problem_3 import find_valid_names


def choose_valid_bot_name(required_letter, used_names, celebrity_names):
    """
    Choose a valid celebrity name for the bot's turn.

    The bot first finds all valid unused names that start with the required
    letter. If any valid name is a special name, the bot returns the first
    special name it finds. A special name is one where the first letter of
    the first name matches the first letter of the last name. If there are
    no special names, the bot returns the first valid name. If there are no
    valid names, it returns None.

    Primary author: Ephraim Alemayehu

        Args:
        required_letter (str): One alphabetical character.
        used_names (set[str]): Names already used in the game.
        celebrity_names (list[str]): Celebrity names available in the game.
        
    Returns:
        str or None: The chosen bot name, or None if no valid name exists.
        
    Raises:
        ValueError: If required_letter is not one alphabetical character.
    """
    # Find all valid names
    valid_names = find_valid_names(required_letter, used_names, celebrity_names)
    
    # First, look for special names (alliterations)
    for name in valid_names:
        name_parts = name.split()
        first_initial = name_parts[0][0].lower()
        last_initial = name_parts[-1][0].lower()
        
        if first_initial == last_initial:
            return name
    
    # If no special names, return the first valid name
    if len(valid_names) > 0:
        return valid_names[0]
    
    # No valid names found
    return None

