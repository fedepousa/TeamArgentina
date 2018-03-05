import time
from selenium import webdriver

def sendMessage(user, message):    
    
    # Abre una instancia de Chrome con mi perfil Default (en el cual ya esta loggueado chess.com)
    options = webdriver.ChromeOptions() 
    options.add_argument("user-data-dir=/home/federico/.config/google-chrome/Default") #Path to your chrome profile
    driver = webdriver.Chrome(executable_path='/home/federico/Desktop/Fede/chesscom/chromedriver', chrome_options=options)


    # Entra a la url del usuario que se le quiere mandar un mensaje
    driver.get('https://www.chess.com/member/'+user)
    
    # Se espera a que cargue la web (forma artesanal, seguro hay que cambiar esto)
    time.sleep(2)
    
    # Se busca el primer icono que se llama "iconized" que en la interfaz actual es el boton para mandar un mensaje personal
    nuevo = driver.find_element_by_class_name("iconized")
    
    # Se clickea en el boton para mandar mensaje personal
    nuevo.click()


    # Se espera a que cargue la interfaz para mandar mensaje y se manda por teclado el mensaje que se quiere escribir
    actions = webdriver.ActionChains(driver)
    time.sleep(2)
    actions.send_keys(message)
    actions.perform()

    # Se busca el boton para enviar el mensaje y se lo clickea
    boton = driver.find_element_by_class_name("btn")
    boton.click()


    time.sleep(2)
    driver.quit()


# Codigo de prueba para mandar un mensaje a un usuario especifico
user = 'fedebau'
message = 'Mensaje de prueba enviado automaticamente'
sendMessage(user, message)


