import random

def validate_input(user_input):
    # Won't let -1 or floating point numbers pass
    if not user_input.isnumeric():
        return None
    
    number = int(user_input)

    if number < 1:
        return None
    
    return number

def generate_mystery_number(user_input):
    
    # We received None
    valid_input = validate_input(user_input)

    if not valid_input:
        # Bad data...bad...
        return None
    
    # Return our random mystery number
    return random.randint(1, int(valid_input))


def process_player_guess(player_guess, mystery_number):
    guess = validate_input(player_guess)
    
    if not guess:
        # Bad data...bad...
        return None

    # True or False won't be able to also tell me if
    #   the value is higher or lower. We'll instead
    #   return a symbol to help us:
    #   * "+" will be our guess is larger than the mystery number
    #   * "-" will be our guess is less than the mystery number
    #   * "=" will be our guess is the correct number
    if guess > mystery_number:
        return '+'
    elif guess < mystery_number:
        return '-'
    else:
        return '='
