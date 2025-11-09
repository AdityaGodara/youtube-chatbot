import streamlit as st
from langchain_helper import create_vectordb_from_yt, get_conversation_chain

# Page config
st.set_page_config(
    page_title="YouTube Video ChatBot",
    page_icon="🎥",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.chat-container {
    border-radius: 10px;
    padding: 20px;
    background-color: #f5f5f5;
}
.user-message {
    background-color: #007bff;
    color: white;
    padding: 10px;
    border-radius: 10px;
    margin: 5px 0;
}
.bot-message {
    background-color: black;
    padding: 10px;
    border-radius: 10px;
    margin: 5px 0;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "processed_url" not in st.session_state:
    st.session_state.processed_url = None

# Main title
st.title("🎥 YouTube Video ChatBot")
st.write("Ask questions about any YouTube video!")

# URL input
url = st.text_input("Enter YouTube Video URL:")

if url and url != st.session_state.processed_url:
    with st.spinner("Processing video content..."):
        vectorstore = create_vectordb_from_yt(url)
        st.session_state.conversation = get_conversation_chain(vectorstore)
        st.session_state.processed_url = url
        st.session_state.chat_history = []
    st.success("Video processed! You can now ask questions.")

# Chat interface
if st.session_state.conversation:
    col1, col2 = st.columns([3, 1])
    
    with col1:
        user_question = st.text_input("Ask a question about the video:", key="user_input")
        if user_question:
            with st.spinner("Thinking..."):
                response = st.session_state.conversation({
                    'question': user_question
                })
                st.session_state.chat_history.append(("user", user_question))
                st.session_state.chat_history.append(("bot", response['answer']))

    # Display chat history
    with col2:
        st.subheader("Chat History")
        
    # st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    for role, message in st.session_state.chat_history:
        if role == "user":
            st.markdown(f"<div class='user-message'>👤 You: {message}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot-message'>🤖 Bot: {message}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by Aditya Godara & Om Gupta")