import streamlit as st
import json

# Load pairings from JSON file
@st.cache_data
def load_pairings():
    with open("pairings.json", "r") as file:
        return json.load(file)

# Process name input
def process_name(name):
    # Take the word before the first space and convert to lowercase
    return name.split()[0].lower()

# Streamlit app
def main():
    st.title("Secret Santa Revealer 🎅")

    # Load pairings
    pairings = load_pairings()

    # User input
    name_input = st.text_input("Your Name:")
    birth_year = st.number_input(
        "Your Birth Year (for verification):", min_value=1900, max_value=2023, value=1990
    )

    if st.button("Reveal My Secret Santa Recipient"):
        # Process the name input
        processed_name = process_name(name_input)
        
        key = f"{processed_name}_{birth_year}"  # Construct the key using processed name and birth year
        
        # Convert all keys in pairings to lowercase for case-insensitive matching
        pairings_lower = {k.lower(): v for k, v in pairings.items()}
        
        if key in pairings_lower:
            recipient = pairings_lower[key]  # Get the recipient's name
            st.success(f"Your Secret Santa recipient is: {recipient}")
        else:
            st.error("Invalid name or birth year. Please try again.")

if __name__ == "__main__":
    main()
