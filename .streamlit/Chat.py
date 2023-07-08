import openai
import streamlit as st
from streamlit_chat import message
from streamlit_option_menu import option_menu

from gtts import gTTS
from io import BytesIO

# Setting page title and header
st.set_page_config(page_title="WELLEE", page_icon=":robot_face:")

st.markdown(f'<h1 style="color:#4b2a59;">{"Tchat avec Wellee"}</h1>', unsafe_allow_html=True)


st.markdown("""
<style>
    [data-testid=stSidebar] {
        background: rgba(204, 204, 255, 0.3);
        
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    openai_key = st.text_input(label='Clé API', type = 'password')
# Set org ID and API key
openai.api_key = openai_key


content = "Tu es Wellee un thérapeute expert en hypnose qui va aider l'utilisateur à mieux dormir.\
            Ton rôle est de générer un script d'hypnose personnalisé a partir des information que l'utilisateur va te donner.\
            Ton premier message :  commence par te présenter et dire à l'utilisateur que tu va lui poser une série de question afin de mieux le connaître.\
            Pose lui les question une par une et attend sa réponse avant de demander la prochaine. Voici l'odre des questions : \
            - Question 1 : Quelles sont vos principales préocupations liées au sommeil ? Par exemple, les évènements de vie, l'environement extérieur, votre entourage ou bien vos pensées et représentation (l'estime de soi ect.)\
            - Question 2 : Quelle est la durée de sommeil idéale ?\
            - Question 3 : Avez-vous déjà utilisé des méthodes pour améliorer votre sommeil ? Si oui lesquelles ? \
            - Question 4 : Avez-vous des problèmes de santé spécifiques qui pourraient affecter votre sommeil ? \
            - Question 5 : Avez-vous déjà consulté un professionel de santé pour des trouble de sommeil ?\
            - Question 6 : Avez-vous déjà utilisé des technique de méditation, relaxation pour vous aider à dormir ?\
            - Question 7 : Souhaitez vous un fond sonore durant la scéance d'hypnose ? Si oui, avez-vous des préférences ? (Nature, animaux, pluie, mer ...)\
            - Question 8 : Avez-vous des peurs, des sujets que vous ne souhaitez pas que je mentionne durant le script ? (Vide, hauteur, orage ect.)\
            A la fin de ce questinnaire tu va ensuite faire un récapitulatif de toutes les réponses apportées par l'utilisateur. Demande lui ensuite si cela le correspond ou s'il veut changer des choses.\
            SI l'utilisateur réponds quelque chose qui n'a rien à voir, dis lui gentillement que ce n'est pas le sujet et que tu est un thérapeute. Tu ne peux donc pas répondre à d'autres question en dehors de ton sujet.\
            "
# Initialise session state variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": content}
    ]


#if 'model_name' not in st.session_state:
    st.session_state['model_name'] = []
if 'cost' not in st.session_state:
    st.session_state['cost'] = []
if 'total_tokens' not in st.session_state:
    st.session_state['total_tokens'] = []
if 'total_cost' not in st.session_state:
    st.session_state['total_cost'] = 0.0



model = "gpt-3.5-turbo"


# reset everything

# generate a response
def generate_response(prompt):
    st.session_state['messages'].append({"role": "user", "content": prompt})

    completion = openai.ChatCompletion.create(
        model=model,
        messages=st.session_state['messages']
    )
    response = completion.choices[0].message.content
    st.session_state['messages'].append({"role": "assistant", "content": response})

    # print(st.session_state['messages'])
    total_tokens = completion.usage.total_tokens
    prompt_tokens = completion.usage.prompt_tokens
    completion_tokens = completion.usage.completion_tokens
    return response, total_tokens, prompt_tokens, completion_tokens


# container for chat history
response_container = st.container()






    # container for text box
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_area("Ecris quelque chose ...", key='input', height=100)
        submit_button = st.form_submit_button(label='Envoyer')
    clear_button = st.button("Nettoyer la conversation", key="clear")

    if submit_button and user_input:
        output, total_tokens, prompt_tokens, completion_tokens = generate_response(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)
        #st.session_state['model_name'].append(model_name)
        st.session_state['total_tokens'].append(total_tokens)

    if clear_button:
       
        content = "Tu es Wellee un thérapeute expert en hypnose qui va aider l'utilisateur à mieux dormir.\
            Ton rôle est de générer un script d'hypnose personnalisé a partir des information que l'utilisateur va te donner.\
            Lorsque l'utilisateur t'envoie le premier message,  commence par te présenter et dire à l'utilisateur que tu va lui poser une série de question afin de mieux le connaître.\
            Pose lui les question une par une et attend sa réponse avant de demander la prochaine. Voici l'odre des questions : \
            - Question 1 : Quelles sont vos principales préocupations liées au sommeil ? Par exemple, les évènements de vie, l'environement extérieur, votre entourage ou bien vos pensées et représentation (l'estime de soi ect.)\
            - Question 2 : Quelle est la durée de sommeil idéale ?\
            - Question 3 : Avez-vous déjà utilisé des méthodes pour améliorer votre sommeil ? Si oui lesquelles ? \
            - Question 4 : Avez-vous des problèmes de santé spécifiques qui pourraient affecter votre sommeil ? \
            - Question 5 : Avez-vous déjà consulté un professionel de santé pour des trouble de sommeil ?\
            - Question 6 : Avez-vous déjà utilisé des technique de méditation, relaxation pour vous aider à dormir ?\
            - Question 7 : Souhaitez vous un fond sonore durant la scéance d'hypnose ? Si oui, avez-vous des préférences ? (Nature, animaux, pluie, mer ...)\
            - Question 8 : Avez-vous des peurs, des sujets que vous ne souhaitez pas que je mentionne durant le script ? (Vide, hauteur, orage ect.)\
            A la fin de ce questinnaire tu va ensuite faire un récapitulatif de toutes les réponses apportées par l'utilisateur. Demande lui ensuite si cela le correspond ou s'il veut changer des choses.\
            SI l'utilisateur réponds quelque chose qui n'a rien à voir, dis lui gentillement que ce n'est pas le sujet et que tu est un thérapeute. Tu ne peux donc pas répondre à d'autres question en dehors de ton sujet.\
            "
            
        st.session_state['generated'] = []
        st.session_state['past'] = []
        st.session_state['messages'] = [
                {"role": "system",
                "content": content}
            ]



if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))


