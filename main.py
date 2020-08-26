from user_info import User_Info
from telegram.ext import (
    Updater, CommandHandler, 
    Filters,
    MessageHandler)
from handlers import (
    logger,
    start,
    view_forward_list,
    reply_user_id,
    forward_message_for_chat,
    add_this_group_to_forward_list,
    forward_message_for_all_chats_in_forward_list)




user_info = User_Info()
token = user_info.token



def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    bot = dp.bot
    bot.forward_list = [-320128406, -463344466]
    forward_handler = MessageHandler(
        Filters.all,
        forward_message_for_all_chats_in_forward_list
    )


    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("id", reply_user_id))
    dp.add_handler(CommandHandler("add", add_this_group_to_forward_list))
    dp.add_handler(CommandHandler("view_forward_list", view_forward_list))

    dp.add_handler(forward_handler)

    updater.start_polling()
    updater.idle()


#if __name__ == '__main__':
#    main()
