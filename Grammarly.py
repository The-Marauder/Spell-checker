from textblob import TextBlob
a = input("Type out anything and I will fix any errors with the sentence.")
input = TextBlob(a)

b = input.correct()
print(b)