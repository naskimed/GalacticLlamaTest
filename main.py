import streamlit as st
from streamlit_chat import message
from streamlit_star_rating import st_star_rating

def main():
    st.set_page_config(
        page_title = "Galactic Llama",
        page_icon = "🤖"
    )

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

    message("Hello I'm Galactic Llama code chatbot, I will assist you with your coding journey !")
    message("""def my_function():
                print("hello wolrd")""", is_user = True)
    
    st.subheader('Was this helpful?')
    if st.button('Yes'):
        st.success('Great to hear!')
    if st.button('No'):
        st.warning('We will improve!')
    
    with st.sidebar:

        st.title("Happy coding journey !")
        user_input = st.text_area("Your code: ", key="user_input", height=420,  help="Paste your code here.")

        # st.write("Rate your experience:")
        # rating = st.radio(
        #     label="",
        #     options=('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐', '⭐⭐⭐', '⭐⭐', '⭐' )
        # )
        # st.write(f"You rated: {rating}")
        stars = st_star_rating("Rate your experience", maxValue=5, defaultValue=3, key="rating", dark_theme = True)


if __name__ == '__main__':
    main()