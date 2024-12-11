import streamlit as st
import json
from cryptography.fernet import Fernet
import base64

# Function to generate password for each user
def generate_password(name, birth_year):
    return f"{name[:4].lower()}{birth_year}"

# Function to decrypt data with a specific password
def decrypt_data(encrypted_data, password):
    key = base64.urlsafe_b64encode(password.encode().ljust(32)[:32])
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data.encode()).decode()

# Streamlit app
def main():
    st.title("Secret Santa Revealer")

    # Load encrypted pairings
    with open('encrypted_pairings.json', 'r') as f:
        encrypted_pairings = json.load(f)

    # User input
    name = st.text_input("Your Name:")
    birth_year = st.number_input("Your Birth Year:", min_value=1900, max_value=2023, value=1990)

    if st.button("Reveal My Secret Santa Recipient"):
        if name and birth_year:
            password = generate_password(name, birth_year)
            try:
                # Encrypt the input name to find the matching key
                encrypted_name = encrypt_data(name, password)
                for encrypted_gifter, encrypted_recipient in encrypted_pairings.items():
                    if decrypt_data(encrypted_gifter, password) == name:
                        decrypted_recipient = decrypt_data(encrypted_recipient, password)
                        st.success(f"Your Secret Santa recipient is: {decrypted_recipient}")
                        break
                else:
                    st.error("Name not found in the participants list.")
            except:
                st.error("Invalid name or birth year. Please try again.")
        else:
            st.error("Please enter both your name and birth year.")

if __name__ == "__main__":
    main()
