import streamlit as st
from streamlit_chat import message
from streamlit_star_rating import st_star_rating
from model import create_response
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
import time


def main():
    st.set_page_config(
        page_title = "Galactic Llama",
        page_icon = "🤖"
    )
    # llm = select_llm()

    css = '''
    <style>
        [data-testid="stSidebar"]{
            min-width: 400px;
            max-width: 800px;
        }
    </style>
    '''
    st.markdown(css, unsafe_allow_html=True)

    st.header("Galactic Llama Code Chatbot:")

    if "messages" not in st.session_state:

        st.session_state.messages = [SystemMessage(content="Hello I'm Galactic Llama code chatbotk, I will assist you with your coding journey !")]

    message("Hello I'm Galactic Llama code chatbot, I will assist you with your coding journey !")
    ask = False

    with st.sidebar:

        st.title("Happy coding journey !")
        user_input = st.text_area("Your code: ", key="user_input", height=420,  help="Paste your code here.")
        if st.button("Ask"):
            ask = True

            # st.write(response)
        stars = st_star_rating("Rate your experience", maxValue=5, defaultValue=3, key="rating", dark_theme = True)

    if user_input:
        message(user_input, is_user=True)
        st.session_state.messages.appned(HumanMessage(content=user_input))
    
    resp = ""
    # intro = """Is this code my cause a bug?
    # """
    response = create_response(user_input)
    if ask:
        ask = False
        with st.spinner("Thinking..."):
            print("generating")
            for chunk in response: 
                # Check if 15 seconds have elapsed
                # if time.time() - start_time > 90:
                #     print("Time limit exceeded. Exiting loop.")
                #     break
                # print("first")
                resp += chunk['message']['content']
                # print("second")
                print(chunk['message']['content'], end = ' ')

        message(resp)

        st.subheader('Was this helpful?')
        if st.button('Yes'):
            st.success('Great to hear!')
        if st.button('No'):
            st.warning('We will improve!')

if __name__ == '__main__':
    main()


# import streamlit as st
# from streamlit_chat import message
# from streamlit_star_rating import st_star_rating
# from model import *
# from model import select_llm

# def init_page():
#     st.set_page_config(
#         page_title="Galactic Llama",
#         page_icon="🤖"
#     )
#     st.header("Galactic Llama Code Chatbot:")

#     message("Hello I'm Galactic Llama code chatbot, I will assist you with your coding journey !")
#     message("""def my_function():
#                 print("hello wolrd")""", is_user=True)

#     st.subheader('Was this helpful?')
#     if st.button('Yes'):
#         st.success('Great to hear!')
#     if st.button('No'):
#         st.warning('We will improve!')

#     css = '''
#     <style>
#         [data-testid="stSidebar"]{
#             min-width: 400px;
#             max-width: 800px;
#         }
#     </style>
#     '''
#     st.markdown(css, unsafe_allow_html=True)

#     st.title("Happy coding journey !")
#     user_input = st.text_area("Your code: ", key="user_input", height=420, help="Paste your code here.")

#     stars = st_star_rating("Rate your experience", maxValue=5, defaultValue=3, key="rating", dark_theme=True)

#     return user_input

# def main():
#     user_input = init_page()
    
#     llm = select_llm()
#     answer = get_answer(llm, user_input)

#     with st.spinner("Bot is typing ..."):
#         message(answer)

# if __name__ == '__main__':
#     main()
