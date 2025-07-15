premena = "Erik" #globalna premena

def hello():
    global premena
    premena = "Adam" #lokalna premena
    print(premena)


hello()

print(premena)
