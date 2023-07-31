```python
import random
from telegram.ext import Updater, CommandHandler

# Define the start command handler
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the Dragon Ball Bot!")

# Define the random character command handler
def random_character(update, context):
    characters = ['Goku', 'Vegeta', 'Piccolo', 'Gohan', 'Krillin', 'Bulma']
    random_character = random.choice(characters)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Random Character: {random_character}")

# Create an instance of the Updater class and pass your bot's token
updater = Updater(token='6568177612:AAHLoaVTwylfFl1QVyTET1oFreZBAYZWx8A', use_context=True)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Register the command handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('randomcharacter', random_character))

# Start polling for updates from Telegram
updater.start_polling()