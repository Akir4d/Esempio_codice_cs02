import http.client

host = input("Inserisci host/IP del sitema target: ")
port = input("Inserisci la porta del sistema target (default:80): ")
path = input("Inserisci il percorso (default:/): ")

if (port == ""): port = 80
if (path == ""): path = '/'

try:
    c = http.client.HTTPConnection(host, port)
    c.request('OPTIONS', path)
    r = c.getresponse()
    allow = r.getheader("Allow")
    if allow:
        print("I metodi abilitati sono: ", allow)
        # print("Questi sono gli headers:\n", r.headers, sep="")
    else:
        print("Non trovo i metodi, questi sono gli headers:\n", r.headers, sep="")
    c.close()
except ConnectionRefusedError:
    print("Connessione fallita")