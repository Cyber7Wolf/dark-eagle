#!/usr/bin/env python3
"""
🦅 DARK EAGLE - Enhanced OSINT Framework
With real API integrations
"""

import argparse
import sys
import json
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt

# Import modules
from modules.username_search import UsernameSearch
from modules.email_intel import EmailIntel

console = Console()

class DarkEagleEnhanced:
    def __init__(self):
        self.username_searcher = UsernameSearch()
        self.email_intel = EmailIntel()
        self.results = {}
        
    def banner(self):
        console.print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    🦅 DARK EAGLE - ENHANCED OSINT 🦅                          ║
║                    Real-time Intelligence Gathering                           ║
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
    
    def generate_report(self, output_format="json"):
        report = {
            'tool': 'Dark Eagle Enhanced',
            'timestamp': datetime.now().isoformat(),
            'results': self.results
        }
        
        filename = f"reports/darkeagle_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{output_format}"
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        
        console.print(f"\n[green]✅ Report saved: {filename}[/]")
        return filename
    
    def run(self):
        self.banner()
        
        if not self.ethical_check():
            return
        
        parser = argparse.ArgumentParser(description="Dark Eagle OSINT Framework")
        parser.add_argument("-u", "--username", help="Username to search")
        parser.add_argument("-e", "--email", help="Email to investigate")
        parser.add_argument("-o", "--output", default="json", help="Report format")
        
        args = parser.parse_args()
        
        if args.username:
            results = self.username_searcher.search(args.username)
            self.results['username'] = results
            self.generate_report(args.output)
        elif args.email:
            results = self.email_intel.analyze(args.email)
            self.results['email'] = results
            self.generate_report(args.output)
        else:
            parser.print_help()

if __name__ == "__main__":
    try:
        app = DarkEagleEnhanced()
        app.run()
    except KeyboardInterrupt:
        console.print("\n[yellow]🦅 Dark Eagle shutdown. Goodbye![/]")
        sys.exit(0)
