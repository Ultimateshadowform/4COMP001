import streamlit as st


def show_log_in():
    st.write("Log in page: coming soon.")


def show_this_week(username):
    st.write("This week page: coming soon.")


def show_add_spending(username):
    st.write("Add spending page: coming soon.")


def show_my_spending(username):
    st.write("My spending page: coming soon.")


def show_weekly_budget(username):
    st.write("Weekly budget page: coming soon.")


st.title("Student Budget Tracker")

username = st.session_state.get("username")

if username is None:
    show_log_in()
else:
    page = st.sidebar.radio("Go to", ["This week", "Add spending", "My spending", "Weekly budget"])
    if page == "This week":
        show_this_week(username)
    elif page == "Add spending":
        show_add_spending(username)
    elif page == "My spending":
        show_my_spending(username)
    else:
        show_weekly_budget(username)
