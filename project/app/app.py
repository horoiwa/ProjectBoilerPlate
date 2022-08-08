import streamlit as st


def main():

    PAGES = {
        "Main app": main_app,
        "Sub app": sub_app
    }

    st.sidebar.title("sidebar")

    selection = st.sidebar.radio("Go to ", list(PAGES.keys()), index=0)
    PAGES[selection]()


def main_app():
    st.title("Main App")

    st.header("Header")
    st.text("Main App")

    st.subheader("Sub header")
    st.text("Main App")


def sub_app():
    st.title("Sub App")
    st.text("sub App")


if __name__ == '__main__':
    main()
