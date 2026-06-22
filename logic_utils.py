def get_range_for_difficulty(difficulty):
    difficulty = difficulty.lower()

    if difficulty == "easy":
        return (1, 10)
    elif difficulty == "normal":
        return (1, 50)
    elif difficulty in ["hard", "difficult"]:
        return (1, 100)

    return (1, 100)

def parse_guess(raw: str):
    """Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except ValueError:
        return False, None, "That is not a number."

    return True, value, None


def _normalize_secret(secret):
    if isinstance(secret, str):
        secret_value = secret.strip()
        try:
            return int(secret_value)
        except ValueError:
            try:
                return int(float(secret_value))
            except ValueError:
                return secret
    return secret


def check_guess(guess, secret_number):
    # FIX: Refactored logic into logic_utils.py using AI assistant, then verified high/low behavior with pytest.
    if guess > secret_number:
        return "Too High", "📉 Go LOWER!"
    elif guess < secret_number:
        return "Too Low", "📈 Go HIGHER!"
    return "Win", "🎉 Correct!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score so it only increases and never goes negative."""
    # FIX: Scoring was refactored with AI assistance so wrong guesses do not add or subtract points.
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)

        if points < 10:
            points = 10

        return current_score + points

    return current_score
