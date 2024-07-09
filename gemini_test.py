import google.generativeai as genai
import configparser

def get_secret_value(section, key, file_name='secret.ini'):
    config = configparser.ConfigParser()
    config.read(file_name)
    
    if section in config and key in config[section]:
        return config[section][key]
    else:
        raise KeyError(f"The key '{key}' not found in section '{section}'")

class callBot:
    '''
    CALL BOT!
    '''
    def __init__(self) -> None:
        self.GEMINI_API_KEY = get_secret_value('DEFAULT', 'GEMINI_API_KEY')
        genai.configure(api_key=self.GEMINI_API_KEY)

        self.history = dict()
        self.model = genai.GenerativeModel('gemini-pro')

    def chat(self, msg:str, ID:str) -> str:
        '''
        chat with gemini, return gemini's answer.
        msg(str): user's message
        ID(str): user's identifier, ex)Phone Number
        '''

        if ID not in self.history:
            self.history[ID] = []

        model = genai.GenerativeModel('gemini-pro')
        chat = model.start_chat(history=self.history[ID])

        res = chat.send_message(msg)
        self.history[ID] = chat.history

        return res.text