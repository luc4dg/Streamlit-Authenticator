# Streamlit-LDAP-Authenticator 
**This version enables the possibility to use LDAP authentication for an application that is deployed within your organization's network**


## Example

Using Streamlit-Authenticator is as simple as importing the module and calling it to verify your predefined users' credentials.

```python
import streamlit_authenticator.authenticate as stauth
```

### 1. Set up the LDAP server parameters for authentication

Set the ldapauth variable to true and configure the parameters for the connection.

```python
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
```

### 2. Creating a login widget

* create an authentication object.
```python
name, authentication_status, username = authenticator.login('Login', 'main')
st.write(authentication_status)
```
## Credits
- Luca Del Giudice 
