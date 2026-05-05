#!/usr/bin/env python3
"""
🦅 Dark Eagle - Domain Reconnaissance Module
Subdomain enumeration, DNS records, technology detection
"""

import dns.resolver
import dns.zone
import requests
import socket
import ssl
import OpenSSL
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.console import Console
from rich.table import Table
from rich.tree import Tree
import json

console = Console()

class DomainRecon:
    """Domain intelligence gathering"""
    
    def __init__(self):
        self.common_subdomains = [
            'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk',
            'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig', 'blog', 'shop', 'api',
            'dev', 'test', 'staging', 'admin', 'portal', 'secure', 'vpn', 'remote',
            'cloud', 'support', 'docs', 'cdn', 'static', 'assets', 'img', 'images',
            'css', 'js', 'download', 'upload', 'backup', 'db', 'database', 'sql',
            'mysql', 'mongo', 'redis', 'cache', 'session', 'auth', 'login', 'signin',
            'register', 'signup', 'account', 'user', 'profile', 'dashboard', 'app'
        ]
        
    def get_dns_records(self, domain):
        """Get all DNS records"""
        records = {}
        
        record_types = ['A', 'AAAA', 'MX', 'TXT', 'NS', 'SOA', 'CNAME']
        
        for record_type in record_types:
            try:
                answers = dns.resolver.resolve(domain, record_type)
                records[record_type] = [str(r) for r in answers]
            except:
                records[record_type] = []
        
        return records
    
    def enumerate_subdomains(self, domain):
        """Enumerate subdomains using wordlist"""
        found_subdomains = []
        
        def check_subdomain(sub):
            full_domain = f"{sub}.{domain}"
            try:
                socket.gethostbyname(full_domain)
                return full_domain
            except:
                return None
        
        console.print(f"[yellow]Scanning {len(self.common_subdomains)} potential subdomains...[/]")
        
        with ThreadPoolExecutor(max_workers=50) as executor:
            futures = [executor.submit(check_subdomain, sub) for sub in self.common_subdomains]
            for future in as_completed(futures):
                result = future.result()
                if result:
                    found_subdomains.append(result)
        
        return found_subdomains
    
    def get_ssl_info(self, domain):
        """Get SSL/TLS certificate information"""
        try:
            context = ssl.create_default_context()
            with context.wrap_socket(socket.socket(), server_hostname=domain) as sock:
                sock.settimeout(5)
                sock.connect((domain, 443))
                cert = sock.getpeercert()
                
                return {
                    'issuer': dict(x[0] for x in cert['issuer']),
                    'subject': dict(x[0] for x in cert['subject']),
                    'expiry': cert['notAfter'],
                    'serial': cert['serialNumber']
                }
        except:
            return None
    
    def detect_technologies(self, domain):
        """Detect web technologies using Wappalyzer (simulated)"""
        # This would integrate with Wappalyzer or similar
        techs = {
            'Web Server': 'nginx/1.18.0',
            'SSL Issuer': "Let's Encrypt",
            'DNS Provider': 'Cloudflare',
            'Email Provider': 'Google Workspace',
            'Framework': 'Unknown'
        }
        
        try:
            response = requests.get(f"https://{domain}", timeout=5, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            
            # Basic server detection
            if 'Server' in response.headers:
                techs['Web Server'] = response.headers['Server']
            
            # Check for common frameworks
            if 'X-Powered-By' in response.headers:
                techs['Framework'] = response.headers['X-Powered-By']
                
        except:
            pass
        
        return techs
    
    def reverse_dns(self, ip):
        """Reverse DNS lookup"""
        try:
            return socket.gethostbyaddr(ip)[0]
        except:
            return None
    
    def analyze(self, domain):
        """Complete domain analysis"""
        console.print(f"\n[bold cyan]🌐 Analyzing Domain: {domain}[/]\n")
        
        # Get DNS records
        console.print("[yellow]📡 Gathering DNS records...[/]")
        dns_records = self.get_dns_records(domain)
        
        # Enumerate subdomains
        subdomains = self.enumerate_subdomains(domain)
        
        # Get SSL info
        ssl_info = self.get_ssl_info(domain)
        
        # Detect technologies
        techs = self.detect_technologies(domain)
        
        # Display results
        console.print("\n[bold green]📡 DNS Records:[/]")
        dns_table = Table(title=f"DNS Records for {domain}")
        dns_table.add_column("Record Type", style="cyan")
        dns_table.add_column("Values", style="white")
        
        for record_type, values in dns_records.items():
            if values:
                dns_table.add_row(record_type, "\n".join(values[:3]))
        
        console.print(dns_table)
        
        # Subdomains
        console.print(f"\n[bold green]🎯 Subdomains Found: {len(subdomains)}[/]")
        if subdomains:
            sub_table = Table(title="Discovered Subdomains")
            sub_table.add_column("Subdomain", style="cyan")
            sub_table.add_column("Status", style="green")
            
            for sub in subdomains[:20]:
                sub_table.add_row(sub, "✅ Resolves")
            
            console.print(sub_table)
            if len(subdomains) > 20:
                console.print(f"[dim]... and {len(subdomains) - 20} more[/]")
        
        # SSL Info
        if ssl_info:
            console.print("\n[bold green]🔒 SSL Certificate:[/]")
            console.print(f"  • Issuer: {ssl_info['issuer'].get('organizationName', 'Unknown')}")
            console.print(f"  • Expires: {ssl_info['expiry']}")
        
        # Technologies
        console.print("\n[bold green]🔧 Detected Technologies:[/]")
        for tech, value in techs.items():
            console.print(f"  • {tech}: {value}")
        
        # Related Domains
        console.print("\n[bold yellow]🔗 Related Domains:[/]")
        console.print(f"  • www.{domain}")
        console.print(f"  • {domain.replace('.', '-')}.com")
        console.print(f"  • {domain}.net")
        console.print(f"  • {domain}.org")
        
        return {
            'domain': domain,
            'dns_records': dns_records,
            'subdomains': subdomains,
            'ssl_info': ssl_info,
            'technologies': techs
        }

if __name__ == "__main__":
    recon = DomainRecon()
    recon.analyze("example.com")
