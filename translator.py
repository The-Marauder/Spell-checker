from textblob import TextBlob
inputtext = input("Type anything in any language and I will translate it to whatever you prefer.")
a = TextBlob(inputtext)
print(a.detect_language())
translateinput = input("Type the language you want it translated to(use the standard 2 letter form in all smalls.) ")
print(a.translate(to=translateinput))