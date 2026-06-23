# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is full of glitches.

Originally:

* The hints were misleading.
* The difficulty ranges were inconsistent.
* Invalid guesses could still affect the game.
* The score could behave unpredictably.
* New game behavior did not always fully reset the game state.

## 🛠️ Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the app:

```bash
python -m streamlit run app.py
```

3. Run tests:

```bash
python -m pytest
```

## 🕵️‍♂️ Your Mission

The goal of this project was to investigate, document, and repair bugs in an AI-generated Streamlit guessing game. I used AI as a coding teammate, but I reviewed each suggestion carefully, tested the code, and made final decisions based on the actual game behavior.

## 📝 Document Your Experience

### Game Purpose

The game is a number guessing game where the user selects a difficulty level and guesses a secret number within the correct range. The app gives high/low hints, tracks attempts, calculates a final score, and allows the user to start a new game.

### Bugs Found

* The high/low hints were reversed.
* The difficulty ranges did not always match the selected difficulty.
* Decimal guesses were not clearly explained to the user.
* Out-of-range guesses, such as 101, were not rejected before hint logic ran.
* Invalid guesses could affect attempts.
* The score could become negative or change unpredictably.
* Starting a new game did not always fully reset score, attempts, history, status, and secret number.

### Fixes Applied

* Refactored core logic from `app.py` into `logic_utils.py`.
* Added `get_range_for_difficulty()` to manage Easy, Normal, and Hard ranges.
* Fixed `check_guess()` so high and low hints are correct.
* Added `parse_guess()` to reject decimals with a clear message.
* Added range validation so guesses outside the difficulty range are rejected.
* Updated scoring so points are only awarded when the user wins.
* Updated new game behavior so game state resets correctly.
* Added pytest tests for hints, difficulty ranges, decimal input, out-of-range guesses, and scoring.

## 📸 Demo Walkthrough

1. The user opens the Streamlit app.
2. The user selects a difficulty level: Easy, Normal, or Hard.
3. The game displays the correct range for the selected difficulty.
4. The user enters a decimal guess, such as `50.5`.
5. The game rejects the input and explains that only whole numbers are accepted.
6. The user enters an out-of-range guess, such as `101`.
7. The game rejects the guess and does not count it as an attempt.
8. The user enters a guess below the secret number.
9. The game returns “Too Low” and displays the hint “Go HIGHER!”
10. The user enters a guess above the secret number.
11. The game returns “Too High” and displays the hint “Go LOWER!”
12. The user enters the correct secret number.
13. The game displays a win message and awards a positive final score.
14. The user clicks “New Game.”
15. The app resets the score, attempts, history, status, and secret number.

## 🧪 Test Results

```text
============================= test session starts =============================
platform win32 -- Python 3.13.14, pytest-9.0.3, pluggy-1.6.0
collected 10 items

tests/test_game_logic.py ..........                                      [100%]

============================== 10 passed in 0.09s =============================
```

## 🚀 Stretch Features

* [x] Added extra edge-case tests for decimal input, out-of-range guesses, and scoring behavior.
* [x] Documented AI-assisted test generation in `ai_interactions.md`.
* [x] Compared AI model support in `ai_interactions.md`.
* [x] Documented style and readability improvements in `ai_interactions.md`.
