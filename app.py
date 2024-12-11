import streamlit as st
import json

# Load pairings and create a reverse lookup dictionary
def load_data():
    with open('pairings.json', 'r') as f:
        pairings = json.load(f)
    
    with open('team_members.json', 'r') as f:
        team_members = json.load(f)
    
    alias_to_name = {alias: name for name, alias in team_members}
    return pairings, alias_to_name

# Christmas tree ASCII art
def christmas_tree():
    return """
        *
       ***
      *****
     *******
    *********
   ***********
  *************
 ***************
*****************
       |||
       |||
    """

# Streamlit app
def main():
    # Set page config for a festive look
    st.set_page_config(
        page_title="Secret Santa Revealer",
        page_icon="🎅",
        layout="centered"
    )

    # Custom CSS for Christmas colors
    st.markdown("""
    <style>
    .stApp {
        background-color: #0C5E1C;
        color: #FFFFFF;
    }
    .stButton>button {
        color: #0C5E1C;
        background-color: #D42426;
        border: 2px solid #FFFFFF;
    }
    .stTextInput>div>div>input {
        color: #0C5E1C;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title with emojis
    st.title("🎄 Secret Santa Revealer 🎅")

    # Display ASCII Christmas tree
    st.text(christmas_tree())

    # Load data
    pairings, alias_to_name = load_data()

    # User input
    user_alias = st.text_input("Enter Your Elf Name (Alias):")

    if st.button("Reveal My Secret Santa Recipient"):
        if user_alias:
            if user_alias in pairings:
                recipient_alias = pairings[user_alias]
                recipient_name = alias_to_name.get(recipient_alias, recipient_alias)
                st.success(f"🎁 Ho Ho Ho! Your Secret Santa recipient is: {recipient_name} 🎁")
                st.balloons()
            else:
                st.error("Oops! This elf name is not on Santa's list. Try again!")
        else:
            st.error("Please enter your elf name (alias).")

    # Festive footer
    st.markdown("---")
    st.markdown("🎄 Merry Christmas and Happy Secret Santa! 🎅")

if __name__ == "__main__":
    main()
