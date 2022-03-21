#modules
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

#key
updater = Updater("Key",
                  use_context=True)


#start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello, Welcome to the Bot. Please write\
        /help to see the commands available.")


#help
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /Class - Class Menu.
    /About - About.
    /disclaimer - Disclaimer.""")


#disclaimer
def disclaimer(update: Update, context: CallbackContext):
    update.message.reply_text(
        """ This bot/project is not affiliated by the NCERT or CBSE. This bot/project uses direct links of ncert from their website as it is. The source code is public i.e this is a non-profit open source project. To find the code visit Github."""
    )


#class
def Class(update: Update, context: CallbackContext):
    update.message.reply_text("""Select Your Class :-
    /nine - CLASS 9.
    /ten - CLASS 10.
    /ele - CLASS 11.
    /twe - CLASS 12.""")

#ninemenu
def nine(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /iebe1 - Beehive.
    /iemo1 - Moments(Supplymentary).
    /ihks1 - Kshitij.
    /ihkr1 - Kritika
    /iemh1 - Maths.
    /iesc1 - Science
    /iess4 - Civics
    /iess1 - Geography
    /iess3 - History
    /iict1 - Information & Technology""")

#tenthmenu
def ten(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /jeff1 - Beehive.
    /jefp1 - Moments(Supplymentary).
    /jhks1 - Kshitij.
    /jhkr1 - Kritika
    /jemh1 - Maths.
    /jesc1 - Science
    /jess4 - Civics
    /jess1 - Geography
    /jess3 - History.""")

#elevenmenu
def ele(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /SciencePCMB.
    /Commerce.
    /Arts.""")


#
#Nine
def ihkr1(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "ihkr1dd.zip")

def iebe1(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "iebe1dd.zip")    

def iemo1(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "iemo1dd.zip")

def ihks1(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "ihks1dd.zip")

def iess4(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "iess4dd.zip")

def iess1(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "iess1dd.zip")

def iict1(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "iict1dd.zip")

#unavaialbe
#unavaialbe
#unavaialbe
def iemh1(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "iemh1dd.zip")

def iesc1(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "iesc1dd.zip")

def iess3(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "iess3dd.zip")



#10th

#notworking maths jemh1
def jemh1(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "jemh1dd.zip")

#notworking science jesc1
def jesc1(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "jesc1dd.zip")

def jeff1(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "jeff1dd.zip")

def jefp1(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "jefp1dd.zip")

def jess1(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "jess1dd.zip")

def jess2(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "jess2dd.zip")

#notworking history jess3
def jess3(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "jess3dd.zip")

def jess4(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "jess4dd.zip")

def jhks1(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "jhks1dd.zip")

def jhkr1(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "jhkr1dd.zip")




#class 11th
def SciencePCMB(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /kech1dd Chemistry1.
    /kech2dd Chemistry2.
    /kemh1dd Maths.
    /keph1dd Physics1.
    /keph2dd Physics2.
    /kecs1dd Computer Science.
    """)

def kech1dd(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "kech1dd.zip")


def kech2dd(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "kech2dd.zip")


def kemh1dd(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "kemh1dd.zip")


def keph1dd(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "keph1dd.zip")

def keph2dd(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "keph2dd.zip")


def kebo1dd(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "kebo1dd.zip")


def kecs1dd(update, context):
    update.message.reply_text("Downloading your pdf book file.")
    context.bot.sendDocument(update.effective_chat.id,
                             "kecs1dd.zip")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" %
                              update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" %
                              update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('Class', Class))
updater.dispatcher.add_handler(CommandHandler('help', help))

#9th
updater.dispatcher.add_handler(CommandHandler('iesc1', iesc1))
updater.dispatcher.add_handler(CommandHandler('iemh1', iemh1))
updater.dispatcher.add_handler(CommandHandler('iess4', iess4))
updater.dispatcher.add_handler(CommandHandler('iess1', iess1))
updater.dispatcher.add_handler(CommandHandler('iess3', iess3))
updater.dispatcher.add_handler(CommandHandler('iict1', iict1))
updater.dispatcher.add_handler(CommandHandler('iebe1', iebe1))
updater.dispatcher.add_handler(CommandHandler('iemo1', iemo1))
updater.dispatcher.add_handler(CommandHandler('ihkr1', ihkr1))
updater.dispatcher.add_handler(CommandHandler('ihks1', ihks1))

#10th
updater.dispatcher.add_handler(CommandHandler('jesc1', jesc1))
updater.dispatcher.add_handler(CommandHandler('jefp1', jefp1))
updater.dispatcher.add_handler(CommandHandler('jeff1', jeff1))
updater.dispatcher.add_handler(CommandHandler('jemh1', jemh1))
updater.dispatcher.add_handler(CommandHandler('jess4', jess4))
updater.dispatcher.add_handler(CommandHandler('jess1', jess1))
updater.dispatcher.add_handler(CommandHandler('jess3', jess3))
updater.dispatcher.add_handler(CommandHandler('jess2', jess2))
updater.dispatcher.add_handler(CommandHandler('jhkr1', jhkr1))
updater.dispatcher.add_handler(CommandHandler('jhks1', jhks1))




updater.dispatcher.add_handler(CommandHandler('ten', ten))
updater.dispatcher.add_handler(CommandHandler('ele', ele))
updater.dispatcher.add_handler(CommandHandler('nine', nine))
updater.dispatcher.add_handler(CommandHandler('disclaimer', disclaimer))

#messageignore
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
updater.start_polling()
