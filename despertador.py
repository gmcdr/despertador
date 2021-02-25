import psutil
import pyttsx3
from datetime import datetime
from playsound import playsound


horas = int(input('Digite o hora do compromisso, EX: 21,8,3 : '))
minuto =  int(input('Digie os minutos do compromisso EX: 50, 43, : '))
bate = str(input('Digite quantas horas deseja pra ser avisado, caso a bateria esteja acabando :'))
per = str(input('Digite quantos porcentos deseja para ser avisado :'))

while True:
    perR = per
    agora = datetime.now()
    hora = agora.hour
    min = agora.minute
    engine = pyttsx3.init()
    battery = psutil.sensors_battery()
    por = str(battery.percent)
    calc =  ((hora-24)+horas)*-1
    y = int(bate)

    if horas == hora and minuto == min:
        playsound('Serenity.mp3')
        break

    if calc <= y and por == perR:
        for x in range(2):
            engine.say(f'A sua bateria esta em {por} por cento, coloque pra carregar ')
            engine.runAndWait()
            break






