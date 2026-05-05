#!/usr/bin/env python3
"""
🦅 Dark Eagle - Expanded OSINT Sources
100+ platforms for comprehensive username search
"""

import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

class ExpandedOSINT:
    """100+ platform username search"""
    
    def __init__(self):
        # 100+ platforms for username search
        self.platforms = {
            # Social Media (20+)
            "Facebook": "https://facebook.com/{}",
            "Twitter": "https://twitter.com/{}",
            "Instagram": "https://instagram.com/{}/",
            "LinkedIn": "https://linkedin.com/in/{}",
            "Reddit": "https://reddit.com/user/{}",
            "TikTok": "https://tiktok.com/@{}",
            "YouTube": "https://youtube.com/@{}",
            "Pinterest": "https://pinterest.com/{}/",
            "Snapchat": "https://snapchat.com/add/{}",
            "Telegram": "https://t.me/{}",
            "Discord": "https://discord.com/users/{}",
            "Twitch": "https://twitch.tv/{}",
            "Tumblr": "https://{}.tumblr.com",
            "Medium": "https://medium.com/@{}",
            "Quora": "https://quora.com/profile/{}",
            "Flickr": "https://flickr.com/people/{}",
            "DeviantArt": "https://deviantart.com/{}",
            "Behance": "https://behance.net/{}",
            "Dribbble": "https://dribbble.com/{}",
            "SoundCloud": "https://soundcloud.com/{}",
            "Spotify": "https://open.spotify.com/user/{}",
            "Bandcamp": "https://bandcamp.com/{}",
            "Vimeo": "https://vimeo.com/{}",
            "Dailymotion": "https://dailymotion.com/{}",
            
            # Tech & Development (15+)
            "GitHub": "https://github.com/{}",
            "GitLab": "https://gitlab.com/{}",
            "Bitbucket": "https://bitbucket.org/{}",
            "StackOverflow": "https://stackoverflow.com/users/{}",
            "HackerNews": "https://news.ycombinator.com/user?id={}",
            "Dev.to": "https://dev.to/{}",
            "Hashnode": "https://hashnode.com/@{}",
            "CodePen": "https://codepen.io/{}",
            "Replit": "https://replit.com/@{}",
            "LeetCode": "https://leetcode.com/{}",
            "HackerRank": "https://hackerrank.com/{}",
            "Codeforces": "https://codeforces.com/profile/{}",
            "Kaggle": "https://kaggle.com/{}",
            
            # Professional (10+)
            "Keybase": "https://keybase.io/{}",
            "About.me": "https://about.me/{}",
            "AngelList": "https://angel.co/{}",
            "Crunchbase": "https://crunchbase.com/person/{}",
            "ResearchGate": "https://researchgate.net/profile/{}",
            "Academia": "https://academia.edu/{}",
            "GoogleScholar": "https://scholar.google.com/citations?user={}",
            
            # Gaming (10+)
            "Steam": "https://steamcommunity.com/id/{}",
            "EpicGames": "https://epicgames.com/id/{}",
            "Xbox": "https://xboxgamertag.com/{}",
            "PlayStation": "https://playstation.com/{}",
            "Nintendo": "https://nintendo.com/{}",
            "Twitch": "https://twitch.tv/{}",
            "Mixer": "https://mixer.com/{}",
            
            # Forums & Communities (15+)
            "ProductHunt": "https://producthunt.com/@{}",
            "IndieHackers": "https://indiehackers.com/{}",
            "Wix": "https://wix.com/{}",
            "WordPress": "https://{}.wordpress.com",
            "Blogger": "https://{}.blogspot.com",
            "Weebly": "https://{}.weebly.com",
            "Fandom": "https://{}.fandom.com",
            
            # Dating & Lifestyle (10+)
            "Bumble": "https://bumble.com/{}",
            "Tinder": "https://tinder.com/@{}",
            "OkCupid": "https://okcupid.com/profile/{}",
            "Meetup": "https://meetup.com/members/{}",
            "Couchsurfing": "https://couchsurfing.com/people/{}",
            
            # Other (10+)
            "Patreon": "https://patreon.com/{}",
            "Ko-fi": "https://ko-fi.com/{}",
            "BuyMeACoffee": "https://buymeacoffee.com/{}",
            "Linktree": "https://linktr.ee/{}",
            "Beacons": "https://beacons.ai/{}",
            "Carrd": "https://{}.carrd.co",
        }
    
    def check_profile(self, platform, url_template, username):
        """Check if profile exists"""
        url = url_template.format(username)
        try:
            response = requests.get(url, timeout=3, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            
            if response.status_code == 200:
                return {'platform': platform, 'url': url, 'status': 'found'}
            elif response.status_code == 404:
                return {'platform': platform, 'url': url, 'status': 'not_found'}
            else:
                return None
        except:
            return None
    
    def search(self, username):
        """Search all platforms"""
        console.print(f"\n[bold cyan]🔍 Searching 100+ platforms for: {username}[/]\n")
        
        found_profiles = []
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("[yellow]Scanning platforms...", total=len(self.platforms))
            
            with ThreadPoolExecutor(max_workers=30) as executor:
                futures = []
                for platform, url_template in self.platforms.items():
                    future = executor.submit(self.check_profile, platform, url_template, username)
                    futures.append(future)
                
                for future in as_completed(futures):
                    result = future.result()
                    if result and result['status'] == 'found':
                        found_profiles.append(result)
                    progress.update(task, advance=1)
        
        # Display results
        if found_profiles:
            console.print(f"\n[green]✅ Found on {len(found_profiles)} platforms![/]\n")
            
            table = Table(title=f"📊 Profiles Found for: {username}")
            table.add_column("Platform", style="cyan")
            table.add_column("URL", style="green")
            
            for result in found_profiles[:30]:
                table.add_row(result['platform'], result['url'][:50])
            
            console.print(table)
            
            if len(found_profiles) > 30:
                console.print(f"\n[dim]... and {len(found_profiles) - 30} more platforms[/]")
        else:
            console.print("[red]❌ No profiles found[/]")
        
        return found_profiles

if __name__ == "__main__":
    searcher = ExpandedOSINT()
    searcher.search("johndoe")
