import random
import streamlit as st

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
    validate_guess_in_range,
)

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.markdown(
    """
    <style>
    .stApp {
        background:
            linear-gradient(rgba(8, 8, 14, 0.92), rgba(8, 8, 14, 0.92)),
            repeating-linear-gradient(
                90deg,
                #111 0px,
                #111 24px,
                #ff004c 24px,
                #ff004c 28px,
                #00f5ff 28px,
                #00f5ff 32px,
                #111 32px,
                #111 70px
            );
        color: #f8f8ff;
    }

    .block-container {
        background-color: rgba(15, 15, 24, 0.92);
        border: 1px solid #2f2f46;
        border-radius: 18px;
        padding: 2rem;
        box-shadow: 0 0 25px rgba(0, 245, 255, 0.18);
    }

    section[data-testid="stSidebar"] {
        background-color: #090911;
        border-right: 2px solid #00f5ff;
    }

    section[data-testid="stSidebar"] * {
        color: #f8f8ff !important;
    }

    h1, h2, h3 {
        color: #ffffff !important;
        text-shadow: 2px 2px 0px #ff004c, -2px -2px 0px #00f5ff;
        letter-spacing: 1px;
    }

    p, span, label, div {
        color: #f8f8ff;
    }

    .stCaptionContainer, [data-testid="stCaptionContainer"] {
        color: #c9c9d8 !important;
    }

    div[data-testid="stAlert"] {
        border-radius: 12px;
        border: 1px solid #00f5ff;
        background-color: rgba(25, 25, 40, 0.95);
        color: #ffffff;
    }

    .stTextInput input {
        background-color: #10101c;
        color: #ffffff;
        border: 2px solid #00f5ff;
        border-radius: 10px;
    }

    .stTextInput input:focus {
        border: 2px solid #ff004c;
        box-shadow: 0 0 10px rgba(255, 0, 76, 0.6);
    }

    .stButton > button,
    .stFormSubmitButton > button {
        background-color: #111122;
        color: #ffffff;
        border: 2px solid #00f5ff;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-weight: 700;
        box-shadow: 3px 3px 0px #ff004c;
    }

    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        background-color: #ff004c;
        color: #ffffff;
        border: 2px solid #ffffff;
        box-shadow: 3px 3px 0px #00f5ff;
    }

    .stCheckbox label {
        color: #ffffff !important;
    }

    [data-testid="stExpander"] {
        background-color: rgba(20, 20, 32, 0.95);
        border: 1px solid #444466;
        border-radius: 12px;
    }

    hr {
        border-color: #00f5ff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}

attempt_limit = attempt_limit_map[difficulty]
low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

# FIXME: Original new game flow did not fully reset score, attempts, history, status, and secret number.
def reset_game():
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.active_difficulty = difficulty


if "active_difficulty" not in st.session_state:
    reset_game()

if st.session_state.active_difficulty != difficulty:
    reset_game()
    st.rerun()

if "secret" not in st.session_state:
    reset_game()

st.subheader("Make a guess")

st.info(
    f"Guess a whole number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

show_hint = st.checkbox("Show hint", value=True)

with st.form("guess_form", clear_on_submit=False):
    raw_guess = st.text_input(
        "Enter your guess:",
        key=f"guess_input_{difficulty}",
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        submit = st.form_submit_button("Submit Guess 🚀")

    with col2:
        new_game = st.form_submit_button("New Game 🔁")

if new_game:
    # FIX: New game now clears score, attempts, history, status, and regenerates the secret using the selected difficulty range.
    reset_game()
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

# FIXME: Original submit flow counted invalid guesses as attempts and checked hints before validating range.
if submit:
    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.error(err)
    else:
        in_range, range_error = validate_guess_in_range(guess_int, low, high)

        if not in_range:
            st.error(range_error)
        else:
            st.session_state.attempts += 1
            st.session_state.history.append(guess_int)

            outcome, message = check_guess(guess_int, st.session_state.secret)

            if show_hint:
                st.warning(message)

            st.session_state.score = update_score(
                current_score=st.session_state.score,
                outcome=outcome,
                attempt_number=st.session_state.attempts,
            )

            if outcome == "Win":
                st.balloons()
                st.session_state.status = "won"
                st.success(
                    f"You won! The secret was {st.session_state.secret}. "
                    f"Final score: {st.session_state.score}"
                )
            elif st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")