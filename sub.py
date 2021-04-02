import requests
import time

print('''

███████╗██╗   ██╗██████╗        ██████╗  ██╗
██╔════╝██║   ██║██╔══██╗      ██╔═████╗███║
███████╗██║   ██║██████╔╝█████╗██║██╔██║╚██║
╚════██║██║   ██║██╔══██╗╚════╝████╔╝██║ ██║
███████║╚██████╔╝██████╔╝      ╚██████╔╝ ██║
╚══════╝ ╚═════╝ ╚═════╝        ╚═════╝  ╚═╝
                                            
           INSTA ---> @D_5TR
           INSTA ---> @ZER0ONE_01
           MAKE BY ---> D5TR
           TEAM ---> ZERO ONE
''')

target = input('[*] Enter Url :')

http = int(input('[1] http | [2] https :'))

file = open(input('[*] Enter Name File :'))

sleeps = int(input('[*] Emter Sleep :'))


filez = file.readlines()

for filex in filez:
    filex = str(filex).strip()




    if http == 1:
        urls = 'http://'+filex+'.'+target

        try:

            req = requests.get(urls).status_code
            req2 = requests.post(urls).status_code
            time.sleep(sleeps)

            if req or req2 == 200 :
                print('[+] Found Url >>>',urls)

            elif req or req2 == 429:
                print('[!!] Have Band !! ')

            else:
                print('[-] Not Found !!')

        except requests.exceptions.ConnectionError:
            print('[-] Not Found !!')
            pass



    elif http == 2:
        urls = 'https://'+filex+'.'+target

        try:

            req = requests.get(urls).status_code
            req2 = requests.post(urls).status_code
            time.sleep(sleeps)

            if req or req2 == 200 :
                print('[+] Found Url >>>',urls)

            elif req or req2 == 429:
                print('[!!] Have Band !! ')

            else:
                print('[-] Not Found !!')

        except requests.exceptions.ConnectionError:
            print('[-] Not Found !!')
            pass



