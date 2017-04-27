import instagramm
import re
import telepot
import telepot.helper
import datetime

from telepot.delegate import (
    per_chat_id, create_open, pave_event_space, include_callback_query_chat_id)


def new_user_hello(msg):
    try:
        chat_id = msg['chat']['id']
        user_ = msg['new_chat_member']
        bot.sendMessage(chat_id, 'Приветствуйте нового участника: {} {}'.format(user_['first_name'], user_['last_name']))
    except Exception as e:
        return "Приветствуйте нового участника"

def sender_photo(chat_id, data):
    data = data.split('||')
    if re.findall('http.*.mp4', data[0]):
        bot.sendVideo(chat_id, data[0], data[1])
    elif re.findall('http.*.jpg', data[0]):
        bot.sendPhoto(chat_id, data[0], data[1])
    else:
        bot.sendMessage(chat_id, data)

class VoteCounter(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(VoteCounter, self).__init__(*args, **kwargs)
        self._ballot_box = None
        self._keyboard_msg_ident = None
        self._editor = None
        self._expired_event = None
        self._member_count = self.administrator.getChatMembersCount() - 1  # exclude myself, the bot


    def on_chat_message(self, msg):
        content_type, from_id, chat_id = telepot.glance(msg)
        now_time = datetime.datetime.now()
        print(str(now_time.strftime("%H")))
        try:
            # if int(now_time.strftime("%H")) >= 10 and int(now_time.strftime("%H")) < 19:
            if content_type == 'new_chat_member':
                new_user_hello(msg)
            if content_type != 'text':
                print('Not a text message.')
                return
            if msg['text'] == '/boobs':
                print('boobs')
                sender_photo(chat_id, instagramm.Inst('boobs'))
                return
            if re.findall('/#.*', msg['text']):
                diez = msg['text'][3:]
                print(diez)
                sender_photo(chat_id, instagramm.Inst(diez))
            # else:
            #     sender_photo(chat_id, 'https://files5.adme.ru/files/comment/part_2036/20357060-1414483493.png')
        except Exception as e:
            sender_photo(chat_id, 'https://files5.adme.ru/files/comment/part_2036/20357060-1414483493.png')


#TOKEN = '307520552:AAHVG_Yi7nshJHUDYOIn-4G6UXEfTY7egGU'
TOKEN = '294022389:AAHVf5mAejze3naL9Q-BAXKEFHlR7Tdk7E4'

bot = telepot.DelegatorBot(TOKEN, [
    include_callback_query_chat_id(
        pave_event_space())(
            per_chat_id(types=['group']), create_open, VoteCounter, timeout=10),
])
bot.message_loop(run_forever='Listening ...')
