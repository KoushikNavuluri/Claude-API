# Claude AI-API ( Unofficial )
This project provides an unofficial API for Claude AI, allowing users to access and interact with Claude AI .

## Prerequisites

To use this API, you need to have the following:

Python installed on your system
requests library installed 
```bash
  pip install requests

```

## Installation

To use the Claude AI Unofficial API, you can either clone the GitHub repository or directly download the Python file.

Clone the repository:

    git clone https://github.com/KoushikNavuluri/Claude-API.git

## Usage

Import the claude_api module in your Python script:

    from claude_ai import Client

Next, you need to create an instance of the Client class by providing your Claude AI cookie and organization ID:

    cookie = os.environ.get('cookie')
    
    claude_api = Client(cookie)

## List All Conversations

To list all the conversation Id's you had with Claude , you can use the list_all_conversations method:

    conversations = claude_api.list_all_conversations()
    for conversation in conversations:
        conversation_id = conversation['uuid']
        print(conversation_id)

## Send Message

To send a message to Claude, you can use the send_message method. You need to provide the prompt and the conversation ID:



    prompt = "Hello, Claude!"
    conversation_id = "<conversation_id>"
    response = claude_api.send_message(prompt, conversation_id)
    print(response)

## Delete Conversation

To delete a conversation, you can use the delete_conversation method:


    conversation_id = "<conversation_id>"
    deleted = claude_api.delete_conversation(conversation_id)
    if deleted:
        print("Conversation deleted successfully")
    else:
        print("Failed to delete conversation")

## Chat Conversation History

To get the chat conversation history, you can use the chat_conversation_history method:    

    conversation_id = "<conversation_id>"
    history = claude_api.chat_conversation_history(conversation_id)
    print(history)

## Create New Chat

To create a new chat conversation (id), you can use the create_new_chat method:


    new_chat = claude_api.create_new_chat()
    conversation_id = new_chat['uuid']
    print(conversation_id)

## Reset All Conversations

To reset all conversations, you can use the reset_all method:


    reset = claude_api.reset_all()
    if reset:
        print("All conversations reset successfully")
    else:
        print("Failed to reset conversations")   

## Rename Chat

To rename a chat conversation, you can use the rename_chat method:

    conversation_id = "<conversation_id>"
    title = "New Chat Title"
    renamed = claude_api.rename_chat(title, conversation_id)
    if renamed:
        print("Chat conversation renamed successfully")
    else:
        print("Failed to rename chat conversation")

## Disclaimer

This project provides an unofficial API for Claude AI and is not affiliated with or endorsed by Claude AI or Anthropic. Use it at your own risk.

Please refer to the official Claude AI documentation[https://claude.ai/docs] for more information on how to use Claude AI.
        
    




    
