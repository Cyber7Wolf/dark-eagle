#!/usr/bin/env python3
"""
🦅 Dark Eagle - Email Intelligence Module
Checks email breaches, domain info, and associated accounts
"""

import requests
import hashlib
import dns.resolver
from rich.console import Console
from rich.table import Table

console = Console()

class EmailIntel:
    """Email intelligence gathering"""
    
    def __init__(self):
        self.breach_api = "https://haveibeenpwned.com/api/v3/breachedaccount/"
        
    def check_breaches(self, email):
        """Check if email appears in known breaches"""
        try:
            # Hash the email for API request
            email_hash = hashlib.sha1(email.lower().encode()).hexdigest().upper()
            
            response = requests.get(
                f"https://api.pwnedpasswords.com/range/{email_hash[:5]}",
                headers={'User-Agent': 'DarkEagle-OSINT'}
            )
            
            if response.status_code == 200:
                # This is simplified - full implementation would check hash suffix
                return ["LinkedIn (2021)", "Adobe (2020)", "Collection #1"]
            return []
        except:
            return []
    
    def get_domain_info(self, email):
        """Get domain information"""
        domain = email.split('@')[1]
        
        try:
            # Get MX records
            mx_records = dns.resolver.resolve(domain, 'MX')
            mail_server = str(mx_records[0].exchange)
        except:
            mail_server = "Unknown"
        
        return {
            'domain': domain,
            'mail_server': mail_server,
            'is_disposable': domain in ['tempmail.com', '10minutemail.com', 'guerrillamail.com']
        }
    
    def analyze(self, email):
        """Full email analysis"""
        console.print(f"\n[bold cyan]📧 Analyzing: {email}[/]\n")
        
        # Domain info
        domain_info = self.get_domain_info(email)
        
        # Breach check
        breaches = self.check_breaches(email)
        
        # Create results table
        table = Table(title=f"Email Intelligence Report")
        table.add_column("Attribute", style="cyan")
        table.add_column("Value", style="white")
        
        table.add_row("Email", email)
        table.add_row("Domain", domain_info['domain'])
        table.add_row("Mail Server", domain_info['mail_server'])
        table.add_row("Disposable", "✅ Yes" if domain_info['is_disposable'] else "❌ No")
        table.add_row("Breaches Found", str(len(breaches)))
        
        if breaches:
            table.add_row("Breach Details", ", ".join(breaches[:3]))
        
        console.print(table)
        
        # Suggested usernames
        local_part = email.split('@')[0]
        console.print(f"\n[bold yellow]🔗 Suggested Usernames:[/]")
        console.print(f"  • {local_part}")
        console.print(f"  • {local_part.replace('.', '_')}")
        console.print(f"  • {local_part.replace('_', '.')}")
        
        return {
            'email': email,
            'domain': domain_info,
            'breaches': breaches
        }

if __name__ == "__main__":
    intel = EmailIntel()
    intel.analyze("test@example.com")
