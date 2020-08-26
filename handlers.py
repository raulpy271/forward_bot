import logging


logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s : \n %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    logger.info("started")
    update.message.reply_text('Hi!')


def unauthorized_access(update, context):
    text = "Você não tem acesso a esse bot!"
    update.message.reply_text(text)


def reply_user_id(update, context):
    user = update.effective_user
    text = "seu id é: " + str(user.id)
    update.message.reply_text(text)


def add_chat_id_to_forward_list(bot, chat_id):
    bot.forward_list.append(chat_id)


def add_this_group_to_forward_list(update, context):
    chat = update.effective_chat
    add_chat_id_to_forward_list(context.bot, chat.id)
    logger.info(str(chat.id) + " has added to forward list")


def view_forward_list (update, context):
    forward_list = context.bot.forward_list
    text = "this are the groups in forward list:\n" + str(forward_list)
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
    for chat_id in list_of_chats:
        forward_message_for_chat (update, context, chat_id)

