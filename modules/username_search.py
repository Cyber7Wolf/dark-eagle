#!/usr/bin/env python3
"""
🦅 Dark Eagle - Real Username Search Module
Searches real platforms using public APIs and web scraping
"""

import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

class UsernameSearch:
    """Search username across real platforms"""
    
    def __init__(self):
        # Real platforms to search
        self.platforms = {
            "GitHub": "https://github.com/{}",
            "Twitter": "https://twitter.com/{}",
            "Instagram": "https://instagram.com/{}/",
            "Reddit": "https://reddit.com/user/{}",
            "LinkedIn": "https://linkedin.com/in/{}",
            "YouTube": "https://youtube.com/@{}",
            "TikTok": "https://tiktok.com/@{}",
            "Pinterest": "https://pinterest.com/{}/",
            "Tumblr": "https://{}.tumblr.com",
            "Medium": "https://medium.com/@{}",
            "Dev.to": "https://dev.to/{}",
            "Hashnode": "https://hashnode.com/@{}",
            "GitLab": "https://gitlab.com/{}",
            "Bitbucket": "https://bitbucket.org/{}",
            "Keybase": "https://keybase.io/{}",
            "Telegram": "https://t.me/{}",
            "Twitch": "https://twitch.tv/{}",
            "Steam": "https://steamcommunity.com/id/{}",
            "Spotify": "https://open.spotify.com/user/{}",
            "SoundCloud": "https://soundcloud.com/{}",
            "Behance": "https://behance.net/{}",
            "Dribbble": "https://dribbble.com/{}",
            "Flickr": "https://flickr.com/people/{}",
            "Patreon": "https://patreon.com/{}",
            "Discord": "https://discord.com/users/{}",
        }
        
    def check_profile(self, platform, url_template, username):
        """Check if profile exists on a platform"""
        url = url_template.format(username)
        try:
            response = requests.get(url, timeout=5, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            
            if response.status_code == 200:
                return {'platform': platform, 'url': url, 'status': 'found'}
            elif response.status_code == 404:
                return {'platform': platform, 'url': url, 'status': 'not_found'}
            else:
                return {'platform': platform, 'url': url, 'status': 'unknown'}
        except:
            return {'platform': platform, 'url': url, 'status': 'error'}
    
    def search(self, username):
        """Search username across all platforms"""
        console.print(f"\n[bold cyan]🔍 Searching for: {username}[/]")
        console.print(f"[dim]Scanning {len(self.platforms)} platforms...[/]\n")
        
        results = []
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("[yellow]Searching...", total=len(self.platforms))
            
            with ThreadPoolExecutor(max_workers=20) as executor:
                futures = []
                for platform, url_template in self.platforms.items():
                    future = executor.submit(self.check_profile, platform, url_template, username)
                    futures.append(future)
                
                for future in as_completed(futures):
                    result = future.result()
                    results.append(result)
                    progress.update(task, advance=1)
        
        # Display results
        found = [r for r in results if r['status'] == 'found']
        not_found = [r for r in results if r['status'] == 'not_found']
        
        console.print(f"\n[green]✅ Found on {len(found)} platforms[/]")
        console.print(f"[red]❌ Not found on {len(not_found)} platforms[/]\n")
        
        if found:
            table = Table(title=f"📊 Found Profiles for: {username}")
            table.add_column("Platform", style="cyan")
            table.add_column("URL", style="green")
            
            for result in found[:20]:  # Show top 20
                table.add_row(result['platform'], result['url'])
            
            console.print(table)
        
        return found

if __name__ == "__main__":
    searcher = UsernameSearch()
    searcher.search("johndoe")
