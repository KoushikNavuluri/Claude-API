import discord
from discord.ext import commands
from claude_api import create_new_chat, send_message, delete_conversation
import keep_alive
import os

token = os.environ.get('token')

intents = discord.Intents.default()
intents.message_content = True  # Enable receiving message content

bot = commands.Bot(command_prefix='!', intents=intents)


def load_conversation_id():
  with open('conversation_id.txt', 'r') as file:
    return file.read().strip()


conversation_id = load_conversation_id()


def save_conversation_id(conversation_id):
  with open('conversation_id.txt', 'w') as file:
    file.write(conversation_id)


def delete_conversation_id():
  global conversation_id
  if conversation_id is not None:
    delete_conversation(conversation_id)
  conversation_id = create_new_chat()['uuid']
  save_conversation_id(conversation_id)


@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name} ({bot.user.id})')
  conversation_id = load_conversation_id()


@bot.event
async def on_message(message):
  global conversation_id  # Declare conversation_id as global
  if not message.author.bot:
    channel_id = message.channel.id
    user_id = message.author.id
    content = message.content

    if content.lower() == 'delete':
      if conversation_id is None:
        reply = 'There is no active conversation to delete.'
      else:
        delete_conversation_id()
        reply = 'Chat conversation deleted.'
    else:
      if conversation_id is None:
        new_chat = create_new_chat()
        conversation_id = new_chat['uuid']
        save_conversation_id(conversation_id)

      async with message.channel.typing():
        response = send_message(content, conversation_id)
        reply = response['answer']

    await message.channel.send(reply)
  await bot.process_commands(message)


keep_alive.keep_alive()
bot.run(token)
