# chatbot_Clima
Chatbot que pode ser acessado pelo Telegram, com o objetivo de retornar a previsão do tempo. <br>

## Pré-requisitos
- Python 3
- Necessario instalar as bibliotecas pelo terminal, com os comandos:
    - pip install pyTelegramBotAPI==3.8.1
    - pip install requests
- Token para API do [OpenWeatherMap](https://openweathermap.org/api)
- Para versão do Telegram: Gerar token pelo [BotFather](https://web.telegram.org/#/im?p=@BotFather)

## Iniciando o programa
Basta rodar o arquivo <b>botclima.py</b>.
Não esqueça de, antes disso, inserir a cidade e os tokens necessarios no arquivo <b>entradas.py</b>. A cidade que está como defalut é Brasilia.

## Menu de informaçoes principais
Segue o menu de informaçõs presentes no BOT, para a cidade escolhida:
    menu = """
    Ola eu sou o BotClima! Seu assistente para verificar informacoes sobre o clima.
    Favor, clique nos itens abaixo para obter informações!
    <b>/info1 - Temperatura
    /info2 - Tempo
    /info3 - Sensacao Termica
    /info4 - Minima e Maxima
    /info5 - Umidade
    /info6 - Nascer e Por do sol
    /info7 - Previsao para 8 dias
    /info8 - Alertas
    Favor escolha um dos itens"""<b>
