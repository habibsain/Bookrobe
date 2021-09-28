def emojise(message):
    words = message.split(' ')
    cap = {
        ":)":"😀",
        ":(":"☹"
    }
    output = ""
    for word in words:
        output += cap.get(word, word) + " "
    return output

