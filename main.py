# REQ:
# pip install googletrans==4.0.0-rc1

from googletrans import Translator

translator = Translator()


def translate_text(text, dest="en"):
    return translator.translate(text, dest=dest).text


print(translate_text("Merhaba dünya", "en"))    # OUTPUT : Hello world
print(translate_text("Hello world", "tr"))      # OUTPUT : Merhaba dünya
