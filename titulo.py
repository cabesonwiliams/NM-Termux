import os
import colorama
import time
from colorama import Fore
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

############### Banner ###############
banner2 = "\033[1;36m"+ """

▄████▄   ▄▄▄       ▄▄▄▄   ▓█████   ██████  ▒█████   ███▄    █      ██████  ██▓ ███▄    █    ▒███████▒
▒██▀ ▀█  ▒████▄    ▓█████▄ ▓█   ▀ ▒██    ▒ ▒██▒  ██▒ ██ ▀█   █    ▒██    ▒ ▓██▒ ██ ▀█   █    ▒ ▒ ▒ ▄▀░
▒▓█    ▄ ▒██  ▀█▄  ▒██▒ ▄██▒███   ░ ▓██▄   ▒██░  ██▒▓██  ▀█ ██▒   ░ ▓██▄   ▒██▒▓██  ▀█ ██▒   ░ ▒ ▄▀▒░
▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░█▀  ▒▓█  ▄   ▒   ██▒▒██   ██░▓██▒  ▐▌██▒     ▒   ██▒░██░▓██▒  ▐▌██▒     ▄▀▒   ░
▒ ▓███▀ ░ ▓█   ▓██▒░▓█  ▀█▓░▒████▒▒██████▒▒░ ████▓▒░▒██░   ▓██░   ▒██████▒▒░██░▒██░   ▓██░   ▒███████▒
░ ░▒ ▒  ░ ▒▒   ▓▒█░░▒▓███▀▒░░ ▒░ ░▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒    ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒    ░▒▒ ▓░▒░▒
  ░  ▒     ▒   ▒▒ ░▒░▒   ░  ░ ░  ░░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░   ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░   ░░▒ ▒ ░ ▒
░          ░   ▒    ░    ░    ░   ░  ░  ░  ░ ░ ░ ▒     ░   ░ ░    ░  ░  ░   ▒ ░   ░   ░ ░    ░ ░ ░ ░ ░
░ ░            ░  ░ ░         ░  ░      ░      ░ ░           ░          ░   ░           ░      ░ ░
░                        ░                                                                   ░


 """
banner1 = "\033[1;36m"+ """                                            

            ███╗   ██╗███╗   ███╗███████╗ ██████╗██████╗ ██╗██████╗ ████████╗
            ████╗  ██║████╗ ████║██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝
            ██╔██╗ ██║██╔████╔██║███████╗██║     ██████╔╝██║██████╔╝   ██║   
            ██║╚██╗██║██║╚██╔╝██║╚════██║██║     ██╔══██╗██║██╔═══╝    ██║   
            ██║ ╚████║██║ ╚═╝ ██║███████║╚██████╗██║  ██║██║██║        ██║   
            ╚═╝  ╚═══╝╚═╝     ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝  
"""
banner3 = "\033[1;36m"+ '''

             ███╗   ██╗███╗   ███╗███████╗ ██████╗██████╗ ██╗██████╗ ████████╗
             ████╗  ██║████╗ ████║██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝
             ██╔██╗ ██║██╔████╔██║███████╗██║     ██████╔╝██║██████╔╝   ██║   
             ██║╚██╗██║██║╚██╔╝██║╚════██║██║     ██╔══██╗██║██╔═══╝    ██║   
             ██║ ╚████║██║ ╚═╝ ██║███████║╚██████╗██║  ██║██║██║        ██║   
             ╚═╝  ╚═══╝╚═╝     ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝      

                    >>>>>>>>>>>>>>>>>>  Menu  <<<<<<<<<<<<<<<<<<

[0] Nmap help                                [00] Nmap --- Scripts

[1] Scanear 1000 puertos famosos             [11] Host activos en una red (LH)
[2] Scanear todos los puertos existentes     [12] Identidicar IP                        
[3] Escaneo de servicios estandar            [13] Confundir al firewall para que suelte datos importantes  
[4] Escaneo de servicios agreviso            [14] Utilizar señuelos                                     
[5] Scan Detallado                           [15] Detectar Firewall
[6] Scanear de OS                            [16] Deteccion de Firewall exacta  
[7] Scanear SubRed                           [17] Escaneo agresivo  
[8] Scanear un solo puerto                   [18] Escanear todos los puertos - [TCP]          
[9] Scaneo silencioso                        [19] Escanear todos los puertos - [UDP]    
[10] Host activos en la web + trace route    [20] Mandar paquetes ICMP                                            
'''
############### Banner ###############

 # coded by  cabeson sin z!

