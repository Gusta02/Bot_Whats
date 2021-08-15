from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        self.mensagem = "Mensagem de Teste"
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.grupos = ["Teste bot", "Teste bot2"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(15)
        for grupo in self.grupos:
            campo_grupo = self.driver.find_element_by_xpath(
                f"//span[@title='{grupo}']")
            time.sleep(3)
            campo_grupo.click()
            chat_box = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(4)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(3)


bot = WhatsappBot()
bot.EnviarMensagens()