import eel
eel.init("web")


@eel.expose
def printMessage(message):
    print(message)
    return message


eel.start("index.html", size=(600, 600))