############### Nmap code ###############



def nmap():
    os.system('clear') 
    print(banner3) 
  ######################## All opciones - Nmap ##########################
    opcion = input("\033[1;36m"+' Seleciona una opcion\n >> ')
    if opcion == "1":
        os.system("clear")
        print("\033[1;36m"+ banner1)
        normal = input("\033[1;36m" + "Que ip quieres scanear?\n>> " )        
        os.system("nmap --top-ports 1000 " + (normal))
        time.sleep(15)
        input('Presiona Cualquier Letra Para Volver Al Menu\n>> ') 
        nmap()

 ######################## Opcion 2 ##########################

    elif opcion == "2":
        os.system("clear")
        print("\033[1;36m"+ banner1)
        psa = input("\033[1;36m" +"Introduzca una IP\n>> " "")
        os.system("nmap -p- " + (psa))
        time.sleep(15)
        input("\033[1;36m" +'Presiona Cualquier Letra Para Volver Al Menu\n>> ')
        nmap()

 ######################## Opcion 3 ##########################

    elif opcion == "4":
        os.system("clear")
        print("\033[1;36m"+ banner1)
        agresivo = input("\033[1;36m" +"Introduzca una ip u pagina web ( e.j https://googlesource.com )\n>> ")
        os.system("nmap -sV -T5"+agresivo)
        time.sleep(15)
        input("\033[1;36m" +'Presiona Cualquier Letra Para Volver Al Menu\n>> ') 
        nmap()

 ######################## Opcion 4 ##########################

    elif opcion == "3":
        os.system("clear")
        print("\033[1;36m" + banner1)
        normal = input("\033[1;36m" +"Introduzca una ip u pagina web ( e.j https://googlesource.com )\n>> ")      
        os.system("nmap -sV  "+normal)  
        time.sleep(15)
        input("\033[1;36m" +'Presiona Cualquier Letra Para Volver Al Menu\n>> ') 
        nmap()

 ######################## Opcion 5 ##########################

    elif opcion == "5":
        os.system("clear")
        print("\033[1;36m" + banner1)
        s = input("\033[1;36m" +"Introduzca una ip\n>> ")
        os.system(f'nmap -Pn -A  {s}')
        time.sleep(15)
        input("\033[1;36m" +'Presiona Cualquier Letra Para Volver Al Menu\n>> ') 
        nmap()

 ######################## Opcion 6 ##########################

    elif opcion == "6":
        os.system("clear")
        print("\033[1;36m" + banner1)
        systemx4 = input("\033[1;36m" + "Introduzca una ip u pagina web ( e.j https://googlesource.com )\n>> ")
        os.system("nmap -O "+systemx4)
        time.sleep(15)
        input("\033[1;36m" +'Presiona Cualquier Letra Para Volver Al Menu\n>> ') 
        nmap()

 ######################## Opcion 7 ##########################

    elif opcion == "7":
        os.system("clear")
        print("\033[1;36m" + banner1)
        subred = input("\033[1;36m" +"Introduzca una ip\n>> ")
        puertoSub = input("\033[1;36m" + "Introduzca un puerto ( usar abajo del 32 )\n>> ")
        os.system(f'nmap -sP {subred}/{puertoSub}')
        time.sleep(15)
        input("\033[1;36m" +'Presiona Cualquier Letra Para Volver Al Menu\n>> ') 
        nmap()

 ######################## Opcion 8 ##########################

    elif opcion == "8":
        os.system("clear")
        print("\033[1;36m" + banner1)
        ip = (input("\033[1;36m" + "Introduzca una Ip \n>> "))
        port = str(input("\033[1;36m" + "Introduzca un puerto \n>> "))
        os.system(f'nmap -p{port} {ip} ')
        time.sleep(15)
        input("\033[1;36m" + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ') 
        nmap()

 ######################## Opcion 9 ##########################

    elif opcion == "9":
        os.system("clear")
        print("\033[1;36m" + banner1)
        ipyp = input("\033[1;36m" + "Introduzca una ip\n>> ")
        print(Fore.BLUE)
        os.system(f'nmap --script safe {ipyp}')
        time.sleep(15)
        input("\033[1;36m" + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ') 
        nmap() 

 ######################## Opcion 10 ##########################

    elif opcion == "10":
        os.system("clear")
        print("\033[1;36m" + banner1)
        slut = input("\033[1;36m" +"Introduzca una ip u pagina web ( e.j https://googlesource.com )\n>> ")
        os.system(f'nmap -sn --packet-trace --send-ip -v {slut}')
        time.sleep(15)
        input("\033[1;36m" + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ') 
        nmap() 

 ######################## Opcion 11 ##########################

    elif opcion == "11":
        os.system("clear")
        print("\033[1;36m" + banner1)
        njs = input("\033[1;36m" +"Introduzca una ip\n>> ")         
        os.system(f'nmap -sn -v {njs}')
        time.sleep(15)
        input("\033[1;36m" +'Presiona Cualquier Letra Para Volver Al Menu\n>> ')
        nmap()

 ######################## Opcion 12 ##########################

    elif opcion == "12":
        os.system("clear")
        print("\033[1;36m" +banner1)
        ping = input("\033[1;36m" +("Introduzca una pagina web ( e.j https://googlesource.com )\n>> "))
        os.system(f'ping {ping}')
        time.sleep(15)
        input("\033[1;36m" + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ')
        nmap()

 ######################## Opcion 13 ##########################

    elif opcion == "13":
        os.system("clear")
        print("\033[1;36m" + banner1)
        ConfundirFirewall = input("\033[1;36m" + ("Introduzca una ip\n>> "))
        os.system(f' nmap --mtu 24 -sV {ConfundirFirewall}')
        time.sleep(15)
        input("\033[1;36m" +'Presiona Cualquier Letra Para Volver Al Menu\n>> ')
        nmap()

 ######################## Opcion 14 ##########################

    elif opcion == "14":
        os.system("clear")
        print("\033[1;36m" + banner1)
        senuelo = input("\033[1;36m" + ("Introduzca una ip\n>> "))
        os.system(f'nmap -n -D 172.67.131.21,104.21.3.183 {senuelo}')
        time.sleep(15)
        input("\033[1;36m" +'Presiona Cualquier Letra Para Volver Al Menu\n>> ')
        nmap()

 ######################## Opcion 15 ##########################

    elif opcion == "15":
        os.system("clear")
        print("\033[1;36m" + banner1)
        senuelo = input("\033[1;36m" +( "Introduzca una ip u pagina web ( e.j https://googlesource.com )\n>> "))
        Port = input("\033[1;36m" +  ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 80,443)\n>> "))
        os.system(f'nmap -p{Port} --script http-waf-detect --script-args="http-waf-detect.aggro,http-waf-detect.detectBodyChanges" {senuelo}')
        time.sleep(15)
        input("\033[1;36m" + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ')
        nmap()

 ######################## Opcion 16 ##########################
    elif opcion == "16":
        os.system("clear")
        print("\033[1;36m" + banner1)
        senuelo = input("\033[1;36m" + ( "Introduzca una ip u pagina web ( e.j https://googlesource.com )\n>> "))
        Port = input("\033[1;36m" +("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 80,443)\n>> "))
        os.system(f"nmap -p{Port} --script http-waf-fingerprint {senuelo}")
        time.sleep(15)
        input("\033[1;36m" + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ')
        nmap()


 ######################## Opcion 17 ##########################

    elif opcion == "17":
        os.system("clear")
        print("\033[1;36m" + banner1)
        AgresivC = input("\033[1;36m" + ("Introduzca una ip\n>> "))
        os.system(f"nmap -sS -T insane {AgresivC}")
        time.sleep(15)
        input("\033[1;36m" + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ')
        nmap()


 ######################## Opcion 18 ##########################

    elif opcion == "18": 
        os.system("clear")
        print("\033[1;36m" + banner1)
        tcpP = input("\033[1;36m" + ("Introduzca una ip\n>> "))
        os.system(f"nmap -n -Pn -sS -p- {tcpP}")
        time.sleep(15)
        input("\033[1;36m" + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ')
        nmap()

  ######################## Opcion 19 ##########################

    elif opcion == "19": 
        os.system("clear")
        print("\033[1;36m" + banner1)
        Udp = input("\033[1;36m" + ("Introduzca una ip\n>> "))
        os.system(f" nmap -n -Pn -sU -p- {Udp}")
        time.sleep(15)
        input("\033[1;36m" + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ')
        nmap()

  ######################## Opcion 20 ##########################   
    
    elif opcion == "20":
        os.system("clear")
        print("\033[1;36m" + banner1)
        icmp = input("\033[1;36m" + ("Introduzca una ip\n>> "))
        paquetes = int(input(Fore.BLUE + ("Introduzca el numero de paquetes\n>>")))
        os.system(f"nping -c {paquetes} {icmp}") 
        time.sleep(15)
        input("\033[1;36m" + "Presiona Cualquier Letra Para Volver Al Menu\n>> ")
        nmap()  

    elif opcion == "0":
        os.system('clear')
        print('Buscando Ayuda....')
        time.sleep(2)
        os.system('nmap -help')
        time.sleep(5)
        input("\033[1;36m" + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ')
        nmap()
    elif opcion == "00":
        script()    
    else: 
        print("\033[1;36m" + ("no has puesto una opcion correcta!"))
        print("\033[1;36m" + ("Volviendo Al Menu..."))   
        time.sleep(2)
        (nmap()) 
 ######################### Nmap-Scripts ###############################
def script():
    os.system('clear')
    banner = ("\033[1;36m"+ '''

    ███████╗ ██████╗██████╗ ██╗██████╗ ████████╗███████╗
    ██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝██╔════╝
    ███████╗██║     ██████╔╝██║██████╔╝   ██║   ███████╗
    ╚════██║██║     ██╔══██╗██║██╔═══╝    ██║   ╚════██║
    ███████║╚██████╗██║  ██║██║██║        ██║   ███████║
    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   ╚══════╝
                                                                                              
    [001] FTP brute force  -- (Script usado para la fuerza bruta en el protocolo ftp)        
    [002] Safe script nmap -- (Script que permite un escaneo silencioso)                     
    [003] heartbleed --  (Script que Detecta si un servidor es vulnerable a Heartbleed)      
    [004] Dns Search --  (Script utilizado para la busqueda de subdominios)                  
    [005] MySql DB -- (Script que nos permite buscar contrasenias en servicios mysql)       
    [006] Malware -- (Script que detectar si un host remoto posee algún tipo de malware)     
    [007] Version -- (Script que que extienden la funcionalidad de la detección de versiones)
    [008] Enum -- (Script Enumera los directorios utilizados en servidores web)               
    [009] Vulnscan -- (Script que busca vulnerabilidades Mas recomendado)                    
    [010] Para el correcto funcionamiento de todos los script ejecutar esto primero          
    [000] Volver al menu principal                                                           
           
    ''')
    print(banner)
    opcion = input("\033[1;36m"+' Seleciona una opcion\n >> ')     

    if opcion == "001":
        print('Disclamer: Esto puede tardar mucho ya que es una ataque de fuerza bruta ')
        time.sleep(3)
        os.system('clear')
        print(banner1)
        target = input("\033[1;36m" + 'Introduzca una ip\n>>')
        Port = input("\033[1;36m" + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 21)\n>> "))
        os.system(f'nmap --script ftp-brute -p 21 {target}')
        time.sleep(15)
        input("\033[1;36m" + "Presiona Cualquier Letra Para Volver Al Menu\n>> ")
        script() 

    elif opcion == "002":
        os.system('clear')
        print(banner1)
        target = input("\033[1;36m" + 'Introduzca una ip\n>>')
        os.system(f'nmap -f --script safe {target}')
        time.sleep(15)
        input("\033[1;36m" + "Presiona Cualquier Letra Para Volver Al Menu\n>> ")
        script()

    elif opcion == "003":
        os.system('clear')
        print(banner1)
        target = input("\033[1;36m" +'Introduzca una ip\n>>')
        Port = input("\033[1;36m" + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 443)\n>> "))
        os.system(f'nmap -p 443 --script ssl-heartbleed {target}')
        time.sleep(15)
        input("\033[1;36m" + "Presiona Cualquier Letra Para Volver Al Menu\n>> ")
        script()  

    elif opcion == "004":
        os.system('clear')
        print(banner1)
        target = input("\033[1;36m" + 'Introduzca una ip\n>>')
        Port = input("\033[1;36m" + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 80,443)\n>> "))
        os.system(f'nmap -p{Port} --script dns-brute {target}')
        time.sleep(15)
        input("\033[1;36m" + "Presiona Cualquier Letra Para Volver Al Menu\n>> ")
        script()

    elif opcion == "005":
        os.system('clear')
        print(banner1)
        target = input("\033[1;36m" + 'Introduzca una ip\n>>')
        Port = input("\033[1;36m" + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 3306)\n>> "))
        os.system(f'nmap -p{Port} --script mysql-empty-password {target}')
        time.sleep(15)
        input("\033[1;36m" + "Presiona Cualquier Letra Para Volver Al Menu\n>> ")
        script()

    elif opcion == "006":
        os.system('clear')
        print(banner1)
        target = input("\033[1;36m" + 'Introduzca una ip\n>>')
        #Port = input("\033[1;36m" + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 3306)\n>> "))
        os.system(f'nmap -sV --script=http-malware-host  {target}')
        time.sleep(15)
        input("\033[1;36m" + "Presiona Cualquier Letra Para Volver Al Menu\n>> ")
        script()
    elif opcion == "007":
        os.system('clear')
        print(banner1)
        target = input("\033[1;36m" + 'Introduzca una ip\n>>')
        #Port = input("\033[1;36m" + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 3306)\n>> "))
        os.system(f'nmap -sV --script="version,discovery"  {target}')
        time.sleep(15)
        input("\033[1;36m" + "Presiona Cualquier Letra Para Volver Al Menu\n>> ")
        script()
    elif opcion == "008":
        os.system('clear')
        print(banner1)
        target = input("\033[1;36m" + 'Introduzca una ip\n>>')
        #Port = input("\033[1;36m" + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 3306)\n>> "))
        os.system(f'nmap --script http-enum  {target}')
        time.sleep(15)
        input("\033[1;36m" + "Presiona Cualquier Letra Para Volver Al Menu\n>> ")
        script()
    elif opcion == "009":
        os.system('clear')
        print(banner1)
        target = input("\033[1;36m" + 'Introduzca una ip\n>>')
        #Port = input("\033[1;36m" + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 3306)\n>> "))
        os.system(f'nmap -sV --script=vulscan/vulscan.nse {target}')
        time.sleep(15)
        input("\033[1;36m" + "Presiona Cualquier Letra Para Volver Al Menu\n>> ")
        script()
    elif opcion == "010":
        os.system('clear')
        print('Instalando Script porfavor esperar')
        time.sleep(1)
        os.system('git clone https://github.com/scipag/vulscan scipag_vulscan')
        time.sleep(5)
        os.system('ln -s `pwd`/scipag_vulscan /usr/share/nmap/scripts/vulscan')
        time.sleep(5)
        input("\033[1;36m" + "Presiona Cualquier Letra Para Volver Al Menu\n>> ")
        script()        

    elif opcion == "000":
        os.system('clear')
        (nmap())
    
    else:
        print("\033[1;36m" + ("no has puesto una opcion correcta!"))
        print("\033[1;36m" + ("Volviendo Al Menu..."))   
        time.sleep(2)
        (script())    

 ######################## Panel de ayuda - Nmap ##########################

def exit():
    print('Saliendo......')
    time.sleep(1)
    os.system("clear")
    sys.exit(1)


nmap()
