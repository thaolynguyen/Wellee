import streamlit as st
import pandas as pd
import numpy as np
import datetime

import functions

functions.add_bg_from_url() 
st.markdown(f'<h1 style="color:#4b2a59;">{"Mon suivi"}</h1>', unsafe_allow_html=True)

#st.markdown("# Mon suivi")

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


st.markdown("""
<style>
    [data-testid=stSidebar] {
        background: rgba(204, 204, 255, 0.3);
        
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    openai_key = st.text_input(label='Clé API', type = 'password')




col1, col2, col3 = st.columns(3)
col1.metric("Scéances totales", "15")
col2.metric("Heure de sommeil", "7", "+8%")
col3.metric("Scéance ce mois-ci", "11", "4%")



with st.expander("Sommeil", expanded=True):

    st.info("Tu peux renseigner la durée de ton sommeil chaque jour pour pourvoir suivre l'évolution de celui-ci au cours du temps.")
    
    df = pd.DataFrame({

            'date': ['01/07/2023','02/07/2023', '03/07/2023', '04/07/2023','05/07/2023','06/07/2023','07/07/2023'],
             'Nombre d\heures': [10, 7, 8, 10, 5, 7, 10]
            })

    

    st.line_chart(df.rename(columns={'date':'index'}).set_index('index'))

    if st.button("Ajouter une entrée"):
        # Forms can be declared using the 'with' syntax
        with st.form(key='my_form'):
            d = st.date_input(
             "Entre la date", datetime.date(2019, 7, 6))
            heures = st.slider('Nombre d\'heure de sommeil', 0, 10, 24)
            mood = st.radio(
                    "Ressenti général",
                    ('😩 Mauvais', '😐 Moyen', '😀 Très bien'),
                    horizontal= True)
            text_input = st.text_input(label='Remarques')
            submit_button = st.form_submit_button(label='Submit')
            

with st.expander("Scéances", expanded=True):
    st.info("Garde l'historique de tes scéances d'hypnoses")
    df2 = pd.DataFrame({
            'date': ['01/07/2023','02/07/2023', '03/07/2023', '04/07/2023','05/07/2023','06/07/2023','07/07/2023'],
             'Nombre de scéances': [1,1,3,2,1,0,0]
            })

    

    st.bar_chart(df2.rename(columns={'date':'index'}).set_index('index'))


