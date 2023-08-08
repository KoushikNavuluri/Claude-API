import os
from claude_api import Client
from fastapi.responses import StreamingResponse

STREAM = True

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

    if STREAM:
        while True:
            user_input = input("You: ")
            while not user_input:
                user_input = input("You: ")

            if user_input.lower() == 'exit':
                print("Thank you!")
                break

            if not conversation_id:
                conversation = claude.create_new_chat()
                conversation_id = conversation['uuid']

            print("Chatbot:")
            for data in claude.send_message(prompt=user_input, conversation_id=conversation_id, attachment=None, stream=True):
                print(data, end="", flush=True)
            print("\n")

    else:
        while True:
            user_input = input("You: ")
            while not user_input:
                user_input = input("You: ")

            if user_input.lower() == 'exit':
                print("Thank you!")
                break

            if not conversation_id:
                conversation = claude.create_new_chat()
                conversation_id = conversation['uuid']

            response = claude.send_message(user_input, conversation_id)
            print("Chatbot:", response, sep="")

if __name__ == "__main__":
    main()
