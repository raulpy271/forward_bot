import logging


logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s : \n %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)


def is_channel_or_group(chat):
    return chat.title != None


def init_forward_bot_variables_in_user(user):
    if not hasattr(user, "forward_list"):
        user.forward_list = []
        user.link_of_chats_waiting_to_be_added = []

def start(update, context):
    user = update.effective_user
    init_forward_bot_variables_in_user(user)
    text = "I'm forward bot"
    update.message.reply_text(text)


def unauthorized_access(update, context):
    text = "you don't have access to this bot!"
    update.message.reply_text(text)


def reply_user_id(update, context):
    user = update.effective_user
    text = "your id is: " + str(user.id)
    update.message.reply_text(text)


def add_chat_to_forward_list (user, chat):
    user.forward_list.append(chat)


def remove_chat_to_forward_list (user, chat):
    user.forward_list.remove(chat)
    chat.leave()



def add_this_group_to_forward_list_and_reply_the_result(update, context):
    chat = update.effective_chat
    bot = context.bot
    if is_channel_or_group(chat):
        if not chat in bot.forward_list:
            add_chat_to_forward_list(context.bot, chat)
            text = "this chat was successfully added"
        else:
            text = "this chat was already on the list"
    else:
        text = "This chat no has a group o channel"
    update.message.reply_text(text)


def remove_this_group_to_forward_list_and_reply_the_result (update, context):
    chat = update.effective_chat
    bot = context.bot
    if is_channel_or_group(chat):
        if chat in bot.forward_list:
            remove_chat_to_forward_list(context.bot, chat)
            text = "this chat was successfully removed"
        else:
            text = "this chat is not on the list"
    else:
        text = "This chat no has a group o channel"
    update.message.reply_text(text)




def view_forward_list (update, context):
    forward_list = update.effective_user.forward_list
    forward_list_formated = prettify_forward_list(forward_list)
    text = "this are the groups in forward list:" + forward_list_formated
    update.message.reply_text(text)


def forward_message_for_chat (update, context, chat_id):
    user = update.effective_user
    message = update.message
    message.forward(chat_id)
    logger.info(
        "user " + str(user.id) + " sent something to: " + str(chat_id)
    )


def forward_message_for_all_chats_in_forward_list( update, context):
    list_of_chats = context.bot.forward_list
    for chat in list_of_chats:
        forward_message_for_chat (update, context, chat.id)


def prettify_forward_list (forward_list):
    result = "\n"
    for chat in forward_list:
        result += chat.title + "\n"
    return result

def test_handler_base (update, context):
    text = "User added:" + (update.message.new_chat_members)[0].first_name
    update.message.reply_text(text)

