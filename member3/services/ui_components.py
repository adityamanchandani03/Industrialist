import streamlit as st


def success(message):

    st.success(message)


def error(message):

    st.error(message)


def info(message):

    st.info(message)


def header(title):

    st.title(title)


def subheader(title):

    st.subheader(title)