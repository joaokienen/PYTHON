# Import modules
import os
import time
import streamlit as st
from msal import ConfidentialClientApplication


# ----> Auth variables
from dotenv import load_dotenv
load_dotenv('./.env')

authority = f"https://login.microsoftonline.com/{os.getenv('TENANT_ID')}"
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('SECRET_ID')
redirect_uri = "http://localhost"
scopes = ["User.Read"]
# ---->


# ----> Streamlit initial config
st.set_page_config(
    page_title="Cyber Analytics",
    page_icon="+",
    layout='wide'
)
# ---->

# ----> Function to authenticate Azure AD
def authenticate_with_microsoft():

    # Streamlit feature: progress status
    progress = st.progress(5, text="Requesting..")

    # Define variables of APP
    app = ConfidentialClientApplication(
        client_id,
        authority=authority,
        client_credential=client_secret
    )

    # Get accounts from the cache
    accounts = app.get_accounts()

    # Check if there are accounts in the cache
    if accounts:
        chosen = accounts[0]
        result = app.acquire_token_silent(scopes, account=chosen)
    else:
        # Streamlit feature: progress status
        for percent_complete in range(100):
            time.sleep(0.01)
            progress.progress(percent_complete + 1, text="Requesting..")

        # Variable to redirect    
        auth_url = app.get_authorization_request_url(scopes, redirect_uri=redirect_uri)
        st.caption(f'<a href="{auth_url}" target="_self">Click here to reconnect</a>', unsafe_allow_html=True)

        # Variable to get URL Code
        auth_code = st.experimental_get_query_params().get('code', False)

        # If true: get access user
        if auth_code:
            result = app.acquire_token_by_authorization_code(auth_code, scopes=scopes, redirect_uri=redirect_uri)
        else:
            result = None

    # Streamlit feature: progress finish
    progress.empty()

    return result
# ---->


# ----> Main Streamlit app code
def main():
    with st.sidebar:
        with st.container(border=True):
            st.title("Microsoft Authenticator")

            with st.status("Azure connecting..", expanded=True) as status:
                auth = authenticate_with_microsoft()
                st.session_state.connected_state = "Connected!" if auth != None and 'access_token' in auth else "Not Connected!"
                state = "complete" if st.session_state.connected_state == 'Connected!' else "error"
                expanded = False if st.session_state.connected_state == 'Connected!' else True
                status.update(label=st.session_state.connected_state, state=state, expanded=expanded)
                st.session_state.iA = True if auth != None and 'id_token_claims' in auth else False
                #st.session_state.iN = auth['id_token_claims']['name'] if auth != None and 'id_token_claims' in auth else False
                #st.session_state.iM = auth['id_token_claims']['preferred_username'] if auth != None and 'id_token_claims' in auth else False

    if st.session_state.iA:
        print("Connected Space!")
# ---->
        

# Execution Main()
if __name__ == "__main__":
    main()
#---->
