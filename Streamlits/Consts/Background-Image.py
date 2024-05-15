# Import modules
import os
import base64
import streamlit as st


# ---> Function BackgroundImage
def BackgroundImage():

    current_dir = os.path.dirname(os.path.realpath(__file__))
    backgroundfile = os.path.join(current_dir, f'Images/background.png')

    if os.path.exists(backgroundfile):

        @st.cache_data()
        def get_base64_of_bin_file(bin_file):
            with open(bin_file, 'rb') as f:
                data = f.read()
            return base64.b64encode(data).decode()

        bin_str = get_base64_of_bin_file(backgroundfile)
        page_bg_img = '''
            <style>
                .stApp {
                    background-image: url("data:image/png;base64,%s");
                    background-size: cover;
                }
                header.st-emotion-cache-18ni7ap.ezrtsby2, header.st-emotion-cache-1avcm0n.ezrtsby2 {
                    background-color: transparent;
                }
            </style>
        ''' % bin_str
                
        st.markdown(page_bg_img, unsafe_allow_html=True)

    return
# ---> 
