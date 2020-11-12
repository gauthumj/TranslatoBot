from TranslatoBot import translato
from googletrans import Translator

translator = Translator()

update_id = None
bot = translato('config.cfg')

def make_reply(msg):
    reply = None
    if msg is not None:
        # reply = ts.deepl(msg)
        reply = translator.translate(msg).text
    return reply

while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply,from_)