import json
from difflib import get_close_matches


def veritabani_yukle():
    with open('database.json', 'r') as dosya:
        return json.load(dosya)


def veri_yaz(veriler):
    with open('database.json', 'w') as dosya:
        json.dump(veriler, dosya, indent=2)


def yakin_eslesen_soru_bul(soru, sorular):
    eslesenler = get_close_matches(soru, sorular, n=1, cutoff=0.6)
    return eslesenler[0] if eslesenler else None


def cevap_bul(soru, veritabani):
    for s_cevap in veritabani["sorular"]:
        if s_cevap["soru"] == soru:
            return s_cevap["cevap"]
    return None


def chat_bot():
    veritabani = veritabani_yukle()

    while True:
        soru = input("Siz: ")

        if soru == "kapat":
            break

        gelen_soru = yakin_eslesen_soru_bul(soru, [s_cevap["soru"] for s_cevap in veritabani["sorular"]])

        if gelen_soru:
            cevap = cevap_bul(gelen_soru, veritabani)
            print(f"Bot: {cevap}")
        else:
            print("Bot: Bunu nasıl cevaplayacağımı bilmiyorum")
            yeni_cevap = input(print("Öğretmek isterseniz yazın veya 'geç' diyebilirsiniz."))

            if yeni_cevap != 'geç':
                veritabani["sorular"].append({
                    "soru": soru,
                    "cevap": yeni_cevap
                })
                veri_yaz(veritabani)
                print("Bot : Teşekkürler, bunu unutmayacağım")


if __name__ == '__main__':
    chat_bot()
