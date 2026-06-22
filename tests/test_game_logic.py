from logic_utils import check_guess, get_range_for_difficulty, update_score


def test_check_guess_returns_too_high_when_guess_above_secret():
    result, message = check_guess(60, 50)
    assert result == "Too High"


def test_check_guess_returns_too_low_when_guess_below_secret():
    result, message = check_guess(40, 50)
    assert result == "Too Low"


def test_check_guess_returns_correct_when_guess_matches_secret():
    result, message = check_guess(50, 50)
    assert result == "Win"


def test_easy_difficulty_range():
    assert get_range_for_difficulty("Easy") == (1, 10)


def test_normal_difficulty_range():
    assert get_range_for_difficulty("Normal") == (1, 50)


def test_hard_difficulty_range():
    assert get_range_for_difficulty("Hard") == (1, 100)

def test_wrong_guess_does_not_change_score():
    assert update_score(0, "Too High", 1) == 0
    assert update_score(0, "Too Low", 2) == 0


def test_win_adds_positive_score():
    assert update_score(0, "Win", 1) == 100

    