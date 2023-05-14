import requests
import PySimpleGUI as sg
import pytz
from datetime import datetime
#plus plus fazer um monitoramenro de tempo
def tela():
    sg.theme('Black')
    layout = [
        [sg.Text('Digite sua cidade: '),sg.Input(key='sua_cidade',size=(15,15)),sg.Button('Buscar',key='Buscar')],
        [sg.Text('Hora local: '),sg.Text('',key='hora_local')],
        [sg.Text('Cidade: '),sg.Text('',key='cidade')],
        [sg.Text('Situação: '),sg.Text('',key='situacao')],
        [sg.Text('Temperatura atual: '),sg.Text('',key='temp_atual')],
        [sg.Text('Temperatura ambiente: '),sg.Text('',key='temp_amb')],
        [sg.Text('Pressão: '),sg.Text('',key='pressao')],
        [sg.Text('Umidade: '),sg.Text('',key='umidade')],
        [sg.Text('Vento: '),sg.Text('',key='vento')],
        [sg.Text('Temperatura mínima: '),sg.Text('',key='temp_min')],
        [sg.Text('Temperatura máxima: '),sg.Text('',key='temp_max')]

    ]
    return sg.Window('Tempo',layout=layout,finalize=True,font='Verdana',text_justification='c')
janela = tela()
while True:
    window,event,values = sg.read_all_windows()

    if event == 'Buscar':
        api_key = '782fd87d9dcc0da4421edb95c7f0ee0c'
        try:
            link = f"""https://api.openweathermap.org/data/2.5/weather?q={values['sua_cidade']}&appid={api_key}&lang=pt_br"""
            requisicao = requests.get(link)
            requisicao_dic = requisicao.json() 
            descricao = requisicao_dic['weather'][0]['description']
            temperatura = requisicao_dic['main']['temp']
            cidade = requisicao_dic['name']
            pais_codigo = requisicao_dic['sys']['country']
            feels_like = requisicao_dic['main']['feels_like']
            temp_min = requisicao_dic['main']['temp_min']
            temp_max = requisicao_dic['main']['temp_max']
            pressure = requisicao_dic['main']['pressure']
            humidity = requisicao_dic['main']['humidity']
            speed = requisicao_dic['wind']['speed']
            graus = requisicao_dic['wind']['deg']
            zona_fuso = pytz.country_timezones(pais_codigo)
            zona = pytz.timezone(zona_fuso[0])
            zonas_horas = datetime.now(zona)
            zonas_horas = zonas_horas.strftime("%d/%m/%Y - %H:%M:%S")
        except:
            sg.popup('Cidade não encontrada!')
            continue


        window['cidade'].update(f'{cidade}/{pais_codigo}')
        window['situacao'].update(descricao)
        window['temp_atual'].update(int(temperatura) - 273)
        window['temp_amb'].update(int(feels_like) - 273)
        window['temp_max'].update(int(temp_max) - 273)
        window['temp_min'].update(int(temp_min) - 273)
        window['pressao'].update(pressure)
        window['umidade'].update(humidity)
        window['vento'].update(f'{speed}/{graus}')
        window['hora_local'].update(zonas_horas)
        

    elif event == sg.WIN_CLOSED:
        break



