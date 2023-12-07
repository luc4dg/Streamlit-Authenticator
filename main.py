import yaml
from yaml.loader import SafeLoader
import streamlit as st
import streamlit_authenticator.authenticate as stauth


with open('./config.yaml',encoding='utf-8') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized'],
    ldapauth=True,
    domain_name="",
    server="",
    port="",
)

name, authentication_status, username = authenticator.login('Login', 'main')


st.write(authentication_status)

