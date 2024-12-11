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

# Christmas tree made of tree emojis
def christmas_tree():
    return """
        ⭐
        🎄
       🎄🎄
      🎄🎄🎄
     🎄🎄🎄🎄
    🎄🎄🎄🎄🎄
   🎄🎄🎄🎄🎄🎄
  🎄🎄🎄🎄🎄🎄🎄
 🎄🎄🎄🎄🎄🎄🎄🎄
     🎁🎁🎁
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
        background-color: #f0f0f0;
        color: #1e1e1e;
    }
    .stButton>button {
        color: #ffffff;
        background-color: #146B3A;
        border: 2px solid #BB2528;
        font-weight: bold;
        padding: 0.5em 1em;
        font-size: 18px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #BB2528;
        border-color: #146B3A;
        color: #ffffff;
    }
    .stTextInput>div>div>input {
        color: #1e1e1e;
        background-color: #ffffff;
        border: 2px solid #146B3A;
    }
    .tree {
        font-family: 'Courier New', Courier, monospace;
        white-space: pre;
        line-height: 1;
        font-size: 24px;
        text-align: center;
    }
    .centered {
        text-align: center;
    }
    h1 {
        color: #BB2528;
    }
    .stSuccess {
        background-color: #146B3A;
        color: #ffffff;
    }
    .stWarning {
        background-color: #FFF700;
        color: #1e1e1e;
    }
    .stError {
        background-color: #BB2528;
        color: #ffffff;
    }
    .stSuccess, .stWarning, .stError {
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title with emojis
    st.markdown("<h1 class='centered'>🎄 Secret Santa Revealer 🎅</h1>", unsafe_allow_html=True)

    # Display Christmas tree
    st.markdown(f"<div class='tree'>{christmas_tree()}</div>", unsafe_allow_html=True)

    # Load data
    pairings, alias_to_name = load_data()

    # User input
    user_alias = st.text_input("Enter Your Elf Name (Alias):")

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Reveal My Secret Santa Recipient"):
            if user_alias:
                if user_alias in pairings:
                    recipient_alias = pairings[user_alias]
                    recipient_name = alias_to_name.get(recipient_alias, recipient_alias)
                    st.markdown(f"<div class='stSuccess'>🎁 Ho Ho Ho! Your Secret Santa recipient is: <span style='color: #FFD700; font-size: 1.2em;'>{recipient_name}</span> 🎁</div>", unsafe_allow_html=True)
                    st.balloons()
                else:
                    st.error("Oops! This elf name is not on Santa's list. Try again!")
            else:
                st.warning("Please enter your elf name (alias).")

    # Festive footer
    st.markdown("---")
    st.markdown("<p class='centered' style='color: #BB2528;'>🎄 Merry Christmas and Happy Secret Santa! 🎅</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
