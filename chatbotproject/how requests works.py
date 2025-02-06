import requests
import json

def generate_content(input_text):
    """
    Sends a request to the generative language API and returns the response.

    Args:
        api_key (str): Your API key for the generative language API.
        input_text (str): The input text to generate content for.

    Returns:
        dict: The response from the API.
    """
    api_key = "AIzaSyBcdKfkJJ5bjqqLmfnRFJe43XvoNLmU0qQ"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{
            "parts": [{"text": input_text}]
        }]
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        return response.json()
    else:
        return {
            "error": response.status_code,
            "message": response.text
        }

# Example usages :
# api_key = "YOUR_API_KEY"
while True:
    inp = input("Enter the input text: ")
    if inp == "exit":
        break
    result = generate_content( inp)
    result = result['candidates'][0]['content']['parts'][0]['text']
    print(result)



