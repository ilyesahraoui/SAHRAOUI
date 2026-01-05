import instaloader
from rich import print 
from rich.console import Console
import time
console = Console()
def il_insta():
    L = instaloader.Instaloader()
    console.print("""
                                                                 
,--.,--.                 ,--.,--.  ,--. ,---. ,--------. ,---.   
|  ||  |                 |  ||  ,'.|  |'   .-''--.  .--'/  O  \  
|  ||  |                 |  ||  |' '  |`.  `-.   |  |  |  .-.  | 
|  ||  '--.    ,----.    |  ||  | `   |.-'    |  |  |  |  | |  | 
`--'`-----'    '----'    `--'`--'  `--'`-----'   `--'  `--' `--' 


                           ......               
                        .:||||||||:.            
                       /            \           
                      (   o      o   )          
--------------@@@@----------:  :----------@@@@---------------------------                                  
""",style="red")

    print("""

                    [green]+ Welcome to ilinsta +[/green]        
    """)
    name = input("Enter name :")
    for _ in range(100):
        print("=" ,end="" ,flush=True)
        time.sleep(0.02)
    print(">")
    print("[yellow][!][/yellow][green]loding...[/green]")
    time.sleep(2)
    print("[green][+][/green][yellow]running...[/yellow]")
    time.sleep(2)
    try:
        profile = instaloader.Profile.from_username(L.context, name)
    except instaloader.exceptions.ProfileNotExistsException:
        print("[red][-] Profile not found[/red]")
        exit()



    print("[green]================================[/green] +[red] Profile information[/red] + [green]=================================[/green]")
    print(f" [yellow]_user name :[/yellow][green]{profile.username}[/green]")              
    print(f" [yellow]_Account id :[/yellow][green]{profile.userid}[/green]")                
    print(f" [yellow]_The full name that appears in the account :[/yellow][green]{profile.full_name}[/green]")            
    print(f" [yellow]_Bio :[/yellow][green]{profile.biography}[/green]")             
    print(f" [yellow]_Link in bio :[/yellow][green]{profile.external_url}[/green]")          
      
    print(f" [yellow]_Number of followers :[/yellow][green]{profile.followers}[/green]")          
    print(f" [yellow]_I follow :[/yellow][green]{profile.followees}[/green]")             
    print(f" [yellow]_Number of posts :[/yellow][green]{profile.mediacount}[/green]")            

    print(f" [yellow]_Is the account private? :[/yellow][green]{profile.is_private}[/green]")           
    print(f" [yellow]_Is the account verified? :[/yellow][green]{profile.is_verified}[/green]")         
    print(f" [yellow]_Is the account commercial? :[/yellow][green]{profile.is_business_account}[/green]")  

    print(f" [yellow]_Profile picture link :[/yellow][green]{profile.profile_pic_url}[/green]")     
    print(f" [yellow]_High-quality profile :[/yellow][green]{profile.profile_pic_url_no_iphone}[/green]") 

    print(f" [yellow]_Does it have highlights? :[/yellow][green]{profile.has_highlight_reels}[/green]")   


    print(f" [yellow]_Commercial activity :[/yellow][green]{profile.business_category_name}[/green]")          

    print(f" [yellow]_Did you ban celebrities? :[/yellow][green]{profile.has_blocked_viewer}[/green]")    
    print(f" [yellow]_Did you send him a follow-up request? :[/yellow][green]{profile.requested_by_viewer}[/green]")   
    print(f" [yellow]_Are you following him? :[/yellow][green]{profile.followed_by_viewer}[/green]")   
    print(f" [yellow]_Is he following you? :[/yellow][green]{profile.follows_viewer}[/green]")       

    for post in profile.get_posts():
        print("\n[bold red]=========================== POST ===================================[/bold red]")

        print(f"[yellow]Shortcode:[/yellow] [green]{post.shortcode}[/green]")
        print(f"[yellow]Post ID:[/yellow] [green]{post.mediaid}[/green]")
        print(f"[yellow]Owner Username:[/yellow] [green]{post.owner_username}[/green]")
        print(f"[yellow]Date:[/yellow] [green]{post.date_local}[/green]")
        print(f"[yellow]location:[/yellow] [green]{post.location}[/green]")
        print(f"[yellow]Caption:[/yellow] [green]{post.caption}[/green]")
        print(f"[yellow]Hashtags:[/yellow] [green]{list(post.caption_hashtags)}[/green]")
        print(f"[yellow]Mentions:[/yellow] [green]{list(post.caption_mentions)}[/green]")

        print(f"[yellow]Likes:[/yellow] [green]{post.likes}[/green]")
        print(f"[yellow]Comments Count:[/yellow] [green]{post.comments}[/green]")

        print(f"[yellow]Is Video:[/yellow] [green]{post.is_video}[/green]")
        if post.is_video:
            print(f"[yellow]Video Views:[/yellow] [green]{post.video_view_count}[/green]")
            print(f"[yellow]Video Duration (sec):[/yellow] [green]{post.video_duration}[/green]")

        print(f"[yellow]Post URL:[/yellow] [green]{post.url}[/green]")


        # Location
        if post.location:
            print(f"[yellow]Location Name:[/yellow] [green]{post.location.name}[/green]")
            print(f"[yellow]Latitude:[/yellow] [green]{post.location.lat}[/green]")
            print(f"[yellow]Longitude:[/yellow] [green]{post.location.lng}[/green]")
        else:
            print(f"[yellow]Location:[/yellow] [red]None[/red]")

        # Tagged users
        print(f"[yellow]Tagged Users:[/yellow] [green]{list(post.tagged_users)}[/green]")

        # Sidecar (multiple images)
        if post.typename == "GraphSidecar":
            print("[yellow]Sidecar Media:[/yellow]")
            for node in post.get_sidecar_nodes():
                print(f"   [green]{node.display_url}[/green]")

        # Comments details
        
        print("\n[bold red]=========================================================================[/bold red]")