
import google.generativeai as genai
import google.ai.generativelanguage as glm


def gemini_text(prompt, entered_api_key):
    genai.configure(api_key=entered_api_key)
    model = genai.GenerativeModel("gemini-pro")

    response = model.generate_content(
        f"You are a helpful programmer. You only respond if the prompt is relevent to programming. You only communicate in proper markdown with proper formatting and headings of each task.\n  Prompt: {prompt}.")
    # print(f"RESPONSE GEMINI : {response}")
    # print(f"RESPONSE TEXT GEMINI : {response.text}")

    return response.text
