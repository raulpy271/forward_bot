import logging


logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s : \n %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

forwarding_list_of_all_users = {
        "12345" :
        {
            "forward_list": [],
            "title_of_chats_waiting_to_be_added": []
        }
    } 

def get_forward_list(user):
    user_id_in_str = str(user.id)
    forward_list = forwarding_list_of_all_users[
        user_id_in_str]["forward_list"]
    return forward_list


def is_channel_or_group(chat):
    return chat.title != None


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


def start(update, context):
    user = update.effective_user
    create_users_variables_in_forwarding_list_of_all_users(user)
    text = "I'm forward bot"
    update.message.reply_text(text)


def unauthorized_access(update, context):
    text = "you don't have access to this bot!"
    update.message.reply_text(text)


def reply_user_id(update, context):
    user = update.effective_user
    text = "your id is: " + str(user.id)
    text = text + "\n\n" + str(forwarding_list_of_all_users)
    update.message.reply_text(text)


def add_chat_to_waiting_list (user, title):
    user_id_in_str = str(user.id)
    (forwarding_list_of_all_users[user_id_in_str][
        "title_of_chats_waiting_to_be_added"]).append(title)
    


def add_chat_to_forward_list (user, chat):
    user_id_in_str = str(user.id)
    (forwarding_list_of_all_users[user_id_in_str][
        "forward_list"]).append(chat)


def remove_chat_to_forward_list (user, chat):
    user_id_in_str = str(user.id)
    (forwarding_list_of_all_users[user_id_in_str][
        "forward_list"]).remove(chat)
    chat.leave()


def remove_chat_to_waiting_list (user, title):
    user_id_in_str = str(user.id)
    (forwarding_list_of_all_users[user_id_in_str][
        "title_of_chats_waiting_to_be_added"]).remove(title)



def add_group_title_to_waiting_list(update, context):
    user = update.effective_user
    user_id_in_str = str(user.id)
    if not user_id_in_str in forwarding_list_of_all_users:
        create_users_variables_in_forwarding_list_of_all_users(user)
    title = " ".join(context.args)
    add_chat_to_waiting_list(user, title)
    text = "Link stored, for end this process, add this bot in your chat"
    update.message.reply_text(text)
    



def remove_group_to_forward_list (update, context):
    user = update.effective_user
    title = " ".join(context.args)
    user_id_in_str = str(user.id)
    if user_id_in_str in forwarding_list_of_all_users:
        forward_list = forwarding_list_of_all_users[
            user_id_in_str][ "forward_list"]
        chat = search_chat_with_this_title(forward_list, title)
        if chat == None:
            text = "Invalid Link or this link not in the list"
        else:
            remove_chat_to_forward_list(user, chat)
            text = "Chat removed, i'm left this chat now"
    else:
        text = """You don't have a forwarding list yet. 
            Call the /start command to see how use this bot"""
    update.message.reply_text(text)



def view_forward_list (update, context):
    user = update.effective_user
    user_id_in_str = str(user.id)
    if user_id_in_str in forwarding_list_of_all_users:
        forward_list = get_forward_list(user)
        forward_list_formated = prettify_forward_list(forward_list)
        text = "this are the groups in forward list:" + forward_list_formated
    else:
        text = """You don't have a forwarding list yet. 
            Call the /start command to see how use this bot"""
    update.message.reply_text(text)


def forward_message_for_chat (update, context, chat_id):
    user = update.effective_user
    message = update.message
    message.forward(chat_id)
    logger.info(
        "user " + str(user.id) + " sent something to: " + str(chat_id)
    )


def forward_message_for_all_chats_in_forward_list( update, context):
    user = update.effective_user
    user_id_in_str = str(user.id)
    if user_id_in_str in forwarding_list_of_all_users:
        text = "Forwarding message"
        list_of_chats = get_forward_list(user)
        for chat in list_of_chats:
            forward_message_for_chat (update, context, chat.id)
    else:
        text = """You don't have a forwarding list yet. 
            Call the /start command to see how use this bot"""
    update.message.reply_text(text)



def prettify_forward_list (forward_list):
    result = "\n"
    for chat in forward_list:
        result += chat.title + "\n"
    return result


def add_group_to_forward_list(update, context):
    user = update.effective_user
    chat = update.effective_chat
    add_chat_to_forward_list(user, chat)
    remove_chat_to_waiting_list(user, chat.title)
    text = "chat added to forward list"
    user.send_message(text)

