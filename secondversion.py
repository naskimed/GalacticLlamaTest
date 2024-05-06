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

        st.session_state.messages = [{'role':'system','content':"Hello I'm Galactic Llama code chatbotk, I will assist you with your coding journey !"}]

    message("Hello I'm Galactic Llama code chatbot, I will assist you with your coding journey !")
    ask = False

    with st.sidebar:

        st.title("Happy coding journey !")
        user_input = st.text_area("Your code: ", key="user_input", height=420,  help="Paste your code here.")
        if user_input:
            st.session_state.messages.append({'role':'user', 'content': "Is this code is bugged?\n"+user_input})
            with st.spinner("Thinking.."):
                response = create_response(st.session_state.messages)
                resp = ""
                start_time = time.time()
                for chunk in response: 
                    # Check if 15 seconds have elapsed
                    if time.time() - start_time > 60:
                        print("Time limit exceeded. Exiting loop.")
                        break
                    
                    resp += chunk['message']['content']
                    print(chunk['message']['content'], end = ' ')

            st.session_state.messages.append({'role':'assistant', 'content': resp})

        stars = st_star_rating("Rate your experience", maxValue=5, defaultValue=3, key="rating", dark_theme = True)

    # messages = st.session_state.get('messages', [])
    # for i, msg in enumerate(messages):
    #     if i % 2 == 0:
    #         message(msg.content, is_user=True, key = str(i) + '_user')
    #     else:
    #         message(msg.content, is_user=False, key = str(i) + '_ai')
    i = 0
    for msg in st.session_state.messages:
        i+=1
        if msg['role'] == 'assistant':
            message(msg['content'], is_user= False, key = str(i) + '_user')
        elif msg['role'] == 'user':
            message(msg['content'], is_user=True, key = str(i) + '_assistant')

    st.subheader('Was this helpful?')
    if st.button('Yes'):
        st.success('Great to hear!')
    if st.button('No'):
        st.warning('We will improve!')


    # if user_input:
    #     message(user_input, is_user=True)
    #     st.session_state.messages.appned(HumanMessage(content=user_input))
    
    # resp = ""
    # # intro = """Is this code my cause a bug?
    # # """
    # response = create_response(user_input)
    # start_time = time.time()

    # if ask:
    #     ask = False
    #     with st.spinner("Thinking..."):
    #         for chunk in response: 
    #             # Check if 15 seconds have elapsed
    #             if time.time() - start_time > 90:
    #                 print("Time limit exceeded. Exiting loop.")
    #                 break
                
    #             resp += chunk['message']['content']
    #             print(chunk['message']['content'], end = ' ')

    #     message(resp)

        # st.subheader('Was this helpful?')
        # if st.button('Yes'):
        #     st.success('Great to hear!')
        # if st.button('No'):
        #     st.warning('We will improve!')

# if __name__ == '__main__':
main()

