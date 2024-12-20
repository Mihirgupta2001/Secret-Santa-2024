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

# Christmas tree ASCII art (centered)
def christmas_tree():
    return """
           🌟
           🎄
          🎄🎄
         🎄🎄🎄
        🎄🎄🎄🎄
       🎄🎄🎄🎄🎄
      🎄🎄🎄🎄🎄🎄
     🎄🎄🎄🎄🎄🎄🎄
    🎄🎄🎄🎄🎄🎄🎄🎄
   🎄🎄🎄🎄🎄🎄🎄🎄🎄
        🎁🎁🎁🎁
    """

# Streamlit app
def main():
    # Set page config for a festive look
    st.set_page_config(
        page_title="Secret Santa Revealer",
        page_icon="🎅",
        layout="centered"
    )

    # Custom CSS for Christmas colors, centered tree, and light success message
    st.markdown("""
    <style>
    .stApp {
        background-color: #1e3f41;
        color: #FFFFFF;
    }
    .stButton>button {
        color: #FFFFFF;
        background-color: #c41e3a;
        border: 2px solid #00a86b;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        color: #1e3f41;
        background-color: #f0f0f0;
    }
    .stTextInput>label {
        color: #b3ffb3 !important;
    }
    .tree {
        font-family: monospace;
        white-space: pre;
        display: flex;
        justify-content: center;
        color: #00a86b;
    }
    .light-success {
        color: #b3ffb3 !important;
        background-color: rgba(0, 255, 0, 0.1) !important;
        border-color: #66ff66 !important;
        padding: 0.5rem;
        border-radius: 0.25rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title with emojis
    st.title("🎄 Secret Santa Revealer 🎅")

    # Display ASCII Christmas tree
    st.markdown(f'<div class="tree">{christmas_tree()}</div>', unsafe_allow_html=True)

    # Load data
    pairings, alias_to_name = load_data()

    # User input
    user_alias = st.text_input("Enter Your Elf Name (Alias):")
    user_alias = user_alias.lower()

    if st.button("Reveal My Secret Santa Recipient"):
        if user_alias:
            if user_alias in pairings:
                recipient_alias = pairings[user_alias]
                recipient_name = alias_to_name.get(recipient_alias, recipient_alias)
                st.markdown(f'<div class="light-success">🎁 Ho Ho Ho! Your Secret Santa recipient is: {recipient_name} 🎁</div>', unsafe_allow_html=True)
                st.balloons()
            else:
                st.error("Oops! This elf name is not on Santa's list. Try again!")
        else:
            st.warning("Please enter your elf name (alias).")

    # Festive footer
    st.markdown("---")
    st.markdown("🎄 Merry Christmas and Happy Secret Santa! 🎅")

if __name__ == "__main__":
    main()
