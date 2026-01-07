"""
E-commerce Chatbot with FAQ and SQL routing
"""

import streamlit as st
from pathlib import Path
from faq import ingest_faq_data, faq_chain
from sql import sql_chain
from router import router


# ========================
# Configuration
# ========================

PAGE_TITLE = "🛍️ E-commerce Bot"
PAGE_ICON = "🤖"
FAQS_PATH = Path(__file__).parent / "book_chatbot_faq.csv"


# ========================
# Page Configuration
# ========================

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="centered",
    initial_sidebar_state="auto"
)


# ========================
# Initialization
# ========================

@st.cache_resource
def initialize_faq_data():
    """Load and cache FAQ data on first run"""
    try:
        ingest_faq_data(FAQS_PATH)
        return True
    except Exception as e:
        st.error(f"Error loading FAQ data: {e}")
        return False


# Initialize FAQ data
initialize_faq_data()


# ========================
# Core Functions
# ========================

def get_response(query: str) -> str:
    """
    Route query to appropriate handler and get response
    
    Args:
        query: User's input query
        
    Returns:
        Response string from the appropriate chain
    """
    try:
        route = router(query).name
        
        if route == 'faq':
            return faq_chain(query)
        elif route == 'sql':
            return sql_chain(query)
        else:
            return f"⚠️ Sorry, I don't know how to handle '{route}' queries yet."
            
    except Exception as e:
        return f"❌ Error processing your query: {str(e)}"


def initialize_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []


def display_chat_history():
    """Display all previous messages in the chat"""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def add_message(role: str, content: str):
    """Add a message to chat history"""
    st.session_state.messages.append({
        "role": role,
        "content": content
    })


# ========================
# UI Components
# ========================

def render_sidebar():
    """Render sidebar with information"""
    with st.sidebar:
        st.header("ℹ️ About")
        st.markdown("""
        This chatbot can help you with:
        - 📋 **FAQ**: Common questions about products, returns, tracking
        - 🔍 **Product Search**: Find products and check prices
        """)
        
        st.divider()
        
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            st.rerun()
        
        st.divider()
        st.caption(f"💬 Messages: {len(st.session_state.messages) // 2}")


# ========================
# Main App
# ========================

def main():
    """Main application logic"""
    
    # Initialize
    initialize_session_state()
    
    # Render UI
    st.title(PAGE_TITLE)
    st.caption("Ask me anything about our products, policies, or search our catalog!")
    
    render_sidebar()
    
    # Display chat history
    display_chat_history()
    
    # Handle new user input
    if query := st.chat_input("💬 Write your query here..."):
        # Display user message
        with st.chat_message("user"):
            st.markdown(query)
        add_message("user", query)
        
        # Get and display bot response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_response(query)
            st.markdown(response)
        add_message("assistant", response)


# ========================
# Entry Point
# ========================

if __name__ == "__main__":
    main()
