import telepot
token = '1273994644:AAEfNuNNESsMGpQpDDFkWP-qUzb8VaDYtkc'
TelegramBot = telepot.Bot(token)
print (TelegramBot.getMe())

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        TelegramBot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))


TelegramBot.message_loop(handle)
