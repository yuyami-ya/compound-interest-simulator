import streamlit as st

from pages import dashboard

def main():
    st.title("複利計算シミュレータ")
    dashboard.display()

if __name__ == "__main__":
    main()