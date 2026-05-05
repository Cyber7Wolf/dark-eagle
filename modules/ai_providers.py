#!/usr/bin/env python3
"""
🦅 Dark Eagle - Multiple AI Providers
Support for Ollama (local), Claude (Anthropic), and GPT (OpenAI)
"""

import os
import json
from rich.console import Console
from rich.panel import Panel

console = Console()

class AIProvider:
    """Unified interface for multiple AI models"""
    
    def __init__(self, provider="ollama"):
        self.provider = provider
        self.api_keys = self.load_api_keys()
        
    def load_api_keys(self):
        """Load API keys from environment or config file"""
        keys = {
            'openai': os.getenv('OPENAI_API_KEY', ''),
            'anthropic': os.getenv('ANTHROPIC_API_KEY', '')
        }
        
        # Try to load from config file
        config_file = os.path.expanduser("~/.darkeagle/config.json")
        if os.path.exists(config_file):
            try:
                with open(config_file, 'r') as f:
                    config = json.load(f)
                    keys.update(config.get('api_keys', {}))
            except:
                pass
        
        return keys
    
    def query(self, prompt, model=None):
        """Query the selected AI provider"""
        if self.provider == "ollama":
            return self.query_ollama(prompt, model)
        elif self.provider == "openai":
            return self.query_openai(prompt, model)
        elif self.provider == "claude":
            return self.query_claude(prompt, model)
        else:
            return f"Unknown provider: {self.provider}"
    
    def query_ollama(self, prompt, model="llama3.2:3b"):
        """Local Ollama query"""
        try:
            import ollama
            response = ollama.generate(model=model, prompt=prompt)
            return response['response']
        except Exception as e:
            return f"Ollama error: {e}"
    
    def query_openai(self, prompt, model="gpt-3.5-turbo"):
        """OpenAI GPT query"""
        if not self.api_keys.get('openai'):
            return "OpenAI API key not set. Set OPENAI_API_KEY environment variable."
        
        try:
            from openai import OpenAI
            client = OpenAI(api_key=self.api_keys['openai'])
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"OpenAI error: {e}"
    
    def query_claude(self, prompt, model="claude-3-haiku-20240307"):
        """Anthropic Claude query"""
        if not self.api_keys.get('anthropic'):
            return "Anthropic API key not set. Set ANTHROPIC_API_KEY environment variable."
        
        try:
            from anthropic import Anthropic
            client = Anthropic(api_key=self.api_keys['anthropic'])
            response = client.messages.create(
                model=model,
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            return f"Claude error: {e}"
    
    def list_providers(self):
        """List available AI providers"""
        providers = {
            "ollama": "Local (Free, Private)",
            "openai": "GPT-3.5/4 (API key required)",
            "claude": "Claude 3 (API key required)"
        }
        
        console.print("\n[bold cyan]🤖 Available AI Providers:[/]")
        for name, desc in providers.items():
            status = "✅" if self.is_available(name) else "❌"
            console.print(f"  {status} {name}: {desc}")
    
    def is_available(self, provider):
        """Check if provider is available"""
        if provider == "ollama":
            return True
        elif provider == "openai":
            return bool(self.api_keys.get('openai'))
        elif provider == "claude":
            return bool(self.api_keys.get('anthropic'))
        return False
    
    def set_api_key(self, provider, api_key):
        """Set API key for a provider"""
        config_dir = os.path.expanduser("~/.darkeagle")
        os.makedirs(config_dir, exist_ok=True)
        config_file = f"{config_dir}/config.json"
        
        config = {}
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                config = json.load(f)
        
        if 'api_keys' not in config:
            config['api_keys'] = {}
        
        config['api_keys'][provider] = api_key
        
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        console.print(f"[green]✅ API key for {provider} saved![/]")

if __name__ == "__main__":
    ai = AIProvider("ollama")
    ai.list_providers()
    result = ai.query("What is OSINT?")
    print(result)
