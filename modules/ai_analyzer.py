#!/usr/bin/env python3
"""
🦅 Dark Eagle - AI-Powered Intelligence Analysis
Using Ollama for smart OSINT correlation
"""

import ollama
import json
from rich.console import Console
from rich.panel import Panel
from datetime import datetime

console = Console()

class AIAnalyzer:
    """AI-powered OSINT analysis"""
    
    def __init__(self, model="llama3.2:3b"):
        self.model = model
        console.log(f"[bold blue]🤖 AI Analyzer initialized with {model}[/]")
    
    def analyze_username(self, username, found_profiles):
        """AI analysis of username across platforms"""
        prompt = f"""Analyze this OSINT data about username '{username}':

Found on these platforms: {json.dumps(found_profiles[:20])}

Provide:
1. A profile summary (2-3 sentences)
2. Estimated person type (developer, gamer, professional, content creator)
3. Potential risk level (LOW/MEDIUM/HIGH)
4. One intelligence recommendation

Be concise and professional. Focus on open-source intelligence only."""

        try:
            response = ollama.generate(model=self.model, prompt=prompt)
            return response['response']
        except Exception as e:
            return f"AI analysis error: {e}"
    
    def analyze_email(self, email, domain_info, breaches):
        """AI analysis of email intelligence"""
        prompt = f"""Analyze this email intelligence:

Email: {email}
Domain: {domain_info.get('domain', 'Unknown')}
Breach Status: {len(breaches)} breaches found

Provide:
1. Security risk assessment
2. Recommended actions for the user
3. How this exposure could be exploited

Focus on educational security awareness."""

        try:
            response = ollama.generate(model=self.model, prompt=prompt)
            return response['response']
        except Exception as e:
            return f"AI analysis error: {e}"
    
    def analyze_domain(self, domain, subdomains, technologies):
        """AI analysis of domain reconnaissance"""
        prompt = f"""Analyze this domain intelligence:

Domain: {domain}
Subdomains found: {len(subdomains)}
Technologies: {json.dumps(technologies)}

Provide:
1. Security posture assessment
2. Potential vulnerabilities based on technology stack
3. Recommended security improvements

Keep it educational and constructive."""

        try:
            response = ollama.generate(model=self.model, prompt=prompt)
            return response['response']
        except Exception as e:
            return f"AI analysis error: {e}"
    
    def correlate_intelligence(self, all_data):
        """Correlate all OSINT data and provide comprehensive analysis"""
        prompt = f"""Correlate this comprehensive OSINT intelligence:

Data collected: {json.dumps(all_data, indent=2)[:2000]}

Provide:
1. Overall threat assessment
2. Key findings summary
3. Actionable recommendations
4. Privacy vulnerabilities discovered

Focus on open-source intelligence and security awareness."""

        try:
            response = ollama.generate(model=self.model, prompt=prompt)
            return response['response']
        except Exception as e:
            return f"AI correlation error: {e}"

if __name__ == "__main__":
    analyzer = AIAnalyzer()
    result = analyzer.analyze_username("testuser", [])
    print(result)
