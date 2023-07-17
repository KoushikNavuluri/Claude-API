import os
from claude_api import Client

def get_cookie():
    cookie = os.environ.get('cookie')
    if not cookie:
        raise ValueError("Please set the 'cookie' environment variable.")
    return cookie

def main():
    cookie = get_cookie()
    claude = Client(cookie)
    conversation_id = None

    print("Welcome to Claude AI Chat!")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Thank you!")
            break

        if not conversation_id:
            conversation = claude.create_new_chat()
            conversation_id = conversation['uuid']

        response = claude.send_message(user_input, conversation_id)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
