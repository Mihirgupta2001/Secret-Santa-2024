import streamlit as st
import json

# Load pairings and create a reverse lookup dictionary
def load_data():
    with open('pairings.json', 'r') as f:
        pairings = json.load(f)
    
    # Create a dictionary to map aliases to names
    with open('team_members.json', 'r') as f:
        team_members = json.load(f)
    
    alias_to_name = {alias: name for name, alias in team_members}
    return pairings, alias_to_name

# Streamlit app
def main():
    st.title("Secret Santa Revealer")

    # Load data
    pairings, alias_to_name = load_data()

    # User input
    user_alias = st.text_input("Your Alias:")

    if st.button("Reveal My Secret Santa Recipient"):
        if user_alias:
            if user_alias in pairings:
                recipient_alias = pairings[user_alias]
                recipient_name = alias_to_name.get(recipient_alias, recipient_alias)
                st.success(f"Your Secret Santa recipient is: {recipient_name}")
            else:
                st.error("Alias not found in the participants list.")
        else:
            st.error("Please enter your alias.")

if __name__ == "__main__":
    main()
