import base64
from mimetypes import guess_type
from openai import OpenAI
key = open('key', 'r').readline().rstrip()
client = OpenAI(api_key=key)

colours = {
    "sad":"dark_blue",
    "happy":"yellow",
    "passionate":"pink",
    "terrified":"brown",
    "tired":"grey",
    "calm":"blue"
}


def local_image_to_data_url(image_path):
    # Guess the MIME type of the image based on the file extension
    mime_type, _ = guess_type(image_path)
    if mime_type is None:
        mime_type = 'application/octet-stream'  # Default MIME type if none is found

    # Read and encode the image file
    with open(image_path, "rb") as image_file:
        base64_encoded_data = base64.b64encode(image_file.read()).decode('utf-8')

    # Construct the data URL
    return f"data:{mime_type};base64,{base64_encoded_data}"


def gpt(data_url):
    messages=[
        {"role": "user", 
            "content": [
	            {
	                "type": "text",
	                "text": "Analyze the photo and choose the emotion which describes it in the best way from the list: [[happy], [sad], [terrified], [calm], [passionate], [tired]]. The output is only the emotion."
	            },
	            {
	                "type": "image_url",
	                "image_url": {
                        "url": data_url
                    }
                } 
           ] }
    ]
    chat = client.chat.completions.create(model='gpt-4-turbo', messages=messages)
    return chat.choices[0].message.content


def extractData_image(image_path):
    data_url = local_image_to_data_url(image_path)
    return gpt(data_url)