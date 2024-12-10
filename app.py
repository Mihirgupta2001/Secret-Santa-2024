import streamlit as st
import random
import json
from cryptography.fernet import Fernet
import base64

# List of team members with birth years
team_members = [
    ("Dhruv", 1990), ("Raghu", 1985), ("Aamir", 1988), ("Abhishek Gupta", 1992),
    ("Abhinav Sharma", 1991), ("Ishant Arora", 1993), ("Arun Jaladi", 1987),
    ("Sankalp", 1989), ("Anupam Kashyap", 1986), ("Deeksha", 1994),
    ("Abhinav Relan", 1990), ("Abhishek Kumar", 1991), ("Akul Jain", 1992),
    ("Arun Saraswat", 1988), ("Bharath Raj", 1989), ("Bilal Khan", 1990),
    ("Gaurav Tiwari", 1991), ("Geerthana Murali", 1993), ("Gopikrishna K", 1987),
    ("Harshi Sharma", 1992), ("Jahnavi Potdar", 1994), ("Joseph Plammoottil", 1986),
    ("Mihir Gupta", 1991), ("Mohit Sharma", 1989), ("Nakul Pradeep", 1990),
    ("Nitesh Gautam", 1988), ("Rahul Raturi", 1992), ("Ritik Chopde", 1993),
    ("Shiva Jain", 1991), ("Shubham Gupta", 1990), ("Shubham Kundu", 1989),
    ("Shubham Sharma", 1992), ("Shweta Tiwari", 1991), ("SWAPNIL SARKAR", 1988)
]

# Function to generate password for each user
def generate_password(name, birth_year):
    return f"{name[:4].lower()}{birth_year}"

# Function to encrypt data with a specific password
def encrypt_data(data, password):
    key = base64.urlsafe_b64encode(password.encode().ljust(32)[:32])
    fernet = Fernet(key)
    return fernet.encrypt(data.encode()).decode()

# Function to decrypt data with a specific password
def decrypt_data(encrypted_data, password):
    key = base64.urlsafe_b64encode(password.encode().ljust(32)[:32])
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data.encode()).decode()

# Generate secret Santa pairings
def generate_pairings():
    random.shuffle(team_members)
    pairings = list(zip(team_members, team_members[1:] + [team_members[0]]))
    encrypted_pairings = {}
    for (gifter, gifter_year), (recipient, _) in pairings:
        password = generate_password(gifter, gifter_year)
        encrypted_recipient = encrypt_data(recipient, password)
        encrypted_pairings[gifter] = encrypted_recipient
    return encrypted_pairings

# Streamlit app
def main():
    st.title("Secret Santa Revealer")

    # Generate pairings if not already done
    if 'pairings' not in st.session_state:
        st.session_state.pairings = generate_pairings()

    # User input
    name = st.text_input("Your Name:")
    birth_year = st.number_input("Your Birth Year:", min_value=1900, max_value=2023, value=1990)

    if st.button("Reveal My Secret Santa Recipient"):
        if name in st.session_state.pairings:
            password = generate_password(name, birth_year)
            try:
                decrypted_recipient = decrypt_data(st.session_state.pairings[name], password)
                st.success(f"Your Secret Santa recipient is: {decrypted_recipient}")
            except:
                st.error("Invalid name or birth year. Please try again.")
        else:
            st.error("Name not found in the participants list.")

if __name__ == "__main__":
    main()
