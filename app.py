import streamlit as st
import json

# Load pairings from JSON file
@st.cache_data
def load_pairings():
    with open("pairings.json", "r") as file:
        return json.load(file)

# Streamlit app
def main():
    st.title("Secret Santa Revealer 🎅")

    # Load pairings
    pairings = load_pairings()

    # User input
    name = st.text_input("Your Name:")
    birth_year = st.number_input(
        "Your Birth Year (for verification):", min_value=1900, max_value=2023, value=1990
    )

    if st.button("Reveal My Secret Santa Recipient"):
        key = f"{name}_{birth_year}"  # Construct the key using name and birth year
        if key in pairings:
            recipient = pairings[key]  # Get the recipient's name
            st.success(f"Your Secret Santa recipient is: {recipient}")
        else:
            st.error("Invalid name or birth year. Please try again.")

if __name__ == "__main__":
    main()
