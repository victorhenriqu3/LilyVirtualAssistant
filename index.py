import speech_recognition as sr
import pyttsx3

audio = sr.Recognizer()
lily = pyttsx3.init() 

## Dando as Boas Vindas
lily.say('Olá, sou a lily')
lily.say('Como posso te ajudar ?')
lily.runAndWait()
comando = ''

## Verificando se você quer sair ou ficar 
while comando != 'sair': 
  try:
    with sr.Microphone() as source:
      audio.adjust_for_ambient_noise(source) ## Removendo o barulho indesejado
      print('Ouvindo...')
      voz = audio.listen(source)
      try:
        comando = audio.recognize_google(voz,language='pt-BR') ## Recebendo o comando dado
        lily.say(comando)
        lily.runAndWait()
      except:
        lily.say('Não entendi ainda') ## Tratando o erro na fala
        lily.runAndWait()
        
  except:
    lily.say('Microfone não está funcionado') ## Tratando erro no microfone
    lily.runAndWait()
