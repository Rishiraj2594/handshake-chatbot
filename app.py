import streamlit as st

from embedchain import App

from scrape import get_top_links

st.set_page_config(page_title="Handshake chatbot",page_icon=":handshake:")
@st.cache_resource
def embedchain_bot():
    app= App.from_config(config={
      "app": {
        "config": {
            "id": "bot1",
        }

      },
       'llm': {
             'provider': 'openai',
             'config': {
                 'model': 'gpt-3.5-turbo',
                 'temperature': 1.0,
                 'max_tokens': 1000,
                 'top_p': 1,
                'stream': False,
                "prompt": (
    "Please consider the provided context while crafting responses to general queries, ensuring they remain relevant and coherent.\n\n"
    "If you feel like query doesn't contain enough info to found in context then don't answer ask the user more about query"
    "Incorporate the context into your answers to maintain continuity and accuracy.\n\n"
    "Strive to understand the nuances within the context and synthesize them with the query to provide comprehensive responses.\n"
    "$context\n\nQuery: $query\n\nResponse:"
    ),
                 'system_prompt': (
                      "your name is Handshake guru Act as a very knowlegable person and respond in bro lang that helps and do tasks for people regarding their queries "
                 ),
                 'number_documents':5,
             }
         },
    })
    #app.add("/home/ubuntu/chatbot/Our Deck.pdf", data_type='pdf_file')
    return app

faq_questions = [
    "What is Handshake?",
    "What is Proof of work?",
    "What is Agaamin?",
    "What are Smart names?"
]
app = embedchain_bot()
st.title("Handshake  Chatbot")
st.caption("🚀 An Embedchain app powered by OpenAI!")
st.subheader("FAQs")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """
        Hi! I'm a chatbot. I can answer questions and learn new things!\n
        Ask me anything and if you want me to learn something do `/add <source>`.\n
        You can also search on hnssearch.io using `/search <search_query>`\n
        I can learn mostly everything. :)
        """,
        }
    ]

button_col1, button_col2 = st.columns(2)

# Define function to execute FAQ prompt
def execute_faq_prompt(prompt):
        #st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
       # msg_placeholder = st.empty()
        #msg_placeholder.markdown("Thinking...")
        full_response = ""

        for response in app.chat(prompt):
            #msg_placeholder.empty()
            full_response += response

        #msg_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# Create layout with 2x2 grid of buttons
button_col1, button_col2 = st.columns(2)

# Create buttons in the first column
for i in range(2):
    if button_col1.button(faq_questions[i]):
        print("hi")
        execute_faq_prompt(faq_questions[i])

# Create buttons in the second column
for i in range(2, 4):
    if button_col2.button(faq_questions[i] ):
        execute_faq_prompt(faq_questions[i])

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything!"):

    if prompt.startswith("/add"):
        with st.chat_message("user"):
            st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
        prompt = prompt.replace("/add", "").strip()
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("Adding to knowledge base...")
            app.add(prompt)
            message_placeholder.markdown(f"Added {prompt} to knowledge base!")
            st.session_state.messages.append({"role": "assistant", "content": f"Added {prompt} to knowledge base!"})
            st.stop()
    if prompt.startswith("/search"):
        with st.chat_message("user"):
            st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
        search_query = prompt.replace("/search", "").strip()
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("Searching on hnssearch.io ...")
            top_links = get_top_links(search_query, 3)
            results  = "\n".join([f"{i+1}. {link}" for i, link in enumerate(top_links)])
            disclaimer = "Please note: You'll need a handshake resolver, like a fingertip, to access these links."
            #message_placeholder.markdown("Please note: You'll need a handshake resolver, like a fingertip, to access these links.")
            message_placeholder.markdown(f"{disclaimer}\n\nTop three links:\n{results}")
            # message_placeholder.markdown(f"Top three links\n1. {top_links[0]}")
            #st.session_state.messages.append({"role": "assistant", "content": "Please note: You'll need a handshake resolver, like a fingertip, to access these links."})
            st.session_state.messages.append({"role": "assistant", "content": f"{disclaimer}\n\nTop three links:\n{results}"})
            st.stop()

    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        msg_placeholder = st.empty()
        msg_placeholder.markdown("Thinking...")
        full_response = ""

        for response in app.chat(prompt):
            msg_placeholder.empty()
            full_response += response

        msg_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
