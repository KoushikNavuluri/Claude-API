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
    conversations = claude_api.list_all_conversations()
    for conversation in conversations:
        conversation_id = conversation['uuid']
        print(conversation_id)

if __name__ == "__main__":
    main()
