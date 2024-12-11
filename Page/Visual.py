import streamlit as st

def app():
    st.title("Visual!")

    st.write("Welcome to the Data Visulisation section.")
    st.write("To Visualize our work You have to use PowerBi App.")
    st.write("To Download Power Bi app click on the button below.")
    st.write("After downloading Power Bi application click on the Download button to download our Power Bi report.")

    url = "https://www.microsoft.com/en-us/download/details.aspx?id=58494"
    if st.button("Power Bi"):
        js_code = f'window.open("{url}");' 
        st.components.v1.html(f'<script>{js_code}</script>', height = 0)
                            
    file_path = "DataVisualisation/IITSeatAllocation.pbix"
    with open(file_path , 'rb') as file:
        file_content = file.read()

    st.download_button("Download Report" ,
                    data = file_content ,
                        file_name = "JeeReport.pbix",
                        mime = "application/octet-stream" )
