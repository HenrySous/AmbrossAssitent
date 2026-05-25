import speech_recognition as sr
import pyttsx3
import os

engine = pyttsx3.init()

engine.setProperty('rate', 180)

recognizer = sr.Recognizer()

print("AMBROSS ONLINE")


def falar(texto):
    print(f"Ambross: {texto}")
    engine.say(texto)
    engine.runAndWait()


falar("Sistema operacional iniciado")

while True:
    try:
        with sr.Microphone() as source:
            print("Escutando...")

            recognizer.adjust_for_ambient_noise(source)

            audio = recognizer.listen(source)

            comando = recognizer.recognize_google(
                audio,
                language='pt-BR'
            ).lower()

            print(f"Você: {comando}")

            if "olá" in comando:
                falar("Sistema operacional")

            elif "hora" in comando:
                falar("Ainda não implementei relógio")

            elif "youtube" in comando:
                falar("Abrindo YouTube")
                os.system("am start -a android.intent.action.VIEW -d https://youtube.com")

            elif "spotify" in comando:
                falar("Abrindo Spotify")
                os.system("am start -a android.intent.action.VIEW -d https://open.spotify.com")

            elif "desligar" in comando:
                falar("Encerrando sistema")
                break

            else:
                falar("Comando desconhecido")

    except Exception as erro:
        print("Erro:", erro)
