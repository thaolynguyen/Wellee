import streamlit as st
from gtts import gTTS
from io import BytesIO
import functions
functions.add_bg_from_url() 


with st.sidebar:
    openai_key = st.text_input(label='Clé API', type = 'password')

st.markdown(f'<h1 style="color:#4b2a59;">{"Mes hypnoses"}</h1>', unsafe_allow_html=True)


tab1, tab2, tab3 = st.tabs(["Par jour", "Par thème", "Favoris"])

with tab1:


    for i in range(5):
        with st.expander("🌞 Jour "+str(i), expanded=False):

            st.caption("Un voyage à la mer ...")

            sound_file = BytesIO()
            tts = gTTS("C'est trop bien la mer !!!", lang='fr')
            tts.write_to_fp(sound_file)
            st.audio(sound_file)
with tab2:
    with st.expander("Anxiété"):
        st.info("Hypnoses sur l'anxiété")
    with st.expander("Famille"):
        st.info("Hypnose famille")













st.markdown(
    '''
    <style>
    .streamlit-expanderHeader {
        background-color: rgba(255,255,255,0.3);
        border-radius: 5px;
        box-shadow: rgb(0 0 0 / 20%) 0px 2px 1px -1px, rgb(0 0 0 / 50%) 0px 1px 1px 0px, rgb(0 0 0 / 12%) 0px 1px 3px 0px;
        box-shadow: rgb(0 0 0 / 20%) 0px 2px 1px -1px, rgb(0 0 0 / 40%) 0px 1px 1px 0px, rgb(0 0 0 / 30%) 0px 1px 3px 0px;

    }
    .streamlit-expanderContent {
        background-color: rgba(255,255,255,0.3);

        color: black; # Expander content color
    }

    [data-testid=stSidebar] {
    background: rgba(204, 204, 255, 0.3);
        
    }
    </style>
    ''',
    unsafe_allow_html=True
)



