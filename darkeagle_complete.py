#!/usr/bin/env python3
"""
🦅 DARK EAGLE - Complete OSINT Framework
All modules integrated
"""

import argparse
import sys
import json
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt

from modules.username_search import UsernameSearch
from modules.email_intel import EmailIntel
from modules.domain_recon import DomainRecon

console = Console()

class DarkEagleComplete:
    def __init__(self):
        self.username_searcher = UsernameSearch()
        self.email_intel = EmailIntel()
        self.domain_recon = DomainRecon()
        self.results = {}
        
    def banner(self):
        console.print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    🦅 DARK EAGLE - COMPLETE OSINT 🦅                          ║
║              Intelligence Gathering | Reconnaissance | Analysis              ║
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
        """Interactive mode with all modules"""
        console.print("\n[bold cyan]🦅 Dark Eagle Interactive Mode[/]")
        console.print("Commands:")
        console.print("  • username <name>  - Search username across platforms")
        console.print("  • email <addr>     - Email intelligence")
        console.print("  • domain <name>    - Domain reconnaissance")
        console.print("  • report           - Generate report")
        console.print("  • exit             - Exit\n")
        
        while True:
            cmd = Prompt.ask("[bold yellow]darkeagle>[/]")
            
            if cmd.startswith("username "):
                username = cmd.split()[1]
                results = self.username_searcher.search(username)
                self.results['username'] = results
                
            elif cmd.startswith("email "):
                email = cmd.split()[1]
                results = self.email_intel.analyze(email)
                self.results['email'] = results
                
            elif cmd.startswith("domain "):
                domain = cmd.split()[1]
                results = self.domain_recon.analyze(domain)
                self.results['domain'] = results
                
            elif cmd == "report":
                self.generate_report()
                
            elif cmd == "exit":
                break
                
            else:
                console.print("[red]Unknown command[/]")
    
    def generate_report(self, output_format="json"):
        """Generate comprehensive report"""
        report = {
            'tool': 'Dark Eagle Complete',
            'version': '2.0',
            'timestamp': datetime.now().isoformat(),
            'results': self.results,
            'summary': {
                'total_modules': len(self.results),
                'findings_count': sum(len(v) for v in self.results.values() if isinstance(v, list))
            }
        }
        
        import os
        os.makedirs("reports", exist_ok=True)
        
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
        parser.add_argument("-d", "--domain", help="Domain to recon")
        parser.add_argument("-i", "--interactive", action="store_true", help="Interactive mode")
        parser.add_argument("-o", "--output", default="json", help="Report format")
        
        args = parser.parse_args()
        
        if args.interactive:
            self.interactive_mode()
        elif args.username:
            results = self.username_searcher.search(args.username)
            self.results['username'] = results
            self.generate_report(args.output)
        elif args.email:
            results = self.email_intel.analyze(args.email)
            self.results['email'] = results
            self.generate_report(args.output)
        elif args.domain:
            results = self.domain_recon.analyze(args.domain)
            self.results['domain'] = results
            self.generate_report(args.output)
        else:
            parser.print_help()

if __name__ == "__main__":
    try:
        app = DarkEagleComplete()
        app.run()
    except KeyboardInterrupt:
        console.print("\n[yellow]🦅 Dark Eagle shutdown. Goodbye![/]")
        sys.exit(0)
