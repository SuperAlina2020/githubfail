string = input()
sos1 = "help"
sos2 = "asap"
sos3 = "urgent"

if string.isupper() or string.endswith('!!!') or sos1 in string or sos2 in string or sos3 in string:
    print("To Steven")


