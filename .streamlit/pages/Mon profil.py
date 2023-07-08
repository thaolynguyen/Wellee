import streamlit as st
import functions


functions.add_bg_from_url() 



st.markdown("""
<style>
    [data-testid=stSidebar] {
        background: rgba(204, 204, 255, 0.3);
        
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    openai_key = st.text_input(label='Clé API', type = 'password')


st.markdown(f'<h1 style="color:#4b2a59;">{"Thao-Ly Nguyen"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h2 style="color:#4b2a59;">{"Mes préférences"}</h2>', unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)




with st.container():


    voix = st.selectbox(
    'Type de voix pour la lecture du script',
    ('Féminine', 'Masculine'))


    Musique = st.selectbox(
    'Musique en fond',
    ('Oui', 'Non'))



    paysage = st.multiselect(
    'Choisis un ou plusieurs paysage que tu aimes',
    ['🏖️ La plage', '⛰️ La montagne', '🐅 La jungle', '🍄 Prarie','🌠 L\'univers', '🌿 Le jardin de mamie'],
    ['🏖️ La plage',]
    )




st.markdown(
    """
<style>
    div[data-testid="stExpander"] div[style*="flex-direction: column;"] div[data-testid="stVerticalBlock"] {
    box-shadow: rgb(0 0 0 / 20%) 0px 2px 1px -1px, rgb(0 0 0 / 50%) 0px 1px 1px 0px, rgb(0 0 0 / 12%) 0px 1px 3px 0px;
    padding: 5% 5% 5% 10%;    
    box-shadow: rgb(0 0 0 / 20%) 0px 2px 1px -1px, rgb(0 0 0 / 40%) 0px 1px 1px 0px, rgb(0 0 0 / 30%) 0px 1px 3px 0px;
    background-color:rgba(255,255,255,0);
    padding: 5% 5% 5% 10%;
    }

    
</style>
""",
    unsafe_allow_html=True,
)
