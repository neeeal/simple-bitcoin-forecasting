import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)

# Add a CSS style to center the title
st.markdown(
    """
    <style>
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create a container div with the center class to center the title
st.markdown('<div class="center"><h1>Time Classification</h1></div>', unsafe_allow_html=True)

st.sidebar.success("Select page above.")
