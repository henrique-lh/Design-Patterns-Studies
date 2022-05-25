from lib.slack import post_slack_message
from .event import subscribe

def handle_user_register(user):
    post_slack_message("sales", f"{user.name} has registered with email address {user.email}. Don't forget to spam this person!")

def setup_slack_event_handlers():
    subscribe("user_registered", handle_user_register)