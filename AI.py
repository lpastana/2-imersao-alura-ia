import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

class AIManager:
    def __init__(self,config,history=[]):
        self.MAIN_DIR=os.getcwd()
        self.frase_complementar="\n\nFaça minha avaliação e as sugestões de séries para assistir"
        self.api_key=os.environ.get("API-KEY")
        genai.configure(api_key=self.api_key)
        self.system_instruction =config['system_instruction']
        self.model = genai.GenerativeModel(config['model_config'],generation_config=config['general_config'],safety_settings=config['safety_config'])
        self.chat = self.model.start_chat(history=history)

    def send_message(self,message):
        response=self.chat.send_message(self.system_instruction+message+self.frase_complementar)
        print(response.text)
        return response
    
