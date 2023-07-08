import openai
import streamlit as st


# Setting page title and header
st.set_page_config(page_title="WELLEE", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'>Wellee Chatbot 👩‍⚕️ </h1>", unsafe_allow_html=True)


 
st.title("💬 Chat with Wellee")


if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if 'past' not in st.session_state:
    st.session_state['past'] = []

if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "Act as a therapist, first you need to ask the user why he wants to use wellee app"}
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



for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])






if prompt := st.chat_input("What is up?"):
    clear_button = st.button("Clear Conversation", key="clear")
    if clear_button:
            st.session_state['generated'] = []
            st.session_state['past'] = []
            st.session_state.messages = [
                {"role": "system", "content": "Act as a therapist, first you need to ask the user why he wants to use wellee app"}
            ]
    


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


