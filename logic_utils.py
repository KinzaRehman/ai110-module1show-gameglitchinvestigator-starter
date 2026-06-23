def get_range_for_difficulty(difficulty):
    difficulty = difficulty.lower()

    if difficulty == "easy":
        return (1, 10)
    elif difficulty == "normal":
        return (1, 50)
    elif difficulty in ["hard", "difficult"]:
        return (1, 100)

    return (1, 100)

#FIXME: Original input handling accepted/converted decimals instead of clearly rejecting non-whole-number guesses.
def parse_guess(raw):

    """Parse user input into a whole number guess."""
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    raw = raw.strip()

    if "." in raw:
        return False, None, "Please enter a whole number, not a decimal."

    try:
        value = int(raw)
    except ValueError:
        return False, None, "That is not a number."

    return True, value, None

# FIXME: Original game allowed out-of-range guesses like 101 instead of rejecting them before checking hints.
def validate_guess_in_range(guess, low, high):
    """Check whether a guess is inside the current difficulty range."""
    if guess < low or guess > high:
        return False, f"Your guess must be between {low} and {high}."
    return True, None


def check_guess(guess, secret_number):
    # FIXME: Refactored logic into logic_utils.py using AI assistance and verified with pytest.
    if guess > secret_number:
        return "Too High", "📉 Go LOWER!"
    elif guess < secret_number:
        return "Too Low", "📈 Go HIGHER!"
    return "Win", "🎉 Correct!"


def update_score(current_score, outcome, attempt_number):
    """Score only increases when the player wins."""
    # FIXME: Scoring now stays positive and only rewards correct guesses.
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)

        if points < 10:
            points = 10

        return current_score + points

    return current_score