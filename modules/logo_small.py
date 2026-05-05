#!/usr/bin/env python3
"""
🦅 Dark Eagle - Ultra Small Logo
"""

from rich.console import Console

console = Console()

def display_banner():
    console.print("""
╔══════════════════════════════════════════════════════════════════╗
║                         🦅 DARK EAGLE 🦅                          ║
║                   ┌─────────────────────────┐                    ║
║                   │      _.--""--_          │                    ║
║                   │   .-'  EAGLE  '-.       │                    ║
║                   │  :    WATCHES   :       │                    ║
║                   │   '-.______.-'         │                    ║
║                   └─────────────────────────┘                    ║
║              OSINT | Dark Web | AI | Image Analysis              ║
║                    ⚠️ Authorized Use Only ⚠️                     ║
╚══════════════════════════════════════════════════════════════════╝
""", style="bold cyan")

if __name__ == "__main__":
    display_banner()
