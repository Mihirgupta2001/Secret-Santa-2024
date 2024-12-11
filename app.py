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
        🌟
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
        background-color: #2c5a7c;
        color: #FFFFFF;
    }
    .stButton>button {
        color: #FFFFFF;
        background-color: #c41e3a;
        border: 2px solid #00a86b;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        color: #2c5a7c;
        background-color: #f0f0f0;
    }
    .tree {
        font-family: monospace;
        white-space: pre;
        line-height: 1;
        color: #00a86b;
    }
    .centered {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title with emojis
    st.markdown("<h1 class='centered'>🎄 Secret Santa Revealer 🎅</h1>", unsafe_allow_html=True)

    # Display ASCII Christmas tree
    st.markdown(f"<pre class='tree centered'>{christmas_tree()}</pre>", unsafe_allow_html=True)

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
                    st.success(f"🎁 Ho Ho Ho! Your Secret Santa recipient is: {recipient_name} 🎁")
                    st.balloons()
                else:
                    st.error("Oops! This elf name is not on Santa's list. Try again!")
            else:
                st.warning("Please enter your elf name (alias).")

    # Festive footer
    st.markdown("---")
    st.markdown("<p class='centered'>🎄 Merry Christmas and Happy Secret Santa! 🎅</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
