import streamlit as st
import streamlit_option_menu as som
import Page.home as home
import Page.Visual as visual

class Main:
    def __init__(self) :
        self.app = []

    def add_apps(self , title , function):
        self.app.append({
            'title' : title,
            'function' : function
        })

    def run():
        with st.sidebar :
            app = som.option_menu(
                menu_title='Jee Seat Allocation',
                options = ['Home' , 'Visualize'],
                icons=['house-fill' , 'bar-chart-fill'],
                menu_icon='cast', # fix it
                default_index=0

            )

        if app == 'Home':
            home.app()
        if app == 'Visualize':
            visual.app()

    run()