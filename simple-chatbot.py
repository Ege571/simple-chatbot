import json
import random

with open("yanıtlar.json", "r", encoding="utf-8") as f:
    yanıtlar = json.load(f)

def temizle(text):
    return text.lower().strip()

def yanıt_al(user_input, yanıtlar):
    for key in yanıtlar:
        if key in user_input:
            return random.choice(yanıtlar[key])

def chat_bot():
    print("Chatbot'a Hoşgeldin (çıkmak için kapat yazınız)")

    while True:
        user_input = input("Sen: ")
        user_input = temizle(user_input)

        if user_input == "kapat":
            print("program kapatılıyor")
            break

        cevaplar = yanıt_al(user_input, yanıtlar)

        if cevaplar is None:
           print("bu kelimeyi bilmiyorum öğretmek ister misin?(evet/hayır)")
           secim = input("Sen: ").lower()

           if secim == "evet":

               yeni_cevaplar = input("Bot: peki böyle bir durumda ne demeliyim: ")

               yanıtlar[user_input] = [yeni_cevaplar]

               with open("yanıtlar.json", "w", encoding="utf-8") as f:
                json.dump(yanıtlar, f, ensure_ascii=False, indent=2)   

                print("Bot: bunu öğrendim teşekkürler")
           else:
               print("Bot: tamamdır")
        else:
            print("Bot: ", cevaplar)
if __name__ == "__main__":
    chat_bot()           