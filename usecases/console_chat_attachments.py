import os
import re

from claude_api import Client

# Regular expression to capture {{filepath=./path/to/file.csv}}
FILE_PATH_RE = r"\{\{filepath=(.*?)\}\}"


def get_cookie():
    # Your method to retrieve the cookie.
    return "YOUR_COOKIE_IS_HERE"

def extract_file_path(user_input):
    """
    Extracts the file path from the user input based on the defined regex pattern.
    Returns the cleaned user input and the extracted file path.
    """
    matches = re.findall(FILE_PATH_RE, user_input)
    file_path = matches[0] if matches else None
    cleaned_input = re.sub(FILE_PATH_RE, '', user_input).strip()
    return cleaned_input, file_path


def read_file_content(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def main():
    cookie = get_cookie()
    claude = Client(cookie)
    conversation_id = None

    print("Welcome to Claude AI Chat with Single Prompt Attachments!")

    while True:
        user_input = input("You (use {{filepath=./your_file.csv}} for attachments): ")

        if user_input.lower() == 'exit':
            print("Thank you!")
            break

        user_input, file_path = extract_file_path(user_input)
        
        # Check if the file exists
        if file_path and not os.path.exists(file_path):
            print("File doesn't exist. Sending message without attachment.")
            file_path = None  # Set file_path to None so no attachment is sent

        # If conversation_id is not yet created, create a new chat
        if not conversation_id:
            conversation = claude.create_new_chat()
            conversation_id = conversation['uuid']

        # Prepare the payload with or without the file content based on the extracted file path
        attachment_data = None
        if file_path:
            file_content = read_file_content(file_path)
            attachment_data = {
                "file_name": os.path.basename(file_path),
                "file_type": "text/csv",  # Assuming CSV, but you can adjust based on file types
                "file_size": os.path.getsize(file_path),
                "extracted_content": file_content
            }
        
        # Send message with or without attachment based on the attachment_data
        response = claude.send_message(user_input, conversation_id, attachments=attachment_data)

        print("Chatbot:", response['completion']['prompt'] if 'completion' in response else response)

if __name__ == "__main__":
    main()
