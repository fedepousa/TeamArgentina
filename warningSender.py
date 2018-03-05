import time
import urllib, json
import StringIO
import re
from selenium import webdriver


# Mismo codigo que messageSender para enviar un mensaje a un usuario especifico
def sendMessage(user, message):    
    options = webdriver.ChromeOptions() 
    options.add_argument("user-data-dir=/home/federico/.config/google-chrome/Default") #Path to your chrome profile
    driver = webdriver.Chrome(executable_path='/home/federico/Desktop/Fede/chesscom/chromedriver', chrome_options=options)


    

    driver.get('https://www.chess.com/member/'+user)
    time.sleep(1);
    nuevo = driver.find_element_by_class_name("iconized")
    nuevo.click()


    actions = webdriver.ActionChains(driver)
    time.sleep(1)
    actions.send_keys(message)
    actions.perform()

    boton = driver.find_element_by_class_name("btn")
    boton.click()


    time.sleep(2)
    driver.quit()


# Iteracion boba para mandar mensajes a una lista de usuarios
def sendMessages(users, message):
    for user in users:
        sendMessage(user, message)


# Funcion para chequear un match especifico
# Actualmente esta funcion solo imprime el nombre del jugador, la idea seria retornar todos los jugadores en una lista para luego usar la funcion sendMessages
def matchChecker(matchNumber):
    
    # Traigo a los argentinos para reconocerlos
    response = urllib.urlopen('https://api.chess.com/pub/club/team-argentina/members')
    data = json.loads(response.read())
    argentinos = data["weekly"]+data["monthly"]+data["all_time"]
    
    # Traigo la cantidad de tableros
    response = urllib.urlopen('https://api.chess.com/pub/match/'+matchNumber)
    data = json.loads(response.read())
    tableros = data["boards"]
    
    # Chequeo cada tablero
    for i in xrange(tableros):
        response = urllib.urlopen('https://api.chess.com/pub/match/'+matchNumber+"/"+str(i+1))
        data = json.loads(response.read())
        apurado = False
        jugadorArgentino = ''
        for game in data["games"]:
            if "turn" in game:
                whosTurn = game[game["turn"]].split("/")[-1]
                if whosTurn in argentinos:
                    if "move_by" in game:
                        timeLeft = game["move_by"]-time.time()
                        if timeLeft > 0 and timeLeft < 25*3600:
                            apurado = True
                            jugadorArgentino = whosTurn 
        if apurado:
            print jugadorArgentino

# Se chequea un match especifico
matchChecker('862300')


