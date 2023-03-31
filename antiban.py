import telegram
from telegram.ext import Updater

# Create a bot object using your bot token
bot = telegram.Bot(token='YOUR_BOT_TOKEN')

# Create an updater object to handle updates from the bot
updater = Updater(token='YOUR_BOT_TOKEN')

# Define a function to restrict a user's actions in the channel
def prevent_reports(update, context):
    # Get the chat ID and user ID from the update object
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id

    # Use the restrictChatMember method to prevent the user from reporting messages
    bot.restrict_chat_member(chat_id=chat_id, user_id=user_id, can_report_messages=False)

# Register the prevent_reports function with the updater object
updater.dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.all, prevent_reports))

# Start the bot
updater.start_polling()

FREE
