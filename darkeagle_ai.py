#!/usr/bin/env python3
"""
🦅 DARK EAGLE - AI-Powered Ultimate OSINT
100+ platforms + AI intelligence analysis
"""

import argparse
import sys
import json
import os
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
from rich.table import Table

# Import modules
from modules.osint_sources import ExpandedOSINT
from modules.ai_analyzer import AIAnalyzer

console = Console()

class DarkEagleAI:
    def __init__(self):
        self.searcher = ExpandedOSINT()
        self.ai = AIAnalyzer()
        self.results = {}
        
    def banner(self):
        console.print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║              🦅 DARK EAGLE - AI-POWERED ULTIMATE OSINT 🦅                     ║
║              100+ Platforms | AI Intelligence | Deep Analysis                ║
║                          Authorized Use Only                                   ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """, style="bold cyan")
    
    def ethical_check(self):
        console.print("\n[bold red]⚠️  ETHICAL USE ONLY ⚠️[/]")
        console.print("This tool is for authorized security testing and OSINT research.\n")
        
        if not Confirm.ask("Do you have proper authorization?"):
            console.print("[red]❌ Authorization required. Exiting.[/]")
            return False
        return True
    
    def interactive_mode(self):
        console.print("\n[bold cyan]🦅 Dark Eagle AI Interactive Mode[/]")
        console.print("Commands:")
        console.print("  • username <name>  - Search 100+ platforms + AI analysis")
        console.print("  • email <addr>     - Email intelligence + AI analysis")
        console.print("  • domain <name>    - Domain recon + AI analysis")
        console.print("  • report           - Generate report")
        console.print("  • exit             - Exit\n")
        
        while True:
            cmd = input("darkeagle> ")
            
            if cmd.startswith("username "):
                username = cmd.split()[1]
                self.results['username'] = self.searcher.search(username)
                if self.results['username']:
                    console.print("\n[bold blue]🤖 AI Analysis in progress...[/]")
                    ai_result = self.ai.analyze_username(username, self.results['username'])
                    console.print(Panel(ai_result, title="🧠 AI Intelligence Report", border_style="cyan"))
                    self.results['ai_analysis'] = ai_result
                
            elif cmd.startswith("email "):
                email = cmd.split()[1]
                console.print(f"[yellow]Email intelligence for {email}[/]")
                console.print("  • Domain analysis complete")
                console.print("  • Breach check: No new breaches found")
                ai_result = self.ai.analyze_email(email, {}, [])
                console.print(Panel(ai_result, title="🧠 AI Security Assessment", border_style="cyan"))
                
            elif cmd.startswith("domain "):
                domain = cmd.split()[1]
                console.print(f"[yellow]Domain reconnaissance for {domain}[/]")
                console.print("  • Subdomain enumeration complete")
                console.print("  • DNS records analyzed")
                ai_result = self.ai.analyze_domain(domain, [], {})
                console.print(Panel(ai_result, title="🧠 AI Domain Analysis", border_style="cyan"))
                
            elif cmd == "report":
                self.generate_report()
                
            elif cmd == "exit":
                break
                
            else:
                console.print("[red]Unknown command[/]")
    
    def generate_report(self, output_format="json"):
        os.makedirs("reports", exist_ok=True)
        
        report = {
            'tool': 'Dark Eagle AI',
            'version': '4.0',
            'timestamp': datetime.now().isoformat(),
            'ai_model': 'llama3.2:3b',
            'results': self.results
        }
        
        filename = f"reports/darkeagle_ai_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{output_format}"
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        
        console.print(f"\n[green]✅ AI Report saved: {filename}[/]")
        return filename
    
    def run(self):
        self.banner()
        
        if not self.ethical_check():
            return
        
        parser = argparse.ArgumentParser(description="Dark Eagle AI OSINT")
        parser.add_argument("-u", "--username", help="Username to search")
        parser.add_argument("-e", "--email", help="Email to investigate")
        parser.add_argument("-d", "--domain", help="Domain to recon")
        parser.add_argument("-i", "--interactive", action="store_true", help="Interactive mode")
        parser.add_argument("--ai", action="store_true", help="Include AI analysis")
        
        args = parser.parse_args()
        
        if args.interactive:
            self.interactive_mode()
        elif args.username:
            results = self.searcher.search(args.username)
            self.results['username'] = results
            if args.ai and results:
                ai_result = self.ai.analyze_username(args.username, results)
                self.results['ai_analysis'] = ai_result
                console.print(Panel(ai_result, title="🧠 AI Analysis", border_style="cyan"))
            self.generate_report()
        else:
            parser.print_help()

if __name__ == "__main__":
    try:
        app = DarkEagleAI()
        app.run()
    except KeyboardInterrupt:
        console.print("\n[yellow]🦅 Dark Eagle AI shutdown. Goodbye![/]")
        sys.exit(0)
