from user_info import User_Info
from telegram.ext import (
    Updater, 
    Filters,
    Handler,
    CommandHandler, 
    MessageHandler)
from handlers import (
    logger,
    start,
    view_forward_list,
    reply_user_id,
    forward_message_for_chat,
    test_handler_base,
    remove_this_group_to_forward_list_and_reply_the_result,
    add_this_group_to_forward_list_and_reply_the_result,
    forward_message_for_all_chats_in_forward_list)




user_info = User_Info()
token = user_info.token


def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    added_to_group_handler = MessageHandler(
        Filters.status_update.new_chat_members, 
        test_handler_base
    )
    forward_handler = MessageHandler(
        Filters.all,
        forward_message_for_all_chats_in_forward_list
    )


    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("id", reply_user_id))
    dp.add_handler(CommandHandler("show_list", view_forward_list))
    dp.add_handler(CommandHandler(
        "add", 
        add_this_group_to_forward_list_and_reply_the_result)
    )
    dp.add_handler(CommandHandler(
        "remove", 
        remove_this_group_to_forward_list_and_reply_the_result)
    )

    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members,test_handler_base))
    dp.add_handler(forward_handler)

    updater.start_polling()
    updater.idle()


#if __name__ == '__main__':
#    main()

