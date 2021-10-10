import streamlit as st


def header1(url):
    st.markdown(f'<p style="color:#2f4f4f;font-size:50px;">{url}</p>',
                unsafe_allow_html=True)


def header2(url):
    st.markdown(f'<p style="color:#DC143C;font-size:30px;">{url}</p>',
                unsafe_allow_html=True)


def header3(url):
    st.markdown(f'<p style="color:#2f4f4f;font-size:40px;">{url}</p>',
                unsafe_allow_html=True)


def header4(url):
    st.markdown(f'<p style="color:#2f4f4f;font-size:42px;">{url}</p>',
                unsafe_allow_html=True)
