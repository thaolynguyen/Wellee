import openai
import streamlit as st


# Setting page title and header
st.set_page_config(page_title="WELLEE", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'>Wellee Chatbot 👩‍⚕️ </h1>", unsafe_allow_html=True)

with st.sidebar:
    openai_key = st.text_input(label='Clé API', type = 'password')
# Set org ID and API key
openai.api_key = openai_key

model = "gpt-3.5-turbo"

st.title("💬 Chat with Wellee")
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

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if 'past' not in st.session_state:
    st.session_state['past'] = []

if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": content}
    ]



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

clear_button = st.button("Clear Conversation", key="clear")
if clear_button:
    st.session_state['generated'] = []
    st.session_state['past'] = []
    st.session_state.messages = [
                {"role": "system", "content": content}
            ]
    
cpt = 0

for message in st.session_state.messages:
    if cpt !=0:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    cpt +=1






if prompt := st.chat_input("What is up?"):
    


    st.session_state.messages.append({"role": "user", "content": prompt})



    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})




