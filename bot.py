from user_info.user_info import token
from telegram.ext import Updater
from handlers import (
    start_command,
    show_list_command,
    add_title_to_waiting_list_command, 
    remove_group_to_forward_list_command,
    bot_added_to_group_handler,
    forward_handler)


def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher


    dp.add_handler(start_command)
    dp.add_handler(show_list_command)
    dp.add_handler(add_title_to_waiting_list_command)
    dp.add_handler(remove_group_to_forward_list_command)
    dp.add_handler(bot_added_to_group_handler)
    dp.add_handler(forward_handler)


    print("\nbot started")
    updater.start_polling()
    updater.idle()
    print("\nbot endded")


if __name__ == '__main__':
    main()


