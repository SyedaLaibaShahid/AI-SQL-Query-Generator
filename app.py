import streamlit as st
import google.generativeai as genai

google_api_key = ""
genai.configure(api_key=google_api_key)
model=genai.GenerativeModel("models/gemini-2.5-flash")




def main():
    st.set_page_config(page_title="SQL Query Generator 🤖", page_icon=":robot:")

    st.markdown(
        """
        <div style="text-align: center;">
            <h1>SQL Query Generator 🤖</h1>
            <h3>I can generate SQL queries for you!</h3>
            <h4>With Explanation as well!!!</h4>
            <p>This tool is a simple tool that allows you to generate SQL queries based on your prompts.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    text_input = st.text_area("Enter your Query here (Plain Text):")
    submit = st.button("Generate SQL Query")

    if submit:
        with st.spinner("Generating SQL Query..."):
            st.write ("Create a SQL query snippet using the below text:")
            st.markdown(
                f"""
                <div style="
                    border: 1px solid #00cc66;
                    padding: 8px;
                    border-radius: 6px;
                    margin-top: 7px;
                    margin-bottom:15px;
                    font-family: monospace;
                    background-color: #f9fff9;
                ">
                    {text_input}
                </div>
                """,
                unsafe_allow_html=True
            )

            formatted_templete=f"""
Create a SQL query snippet using the below text:
{text_input}
"""
            response = model.generate_content(formatted_templete)
            sql_query=response.text
            st.write(sql_query)

if __name__ == "__main__":
    main()