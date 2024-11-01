from operator import ge
import streamlit as st
import pyperclip
from mnemonic import Mnemonic
from bip44 import Wallet

from frontend.st_utils import initialize_st_page

# Initialize the Streamlit page
initialize_st_page(title="Seed Generator", icon="🌱", initial_sidebar_state="expanded")

st.text(
    'This tool generates Seed Phrases and Private Keys for cryptocurrency wallets. Press "Generate" to generate the Seed Phrase and Private Key.'
)


def secret_input(state_key, label, text_input_type="password"):
    if state_key not in st.session_state:
        st.session_state[state_key] = ""

    text_input = st.text_input(
        label, type=text_input_type, value=st.session_state[state_key], key=state_key
    )

    if st.button(f"Copy {label}", key=f"copy_{state_key}"):
        pyperclip.copy(text_input)


def generate_seed_and_key(coin: str = "eth"):
    # Create a BIP39 seed phrase
    mnemo = Mnemonic("english")
    seed_phrase = mnemo.generate(strength=128)  # 128 bits generates 12 words

    # Use BIP44 to generate a private key from the seed phrase
    wallet = Wallet(seed_phrase)
    [private_key, public_key] = wallet.derive_account(coin=coin, account=0)

    # Update session state
    st.session_state["seed_phrase"] = seed_phrase
    st.session_state["private_key"] = private_key
    st.session_state["public_key"] = public_key


if st.button("Generate"):
    generate_seed_and_key()

secret_input("seed_phrase", "Seed Phrase")
secret_input("private_key", "Private Key")
secret_input("public_key", "Public Key", text_input_type="text")
