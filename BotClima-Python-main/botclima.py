#instalar no terminal-  pip install requests
import requests
import telebot
import json
import datetime 
from entradas import *


#Conexao com o TELEGRAM 
bot = telebot.TeleBot(TOKEN_TELEGRAM)


#Busca dados para a cidade escolhida.
API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_TOKEN}&lang=pt_br"
requisicao = requests.get(API_URL)
req_dicionario = requisicao.json()
    
lon = req_dicionario['coord']['lon']
lat = req_dicionario['coord']['lat']
temperatura = int(req_dicionario['main']['temp'] - 273.15)
descricao = req_dicionario['weather'][0]['description']
sensacao_termica = int(req_dicionario['main']['feels_like'] - 273.15)
temperatura_min = int(req_dicionario['main']['temp_min'] - 273.15)
temperatura_max = int(req_dicionario['main']['temp_max'] - 273.15)
umidade = req_dicionario['main']['humidity']
epoch_nascer_do_sol = req_dicionario['sys']['sunrise']
nascer_do_sol = datetime.datetime.fromtimestamp( epoch_nascer_do_sol )
epoch_por_do_sol = req_dicionario['sys']['sunset']
por_do_sol = datetime.datetime.fromtimestamp( epoch_por_do_sol )


#trata info 1 - temperatura
@bot.message_handler(commands=["info1"])
def info1(mensagem):
    bot.send_message(mensagem.chat.id, f'Em {cidade} atualmente está fazendo {temperatura}ºC')

#trata info 2 - descreve tempo
@bot.message_handler(commands=["info2"])
def info2(mensagem):
    bot.send_message(mensagem.chat.id, f'Em {cidade} o tempo está {descricao}')

#trata info 3 - sensacao termica
@bot.message_handler(commands=["info3"])
def info3(mensagem):
    bot.send_message(mensagem.chat.id, f'Em {cidade} a sensacao termica está em {sensacao_termica}ºC')


#trata info 4 - temperaturas minima e maxima
@bot.message_handler(commands=["info4"])
def info4(mensagem):
    bot.send_message(mensagem.chat.id, f'Em {cidade} a temperatura minima esta em {temperatura_min}ºC e a temperatura maxima esta em {temperatura_max}ºC')


#trata info 5 - umidade
@bot.message_handler(commands=["info5"])
def info5(mensagem):
    bot.send_message(mensagem.chat.id, f'Em {cidade} a umidade do ar esta em {umidade}%')

#trata info 6 - nascer e por do sol
@bot.message_handler(commands=["info6"])
def info6(mensagem):
    bot.send_message(mensagem.chat.id, f'Nascer do Sol: {nascer_do_sol} - Por do Sol: {por_do_sol}')


#trata info 7 - Previsao para 8 dias
@bot.message_handler(commands=["info7"])
def info7(mensagem):
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly,alerts&appid={API_TOKEN}&lang=pt_br"
    requisicao = requests.get(url)
    req_dicionario = requisicao.json()
    iRESPONSE = requests.request("GET", url)
    iRETORNO_REQ = json.loads(iRESPONSE.text)
    for i in req_dicionario['daily']:
        iEPOCH_DATA = i['dt']
        iDATA = datetime.datetime.fromtimestamp( iEPOCH_DATA )
        iTEMPERATURA = int(i["temp"]["day"] - 273.15)
        iDESCRICAO = i["weather"][0]["description"]
        tempo_futuro = f'Em {iDATA} - temperatura de {iTEMPERATURA}ºC - Tempo: {iDESCRICAO}'
        bot.send_message(mensagem.chat.id, tempo_futuro)

#trata info 8 - Alertas
@bot.message_handler(commands=["info8"])
def info8(mensagem):
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly,daily&appid={API_TOKEN}&lang=pt_br"
    requisicao = requests.get(url)
    req_dicionario = requisicao.json()
    instituto = req_dicionario['alerts'][0]['sender_name']
    alerta = req_dicionario['alerts'][0]['description']
    bot.send_message(mensagem.chat.id, f'Em {cidade} - {instituto} - {alerta}')



#funcao para responder a qualquer mensagem nao tratada
def padrao(mensagem):
    return True

@bot.message_handler(func=padrao)
def responder(mensagem):
    menu = """
    Ola eu sou o BotClima! Seu assistente para verificar informacoes sobre o clima.
    Favor, clique nos itens abaixo para obter informações!
    /info1 - Temperatura
    /info2 - Tempo
    /info3 - Sensacao Termica
    /info4 - Minima e Maxima
    /info5 - Umidade
    /info6 - Nascer e Por do sol
    /info7 - Previsao para 8 dias
    /info8 - Alertas
    Favor escolha um dos itens"""
    bot.reply_to(mensagem, menu)


bot.polling()



