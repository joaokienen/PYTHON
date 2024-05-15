# Import modules
import os
import json
import streamlit as st
from streamlit_lottie import st_lottie

# ---> Function LottieAnime
def LottieAnime():

    current_dir = os.path.dirname(os.path.realpath(__file__))
    lottieanime = os.path.join(current_dir, f'Images/lottieanime.json')

    if os.path.exists(lottieanime):

        @st.cache_data()
        def load_lottiefile(filepath):
            with open(filepath, "r") as f:
                return json.load(f)

        with st.container(border=True):
            st_lottie(load_lottiefile(lottieanime), speed=1, width=300, height=200, key="animation")

    return
# ---> 
