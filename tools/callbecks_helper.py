from user_info.user_info import forwarding_list_of_all_users


def get_forward_list(user):
    user_id_in_str = str(user.id)
    forward_list = forwarding_list_of_all_users[
        user_id_in_str]["forward_list"]
    return forward_list


def get_waiting_list(user):
    user_id_in_str = str(user.id)
    waiting_list = forwarding_list_of_all_users[
        user_id_in_str]["title_of_chats_waiting_to_be_added"]
    return waiting_list 



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
        result += "*" + chat.title + "*\n"
    return result


def user_have_forward_list(user):
    user_id_in_str = str(user.id)
    return user_id_in_str in forwarding_list_of_all_users


def forward_list_is_empy(user):
    if user_have_forward_list(user):
        return not bool(get_forward_list(user))
    else: return True


def execute_if_user_have_forward_list(callback):
    def execute_if_user_have_forward_list_and_reply_to_user (update, context):
        user = update.effective_user
        if not forward_list_is_empy(user):
            callback(update, context)
        else:
            text = (

"""You don't have a forwarding list yet.
Call the /start command to see how use this bot""")

            update.message.reply_text(text) 


    return execute_if_user_have_forward_list_and_reply_to_user


def execute_if_bot_are_new_member(callback):
    def get_users_ids(users):
        users_ids = list(
            map( (lambda user : user.id), users) )
        return users_ids


    def execute_if_bot_are_in_new_members_list (update, context):
        bot_id = context.bot.id
        message = update.message
        if bot_id in get_users_ids(message.new_chat_members):
            callback(update, context)
        else: return


    return execute_if_bot_are_in_new_members_list 


