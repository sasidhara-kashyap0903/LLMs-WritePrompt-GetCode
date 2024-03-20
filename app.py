import streamlit as st

from helper_gemini import gemini_text
from helper_openai import openai_text

time_complexity = False
space_complexity = False
generate_test_data = False
integrate_test_cases = False
perform_code_review = False
explain_code = False
add_error_handling = False
write_code_docs = False

my_output = None


def scrollable_text(text):
    return f'<div style="border: 1px solid black; border-radius: 10px; padding: 20px; overflow-y: scroll; height: 590px; box-shadow: 1px 1px 1px gray, -1px -1px 1px gray, 1px -1px 1px gray, -1px 1px 1px gray;">{text}</div>'


def main():
    # change the project name on the browser tab using streamlit
    st.set_page_config(page_title="Write Prompt - Get Code in All Languages", layout="wide")
    st.title("Write Prompt - Get Code in All Languages")
    if "api_key" not in st.session_state:
        st.session_state.api_key = ""
    if "prompt" not in st.session_state:
        st.session_state.prompt = ""
    if "output_text" not in st.session_state:
        st.session_state.output_text = ""

    # Configuration sidebar
    st.sidebar.header('Configuration')
    selected_ai_model = st.sidebar.radio(
        'Select AI Model', ['ChatGPT', 'Gemini'])
    st.session_state.api_key = st.sidebar.text_input(label=f'{selected_ai_model} API Key',
                                                     type='password')
    save_key = st.sidebar.button('Done')
    if save_key:
        try:
            if not st.session_state.api_key:
                raise ValueError("API key is required")

            # call API using api_key

        except ValueError as err:
            st.error(err)

    # write a session state variable with the name prompt
    st.session_state.prompt = st.text_area(
        label="Enter your prompt", value="")

    # Using columns to create two columns, make one column 2/3 and other 1/3
    col1, col2 = st.columns([2, 1])

    # Adding content to the first column
    with col1:
        my_output = st.markdown(scrollable_text(st.session_state.output_text),
                                unsafe_allow_html=True)

    # Adding content to the second column
    with col2:
        st.header("Customize")
        # Perform Analysis
        st.subheader("Perform Analysis")
        col1, col2 = st.columns(2)
        with col1:
            global time_complexity
            time_complexity = st.checkbox("Time Complexity")
        with col2:
            global space_complexity
            space_complexity = st.checkbox("Space Complexity")

        # Select the language
        st.subheader("Change Language")
        language = st.selectbox(
            label="Select Language",
            options=["Select Language", "Python",
                     "JAVA", "C++", "C#", "JavaScript",
                     "Pascal", "TypeScript",
                     "TSX", "JSX", "Vue", "Go",
                     "C", "Visual Basic .NET",
                     "SQL", "Assembly Language", "PHP", "Ruby",
                     "Swift", "SwiftUI", "Kotlin", "R", "Objective-C",
                     "Perl", "SAS", "Scala", "Dart", "Rust", "Haskell",
                     "Lua", "Groovy", "Elixir", "Clojure", "Lisp", "Julia",
                     "Matlab", "Fortran", "COBOL", "Bash", "Powershell",
                     "PL/SQL", "CSS", "Racket", "HTML", "NoSQL", "CoffeeScript"]
        )

        # Testing Tools
        st.subheader("Testing Tools")
        col1, col2 = st.columns(2)
        with col1:
            global generate_test_data
            generate_test_data = st.checkbox("Generate Test Data")
        with col2:
            global integrate_test_cases
            integrate_test_cases = st.checkbox("Generate Test Cases")

        # More Actions
        st.subheader("More Actions")
        col1, col2 = st.columns(2)

        with col1:
            global perform_code_review
            perform_code_review = st.checkbox("Perform Code Review")

        with col2:
            global explain_code
            explain_code = st.checkbox("Explain Code")
        with col2:
            global write_code_docs
            write_code_docs = st.checkbox("Generate Docs")

        with col1:
            global add_error_handling
            add_error_handling = st.checkbox("Add Error Handling")

        send = st.button("Send", use_container_width=True)
        if send:
            if st.session_state.prompt:
                st.session_state.prompt = f"- Hello \n Perform the following.\n - \
                {st.session_state.prompt}"
                if time_complexity:
                    st.session_state.prompt = st.session_state.prompt + \
                        f"\n - Find time complexity of the generated code."
                if space_complexity:
                    st.session_state.prompt = st.session_state.prompt + \
                        f"\n - Find space complexity of the generated code."
                if language != "Select Language":
                    st.session_state.prompt = st.session_state.prompt + \
                        f"\n - Convert this code into {language}."
                if generate_test_data:
                    st.session_state.prompt = st.session_state.prompt + \
                        f"\n - Generate test data for the generated code."
                if integrate_test_cases:
                    st.session_state.prompt = st.session_state.prompt + \
                        f"\n - Integrate test cases for the generated code."
                if perform_code_review:
                    st.session_state.prompt = st.session_state.prompt + \
                        f"\n - Perform code review for the generated code."
                if explain_code:
                    st.session_state.prompt = st.session_state.prompt + \
                        f"\n - Explain the generated code."
                if add_error_handling:
                    st.session_state.prompt = st.session_state.prompt + \
                        f"\n - Add error handling for the generated code."
                if write_code_docs:
                    st.session_state.prompt = st.session_state.prompt + \
                        f"\n - Generate function docs for the generated code."

                # print("Prompt : ")
                # print(st.session_state.prompt)
                # print("Selected Language : ")
                # print(selected_ai_model)

                if selected_ai_model == 'ChatGPT':
                    st.session_state.output_text = openai_text(
                        st.session_state.prompt, st.session_state.api_key)
                elif selected_ai_model == 'Gemini':
                    st.session_state.output_text = gemini_text(
                        st.session_state.prompt, st.session_state.api_key)
                my_output.markdown(scrollable_text(
                    st.session_state.output_text),
                    unsafe_allow_html=True)
            else:
                st.error("Prompt is required")


if __name__ == "__main__":
    main()
