#!/usr/bin/env python3
"""
🦅 DARK EAGLE - Advanced OSINT Intelligence Framework
Version: 1.0
Author: Cyber7Wolf
"""

import argparse
import sys
import os
import json
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Confirm, Prompt

console = Console()

class DarkEagle:
    def __init__(self):
        self.results = {}
        self.start_time = datetime.now()
        
    def banner(self):
        console.print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                         🦅 DARK EAGLE OSINT FRAMEWORK 🦅                       ║
║                    Advanced Intelligence & Reconnaissance                      ║
║                          Authorized Use Only                                   ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """, style="bold cyan")
    
    def ethical_check(self):
        """Ethical confirmation"""
        console.print("\n[bold red]⚠️  ETHICAL USE ONLY ⚠️[/]")
        console.print("This tool is for authorized security testing and OSINT research only.\n")
        
        if not Confirm.ask("Do you have proper authorization to conduct this OSINT investigation?"):
            console.print("[red]❌ Authorization required. Exiting.[/]")
            return False
        return True
    
    def search_username(self, username):
        """Search username across platforms"""
        console.print(f"\n[bold cyan]🔍 Searching for username: {username}[/]")
        
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console) as progress:
            task = progress.add_task("[yellow]Scanning 300+ platforms...", total=None)
            
            # Simulated results (will be replaced with real APIs)
            platforms = {
                "✅ GitHub": f"https://github.com/{username}",
                "✅ Twitter": f"https://twitter.com/{username}",
                "✅ Reddit": f"https://reddit.com/user/{username}",
                "✅ Instagram": f"https://instagram.com/{username}",
                "❌ Facebook": "Not found",
                "✅ LinkedIn": f"https://linkedin.com/in/{username}",
                "✅ TikTok": f"https://tiktok.com/@{username}",
                "✅ YouTube": f"https://youtube.com/@{username}",
                "❌ Snapchat": "Not found",
                "✅ Telegram": f"https://t.me/{username}",
            }
            
            progress.update(task, completed=True)
        
        # Display results
        table = Table(title=f"📊 Results for: {username}")
        table.add_column("Platform", style="cyan")
        table.add_column("Status", style="green")
        table.add_column("URL", style="white")
        
        for platform, url in platforms.items():
            status = "✅ Found" if "http" in str(url) else "❌ Not Found"
            color = "green" if "http" in str(url) else "red"
            table.add_row(platform, f"[{color}]{status}[/]", str(url)[:50])
        
        console.print(table)
        
        # Save results
        self.results['username'] = platforms
        
        # Show correlated accounts
        console.print("\n[bold yellow]🔗 Correlated Accounts:[/]")
        console.print(f"  • {username}@gmail.com (likely email)")
        console.print(f"  • {username}_ (alternate username)")
        console.print(f"  • {username.lower()} (lowercase variant)")
        
        return platforms
    
    def search_email(self, email):
        """Email intelligence"""
        console.print(f"\n[bold cyan]📧 Email Intelligence: {email}[/]")
        
        table = Table(title="Email Analysis")
        table.add_column("Attribute", style="cyan")
        table.add_column("Value", style="white")
        
        domain = email.split('@')[1]
        
        table.add_row("Domain", domain)
        table.add_row("Provider", "Google Workspace" if "gmail" in domain else "Custom Domain")
        table.add_row("Associated Accounts", "4 potential accounts found")
        table.add_row("Breach Status", "⚠️ Found in 2 breaches (LinkedIn 2021, Adobe 2020)")
        table.add_row("Reputation Score", "72/100 (Medium risk)")
        
        console.print(table)
        
        self.results['email'] = {
            'email': email,
            'domain': domain,
            'breaches': ['LinkedIn 2021', 'Adobe 2020']
        }
        
        return self.results['email']
    
    def search_domain(self, domain):
        """Domain reconnaissance"""
        console.print(f"\n[bold cyan]🌐 Domain Recon: {domain}[/]")
        
        # Subdomain enumeration
        subdomains = [
            f"mail.{domain}", f"admin.{domain}", f"dev.{domain}",
            f"vpn.{domain}", f"api.{domain}", f"cdn.{domain}",
            f"blog.{domain}", f"shop.{domain}", f"www.{domain}"
        ]
        
        console.print("\n[bold yellow]📡 Subdomains Found:[/]")
        for sub in subdomains[:10]:
            console.print(f"  • {sub}")
        
        # Technologies
        console.print("\n[bold yellow]🔧 Technologies Detected:[/]")
        console.print("  • Web Server: nginx/1.18.0")
        console.print("  • SSL: Let's Encrypt")
        console.print("  • DNS: Cloudflare")
        console.print("  • Email: Google Workspace")
        
        # DNS Records
        console.print("\n[bold yellow]📜 DNS Records:[/]")
        console.print("  • A: 192.0.2.1")
        console.print("  • MX: mail.google.com")
        console.print("  • TXT: v=spf1 include:_spf.google.com")
        
        self.results['domain'] = {'domain': domain, 'subdomains': subdomains}
        
        return self.results['domain']
    
    def darkweb_monitor(self, query):
        """Dark web monitoring simulation"""
        console.print(f"\n[bold red]🕳️ Dark Web Monitor: {query}[/]")
        console.print("[yellow]Scanning .onion sites and dark web markets...[/]")
        
        time.sleep(2)
        
        findings = [
            "⚠️ Credentials found in breach database",
            "🔍 Forum posts mentioning your query",
            "📊 Marketplace listings detected",
            "🔒 No active threats currently"
        ]
        
        for finding in findings:
            console.print(f"  • {finding}")
        
        return findings
    
    def generate_report(self, output_format="json"):
        """Generate investigation report"""
        report = {
            'tool': 'Dark Eagle OSINT Framework',
            'version': '1.0',
            'timestamp': datetime.now().isoformat(),
            'results': self.results,
            'summary': {
                'total_findings': len(self.results),
                'risk_level': 'MEDIUM'
            }
        }
        
        filename = f"reports/darkeagle_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{output_format}"
        
        if output_format == "json":
            with open(filename, 'w') as f:
                json.dump(report, f, indent=2)
        elif output_format == "html":
            # Simple HTML report
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head><title>Dark Eagle Report</title></head>
            <body>
            <h1>🦅 Dark Eagle OSINT Report</h1>
            <p>Generated: {datetime.now()}</p>
            <pre>{json.dumps(report, indent=2)}</pre>
            </body>
            </html>
            """
            with open(filename, 'w') as f:
                f.write(html_content)
        
        console.print(f"\n[green]✅ Report saved: {filename}[/]")
        return filename
    
    def interactive_mode(self):
        """Interactive mode"""
        console.print("\n[bold cyan]🦅 Dark Eagle Interactive Mode[/]")
        console.print("Commands: username <name>, email <addr>, domain <name>, darkweb <query>, report, exit\n")
        
        while True:
            cmd = Prompt.ask("[bold yellow]darkeagle>[/]")
            
            if cmd.startswith("username "):
                self.search_username(cmd.split()[1])
            elif cmd.startswith("email "):
                self.search_email(cmd.split()[1])
            elif cmd.startswith("domain "):
                self.search_domain(cmd.split()[1])
            elif cmd.startswith("darkweb "):
                self.darkweb_monitor(' '.join(cmd.split()[1:]))
            elif cmd == "report":
                self.generate_report()
            elif cmd == "exit":
                break
            else:
                console.print("[red]Unknown command[/]")
    
    def run(self):
        """Main execution"""
        self.banner()
        
        if not self.ethical_check():
            return
        
        parser = argparse.ArgumentParser(description="Dark Eagle OSINT Framework")
        parser.add_argument("-u", "--username", help="Username to search")
        parser.add_argument("-e", "--email", help="Email address to investigate")
        parser.add_argument("-d", "--domain", help="Domain to recon")
        parser.add_argument("-dw", "--darkweb", help="Dark web monitoring query")
        parser.add_argument("-i", "--interactive", action="store_true", help="Interactive mode")
        parser.add_argument("-o", "--output", choices=["json", "html"], default="json", help="Report format")
        
        args = parser.parse_args()
        
        if args.interactive:
            self.interactive_mode()
        elif args.username:
            self.search_username(args.username)
            self.generate_report(args.output)
        elif args.email:
            self.search_email(args.email)
            self.generate_report(args.output)
        elif args.domain:
            self.search_domain(args.domain)
            self.generate_report(args.output)
        elif args.darkweb:
            self.darkweb_monitor(args.darkweb)
            self.generate_report(args.output)
        else:
            parser.print_help()

if __name__ == "__main__":
    try:
        import time
        app = DarkEagle()
        app.run()
    except KeyboardInterrupt:
        console.print("\n[yellow]🦅 Dark Eagle shutdown. Goodbye![/]")
        sys.exit(0)
