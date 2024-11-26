import pyttsx3
from deep_translator import GoogleTranslator


def traduzir_ingles_para_portugues(texto_ingles):
    traducao = GoogleTranslator(source='en', target='pt').translate(texto_ingles)
    return traducao


def cantar_musica(traducao):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150) 
    engine.setProperty('volume', 1)  
    engine.say(traducao)  
    engine.runAndWait()


def cantar_musica_em_portugues(letra_ingles):
    print("Traduzindo a letra para o português...")
    letra_traduzida = traduzir_ingles_para_portugues(letra_ingles)
    print("Letra traduzida:")
    print(letra_traduzida)
    print("\nCANTANDO A MÚSICA...")
    cantar_musica(letra_traduzida)


letra_ingles = """
slow dance in the burning room
"""


cantar_musica_em_portugues(letra_ingles)


