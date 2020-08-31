from user_info.user_info import forwarding_list_of_all_users
from tools.callbecks_helper import (
    create_users_variables_in_forwarding_list_of_all_users,
    forward_message_for_chat, 
    search_chat_with_this_title, 
    get_forward_list,
    get_waiting_list,
    prettify_forward_list,
    execute_if_bot_are_new_member,
    execute_if_user_have_forward_list)


start_text = (
"""Hello World, I'm forward_bot!
I will help you forward your messages to many groups and channels at once.
Type /help to see how make it.""")


help_text = (
"""To forward your messages you should put your chats in the "forward list". and so, send me a message that you want forward. 

For see which chats are in the "forward list" type /show.

For add a chat you should use the /add command and next add the bot in your chat.

If you want remove a chat of your list you can use the /remove command.

this are the syntax of commands:

/add Chat_Title
/remove Chat_Title
""")


def start(update, context):
    user = update.effective_user
    create_users_variables_in_forwarding_list_of_all_users(user)
    update.message.reply_text(start_text)


def help_message(update, context):
    user = update.effective_user
    update.message.reply_text(help_text)


def add_chat_to_waiting_list (user, title):
    get_waiting_list(user).append(title)

    
def add_chat_to_forward_list (user, chat):
    get_forward_list(user).append(chat)


def remove_chat_to_forward_list (user, chat):
    get_forward_list(user).remove(chat)
    chat.leave()


def remove_chat_to_waiting_list (user, title):
    get_waiting_list(user).remove(title)


def add_group_title_to_waiting_list(update, context):
    user = update.effective_user
    create_users_variables_in_forwarding_list_of_all_users(user)
    title = " ".join(context.args)
    add_chat_to_waiting_list(user, title)
    text = "Chat title stored, for end this process, add this bot as a member of your chat"
    update.message.reply_text(text)


@execute_if_user_have_forward_list
def remove_group_to_forward_list (update, context):
    user = update.effective_user
    title = " ".join(context.args)
    forward_list = get_forward_list(user) 
    chat = search_chat_with_this_title(forward_list, title)
    if chat == None:
        text = (

""" This chat title is not on your forward list.
Type \show to see what on it""") 

    else:
        remove_chat_to_forward_list(user, chat)
        text = "Chat removed, i'm left this chat now"
    update.message.reply_text(text)


@execute_if_user_have_forward_list
def view_forward_list (update, context):
    user = update.effective_user
    forward_list = get_forward_list(user)
    forward_list_formated = prettify_forward_list(forward_list)
    text = "this are the groups in forward list:" + forward_list_formated
    update.message.reply_text(text, parse_mode="Markdown")


@execute_if_user_have_forward_list
def forward_message_for_all_chats_in_forward_list( update, context):
    user = update.effective_user
    forward_list = get_forward_list(user)
    forward_list_formated = prettify_forward_list(forward_list)
    text = "Forwarding message for:" + forward_list_formated
    for chat in forward_list:
        forward_message_for_chat (update, context, chat.id)
    update.message.reply_text(text, parse_mode="Markdown")


@execute_if_bot_are_new_member
def add_group_to_forward_list(update, context):
    user = update.effective_user
    chat = update.effective_chat
    add_chat_to_forward_list(user, chat)
    remove_chat_to_waiting_list(user, chat.title)
    text = "*" + chat.title + "*" + " added to forward list"
    user.send_message(text, parse_mode="Markdown")


