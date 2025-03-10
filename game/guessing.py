import streamlit as st
import random

# Initialize session state variables
if "target_number" not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

st.title("Number Guessing Game 🎯")

# Optional: Allow users to set a custom range
min_val = st.number_input("Set minimum value", value=1, step=1)
max_val = st.number_input("Set maximum value", value=100, step=1)

if st.button("Set Range"):
    st.session_state.target_number = random.randint(min_val, max_val)
    st.session_state.attempts = 0
    st.success(f"New number set between {min_val} and {max_val}")

st.write("Guess the number!")

# User input for guessing
user_guess = st.number_input("Enter your guess:", min_value=min_val, max_value=max_val, step=1)

if st.button("Submit Guess✅"):
    st.session_state.attempts += 1

    if user_guess < st.session_state.target_number:
        st.warning("Too low! Try again.❌")
    elif user_guess > st.session_state.target_number:
        st.warning("Too high! Try again.❌")
    else:
        st.success(f"Congratulations!🎉 You guessed the number in {st.session_state.attempts} attempts.")
        st.session_state.target_number = random.randint(min_val, max_val)
        st.session_state.attempts = 0

st.write(f"Attempts: {st.session_state.attempts}")

# Reset game
if st.button("Reset Game"):
    st.session_state.target_number = random.randint(min_val, max_val)
    st.session_state.attempts = 0
    st.success("Game reset! Try again.❌")
