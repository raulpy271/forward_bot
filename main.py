from user_info import User_Info
from telegram.ext import (
    Updater, 
    BaseFilter,
    Filters,
    Handler,
    CommandHandler, 
    MessageHandler)
from handlers import (
    logger,
    start,
    view_forward_list,
    reply_user_id,
    add_group_to_forward_list, 
    forwarding_list_of_all_users,
    remove_group_to_forward_list,
    add_group_title_to_waiting_list,
    forward_message_for_all_chats_in_forward_list)


class Chat_In_Waiting_List(BaseFilter):
    def filter(self, message):
        user = message.from_user
        user_id_in_str = str(user.id)
        if not user_id_in_str in forwarding_list_of_all_users: 
            return False
        titles = forwarding_list_of_all_users[user_id_in_str][
            "title_of_chats_waiting_to_be_added"]
        return message.chat.title in titles


user_info = User_Info()
token = user_info.token


def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    bot_added_to_group_handler = MessageHandler(
        Filters.status_update.new_chat_members
        & (Chat_In_Waiting_List()),
        add_group_to_forward_list
    )
    forward_handler = MessageHandler(
        Filters.private,
        forward_message_for_all_chats_in_forward_list
    )


    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("id", reply_user_id))
    dp.add_handler(CommandHandler("show_list", view_forward_list))
    dp.add_handler(CommandHandler(
        "add", 
        add_group_title_to_waiting_list)
    )
    dp.add_handler(CommandHandler(
        "remove", 
        remove_group_to_forward_list)
    )

    dp.add_handler(bot_added_to_group_handler)
    dp.add_handler(forward_handler)

    updater.start_polling()
    updater.idle()


#if __name__ == '__main__':
#    main()

