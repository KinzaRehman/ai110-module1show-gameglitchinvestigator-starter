# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.
### What task did you give the agent?

I asked the AI assistant to refactor the game logic by moving functions from `app.py` into `logic_utils.py`, fix the reversed hint bug, correct the difficulty ranges, improve the scoring logic, and update imports so the Streamlit application continued working correctly.

### What did the agent do?

* Moved game logic functions from `app.py` to `logic_utils.py`
* Updated imports in `app.py`
* Suggested fixes for the `check_guess()` function
* Suggested fixes for difficulty ranges
* Generated pytest tests for game behavior
* Helped identify scoring inconsistencies
* Suggested validation for out-of-range and decimal guesses

### What did you have to verify or fix manually?

I reviewed every file change before accepting it. One AI suggestion incorrectly assumed all scoring issues came from the `update_score()` function, but additional testing showed Streamlit session state also affected game behavior. I manually verified the final behavior by running pytest and testing the application in Streamlit.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

## Test Generation (SF7)

| Edge Case          | Prompt Used                                          | AI-Suggested Test                                                    | Did It Pass? | Your Reasoning                                              |
| ------------------ | ---------------------------------------------------- | -------------------------------------------------------------------- | ------------ | ----------------------------------------------------------- |
| Guess above secret | "Create a pytest test for the high hint bug."        | Assert that a guess of 60 against a secret of 50 returns "Too High". | Yes          | Verified that the corrected logic returned the proper hint. |
| Guess below secret | "Create a pytest test for low guess behavior."       | Assert that a guess of 40 against a secret of 50 returns "Too Low".  | Yes          | Confirmed the hint logic was no longer reversed.            |
| Correct guess      | "Create a test for winning the game."                | Assert that a matching guess returns a win outcome.                  | Yes          | Verified successful game completion behavior.               |
| Difficulty ranges  | "Generate tests for Easy, Normal, and Hard ranges."  | Tested Easy (1–10), Normal (1–50), and Hard (1–100).                 | Yes          | Confirmed each difficulty level uses the expected range.    |
| Decimal input      | "Generate a test for decimal guesses."               | Assert that decimal guesses are rejected with an error message.      | Yes          | Improved input validation and user feedback.                |
| Out-of-range input | "Generate a test for guesses above the valid range." | Assert that 101 is rejected when the range is 1–100.                 | Yes          | Prevented inconsistent hint behavior for invalid guesses.   |


---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**
### Prompt used:

```text
Review app.py and logic_utils.py for readability, style issues, duplicate logic, unused code, and Python best practices. Suggest improvements that make the code easier to understand without changing functionality.
```

### Linting output before:

```text
No formal linter was used, but manual review identified:
- Logic and UI code mixed together in app.py
- Inconsistent comments
- Difficulty ranges stored in multiple locations
- Some functions were too large and difficult to test
```

### Changes applied:

* Refactored game logic from app.py into logic_utils.py.
* Added helper functions for difficulty ranges, input parsing, range validation, and scoring.
* Improved comments and added FIXME annotations documenting discovered bugs.
* Simplified scoring logic so incorrect guesses no longer modify the score.
* Improved readability by separating game logic from Streamlit UI code.

These changes made the code easier to maintain, test, and debug.
---

## Model Comparison (SF11)

> Compare two AI models on the same task.

## Model Comparison (SF11)

### Task given to both models:

Review the guessing game code, identify bugs, suggest fixes, and explain the reasoning behind the changes.

|                            | Model A                                                                                                                                                     | Model B                                                                                                       |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Model name**             | ChatGPT                                                                                                                                                     | DeepSeek                                                                                                      |
| **Response summary**       | Suggested refactoring logic into logic_utils.py, generated pytest tests, explained Streamlit session state, and helped debug scoring and difficulty issues. | Focused on analyzing the existing code and explaining why the hint logic and scoring behavior were incorrect. |
| **More Pythonic?**         | Yes                                                                                                                                                         | Somewhat                                                                                                      |
| **Clearer explanation?**   | Yes                                                                                                                                                         | Yes, especially for code analysis                                                                             |
| **Better debugging help?** | Yes                                                                                                                                                         | Good for identifying logic issues                                                                             |

### Which did you prefer and why?

I preferred ChatGPT because it provided more complete end-to-end guidance, it was also the tool that I use in my day to day, including refactoring suggestions, testing strategies, Git commands, and explanations of Streamlit behavior. DeepSeek was useful for reviewing logic and identifying bugs, but ChatGPT was more effective as an overall development assistant throughout the project.
