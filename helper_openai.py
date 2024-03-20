from openai import OpenAI


def openai_text(prompt, entered_api_key):
    client = OpenAI(api_key=entered_api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful programmer. You only respond if the prompt is relevent to programming. You only communicate using markdown with proper formatting and headings of each task."},
            {"role": "user", "content": prompt}
        ],
        # max_tokens=300,  # the maximum number of tokens to generate in the completion
        temperature=0,  # this is the degree of randomness of the model's output
    )
    # print(f"RESPONSE OPENAI : {response}")
    # print(f"response.choices[0].message.content : {
    #       response.choices[0].message.content}")
    return response.choices[0].message.content
