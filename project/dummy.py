from xbee import send

dumbdumb = ["l", "r", "r", "p", "l", "l", "r", "d"]

for c in dumbdumb:
    send(c)
    print("Sent {}".format(c))
