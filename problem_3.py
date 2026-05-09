# problem_3.py 

def eject_player_if_invalid(player, name, used_names, celebrity_names):
    """
    Eject a player from the game if they fail to provide a valid celebrity name.
    (Same as before)
    """
    # Check if player wants to skip their turn
    if name.lower() == "skip" or name.lower() == "pass":
        print(f"{player.name} chooses to skip their turn.")
        print(f"No points awarded. Moving to next player.")
        return False
    
    # Check if the name is empty or just spaces
    if not name or name.strip() == "":
        print("No name was entered!")
        print(f"{player.name} is ejected from the game!")
        player.is_active = False
        return True
    
    # Clean up the name
    clean_name = name.strip()
    
    # Check if name has at least first and last name
    name_parts = clean_name.split()
    if len(name_parts) < 2:
        print(f"Invalid name: '{clean_name}' must have at least a first and last name.")
        print(f"{player.name} is ejected from the game!")
        player.is_active = False
        return True
    
    # Check if name exists in the celebrity database
    if clean_name not in celebrity_names:
        print(f"'{clean_name}' is not in our celebrity database.")
        print(f"{player.name} is ejected from the game!")
        player.is_active = False
        return True
    
    # Check if name has already been used
    if clean_name in used_names:
        print(f"'{clean_name}' has already been used in this game!")
        print(f"{player.name} is ejected from the game!")
        player.is_active = False
        return True
    
    # Player is valid and stays in the game
    print(f"Valid name! {player.name} stays in the game.")
    return False


def check_name_validity(name, used_names, celebrity_names):
    """
    Check if a celebrity name is valid without ejecting a player.
    (Same as before)
    """
    # Check if player wants to skip
    if name.lower() == "skip" or name.lower() == "pass":
        return True, "skip"
    
    # Check if the name is empty or just spaces
    if not name or name.strip() == "":
        return False, "No name was entered."
    
    # Clean up the name
    clean_name = name.strip()
    
    # Check if name has at least first and last name
    name_parts = clean_name.split()
    if len(name_parts) < 2:
        return False, "Name must have at least a first and last name."
    
    # Check if name exists in the celebrity database
    if clean_name not in celebrity_names:
        return False, f"'{clean_name}' is not in our celebrity database."
    
    # Check if name has already been used
    if clean_name in used_names:
        return False, f"'{clean_name}' has already been used."
    
    # Name is valid
    return True, ""


def validate_and_process_turn(player, name, used_names, celebrity_names):
    """
    Process a player's turn, validating their name and handling ejection if needed.
    (Same as before)
    """
    # Check if player wants to skip
    if name.lower() == "skip" or name.lower() == "pass":
        print(f"{player.name} skips their turn. No points awarded.")
        return True
    
    # First check if the player should be ejected
    was_ejected = eject_player_if_invalid(player, name, used_names, celebrity_names)
    
    if was_ejected:
        return False
    
    # Name is valid, add to used names and award point
    clean_name = name.strip()
    used_names.add(clean_name)
    player.score = player.score + 1
    
    print(f"Great job {player.name}! '{clean_name}' is a valid celebrity!")
    print(f"{player.name}'s score is now {player.score}")
    
    return True


def find_valid_names(required_letter, used_names, celebrity_names):
    """
    Find all valid unused celebrity names that start with the required letter.
    This is used by the bot to know what names are available.
    
    Args:
        required_letter (str): One alphabetical character.
        used_names (set[str]): Names already used in the game.
        celebrity_names (list[str]): Celebrity names available in the game.
        
    Returns:
        list[str]: A list of valid unused names.
        
    Raises:
        ValueError: If required_letter is not one alphabetical character.
    """
    # Validate the required letter
    if len(required_letter) != 1:
        raise ValueError("required_letter must be one letter.")
    
    if required_letter.isalpha() == False:
        raise ValueError("required_letter must be a letter.")
    
    required_letter = required_letter.lower()
    
    # Build list of valid names
    valid_names = []
    for name in celebrity_names:
        # Check if name has at least two parts
        name_parts = name.split()
        if len(name_parts) < 2:
            continue
        
        # Check if name is not used
        if name in used_names:
            continue
        
        # Check if first name starts with required letter
        first_initial = name_parts[0][0].lower()
        if first_initial == required_letter:
            valid_names.append(name)
    
    return valid_names


