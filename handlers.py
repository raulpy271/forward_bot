from telegram.ext import (
    Filters,
    CommandHandler, 
    MessageHandler)


from callbecks import (
    start,
    view_forward_list,
    forward_message_for_all_chats_in_forward_list,
    add_group_title_to_waiting_list,
    remove_group_to_forward_list,
    add_group_to_forward_list)

from tools.custom_filters import (
    user_have_waiting_list)


bot_added_to_group_handler = MessageHandler(
    Filters.status_update.new_chat_members
    & user_have_waiting_list,
    add_group_to_forward_list)


forward_handler = MessageHandler(
    Filters.private,
    forward_message_for_all_chats_in_forward_list)


start_command = CommandHandler("start", start)


show_list_command = CommandHandler("show", view_forward_list)


add_title_to_waiting_list_command = CommandHandler(
    "add", 
    add_group_title_to_waiting_list)


remove_group_to_forward_list_command = CommandHandler(
    "remove", 
    remove_group_to_forward_list)

