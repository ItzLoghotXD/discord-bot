from bot import bot
from config import LOGGER

import os
import sys

def check_bot_token():
    if "DC_BOT_TOKEN" not in os.environ or not os.environ["DC_BOT_TOKEN"]:
        LOGGER(__name__).error("Environment variable 'DC_BOT_TOKEN' not set.\nPlease set up the environment variable for your bot's token.")
        bot.close
        sys.exit(1)  # Exit the script with an error code

# Call the function to check for the bot token before proceeding
check_bot_token()

# After this point, you can safely use os.environ["DC_BOT_TOKEN"] knowing it's set.

######################################################################################################

#import os
#import sys

# Check if the environment variable is set
#if "DC_BOT_TOKEN" not in os.environ:
#    LOGGER(__name__).error("Environment variable 'DC_BOT_TOKEN' not set.\nPlease set up the environment variable for your bot's token.")
#    bot.close
#    sys.exit(1)  # Exit the script with an error code

#DC_BOT_TOKEN = os.environ["DC_BOT_TOKEN"]  # Get the bot token from the environment variable
