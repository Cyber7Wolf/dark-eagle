#!/usr/bin/env python3
"""
🦅 Dark Eagle - ASCII Art Logo Module
"""

import random
from rich.console import Console
from rich.panel import Panel

console = Console()

def get_eagle_logo():
    """Return different eagle ASCII art variants"""
    
    logos = [
        # Logo 1 - Classic Eagle
        """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║                                    ,....,                                     ║
║                               ,ad88'  `'Y8ba,                                 ║
║                            ,d8P"'         `"Y8b,                              ║
║                          ,d8"                 "8b,                            ║
║                         d8'      ,adPPba,       `8b                           ║
║                        88      d8'    `'8b       88                           ║
║                        88      88       "8b      88                           ║
║                        88      88        Y8      88                           ║
║                        88      88        88      88                           ║
║                        88      88        88      88                           ║
║                        Y8      88       ,8P      Y8                           ║
║                         `8b     `8ba, ,ad8'      d8'                           ║
║                          `Y8,     `"Y88P"      ,8P'                            ║
║                            `"Y8ba,          ,ad8"'                             ║
║                                `"Y888888888P"'                                 ║
║                                                                                ║
║                         🦅 DARK EAGLE OSINT FRAMEWORK 🦅                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """,
        
        # Logo 2 - Cyber Eagle
        """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║                           ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ ║
║                          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌ ║
║                          ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ║
║                          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌ ║
║                          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌ ║
║                          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌ ║
║                          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌ ║
║                          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌ ║
║                          ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ ║
║                          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌ ║
║                           ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ║
║                                                                                ║
║                      ██████╗  █████╗ ██████╗ ██╗  ██╗                          ║
║                      ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝                          ║
║                      ██║  ██║███████║██████╔╝█████╔╝                           ║
║                      ██║  ██║██╔══██║██╔══██╗██╔═██╗                           ║
║                      ██████╔╝██║  ██║██║  ██║██║  ██╗                          ║
║                      ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝                          ║
║                                                                                ║
║                         🦅 DARK EAGLE OSINT FRAMEWORK 🦅                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """,
        
        # Logo 3 - Minimal Eagle
        """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║                                    .,,                                         ║
║                                .;llc;'.                                       ║
║                              .:odddddoc'                                      ║
║                             'cdddddddddc.                                     ║
║                            .ldddddddddddl.                                    ║
║                           .cdddddddddddddc.                                   ║
║                          'ldddddddddddddddl.                                  ║
║                         .ldddddddddddddddddc.                                 ║
║                        .cdddddddddddddddddddl.                                ║
║                       .oddddddddddddddddddddd:                                ║
║                       oooooooooooooooooooooooo                                ║
║                       ░░░░░░░░░░░░░░░░░░░░░░░░                                ║
║                                                                                ║
║                    ░██████╗░░█████╗░██████╗░██╗░░██╗                          ║
║                    ██╔════╝░██╔══██╗██╔══██╗██║░██╔╝                          ║
║                    ██║░░██╗░███████║██████╔╝█████═╝░                          ║
║                    ██║░░╚██╗██╔══██║██╔══██╗██╔═██╗░                          ║
║                    ╚██████╔╝██║░░██║██║░░██║██║░╚██╗                          ║
║                    ░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝                          ║
║                                                                                ║
║                         🦅 DARK EAGLE OSINT FRAMEWORK 🦅                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """,
    ]
    
    # Return random logo variant
    return random.choice(logos)

def display_banner():
    """Display the Dark Eagle banner with logo"""
    console = Console()
    
    # Get and display logo
    logo = get_eagle_logo()
    console.print(logo, style="bold cyan")
    
    # Add additional info
    info_panel = Panel(
        "[bold cyan]Advanced OSINT Framework[/]\n"
        "[dim]100+ Platforms | Dark Web | AI Analysis | Image Intelligence[/]\n\n"
        "[yellow]⚠️ Authorized Use Only ⚠️[/]",
        title="🦅 Dark Eagle Ultimate",
        border_style="cyan"
    )
    console.print(info_panel)
    
    return logo

if __name__ == "__main__":
    display_banner()
