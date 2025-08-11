import time
from datetime import datetime

def reminder_bot():
    while True:
        # Get the current time
        now = datetime.now()
        current_hour = now.hour
        current_minute = now.minute
        
        # Check if it's 8 PM (20:00)
        if current_hour == 20 and current_minute == 0:
            print("It's 8 PM! Time to do your task!")
            # Wait for a minute so the bot doesn't repeatedly send reminders in the same minute
            time.sleep(60)
        else:
            # Check again after 30 seconds
            time.sleep(30)

# Start the reminder bot
reminder_bot()
