from user_info.user_info import forwarding_list_of_all_users


def get_forward_list(user):
    user_id_in_str = str(user.id)
    forward_list = forwarding_list_of_all_users[
        user_id_in_str]["forward_list"]
    return forward_list


def forward_message_for_chat (update, context, chat_id):
    user = update.effective_user
    message = update.message
    message.forward(chat_id)


def search_chat_with_this_title(list_of_chats, title):
    for chat in list_of_chats:
        if chat.title == title:
            return chat
    return None


def create_users_variables_in_forwarding_list_of_all_users(user):
    user_id_in_str = str(user.id)
    if not user_id_in_str in forwarding_list_of_all_users:
        forwarding_list_of_all_users[user_id_in_str] = {
            "forward_list": [],
            "title_of_chats_waiting_to_be_added": []
        }


def prettify_forward_list (forward_list):
    result = "\n"
    for chat in forward_list:
        result += chat.title + "\n"
    return result


