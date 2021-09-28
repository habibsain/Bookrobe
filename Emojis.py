message = input("> ")
words = message.split(' ')
cap = {
    ":)":"😀",
    ":(":"☹"
}
output = ""
for word in words:
    output += cap.get(word, word) + " "
print(output)

