from googletrans import Translator

trans = Translator()
t = trans.translate(
'Bom dia para você', src= 'pt', dest='de'
)
print(f'{t.origin} -> {t.text}')