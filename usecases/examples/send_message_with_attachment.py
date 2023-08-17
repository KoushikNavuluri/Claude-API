import os
from claude_api import Client

def get_cookie():
    cookie = os.environ.get('cookie')
    if not cookie:
        raise ValueError("Please set the 'cookie' environment variable.")
    return cookie

def main():
    cookie = get_cookie()
    claude_api = Client(cookie)
    prompt = "Hey,Summarize me this document.!"
    conversation_id = claude_api.create_new_chat()['uuid']
    response = claude_api.send_message(prompt, conversation_id, attachment="../igor-popov-idea.pdf", timeout=600)
    print(response)

if __name__ == "__main__":
    main()
