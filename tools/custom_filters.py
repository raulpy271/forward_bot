from telegram.ext import BaseFilter
from user_info.user_info import forwarding_list_of_all_users


class User_Have_Waiting_List (BaseFilter):
    def filter(self, message):
        user = message.from_user
        user_id_in_str = str(user.id)
        if not user_id_in_str in forwarding_list_of_all_users: 
            return False
        titles = forwarding_list_of_all_users[user_id_in_str][
            "title_of_chats_waiting_to_be_added"]
        return message.chat.title in titles


user_have_waiting_list = User_Have_Waiting_List()


