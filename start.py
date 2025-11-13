#!/usr/bin/env python3
"""
AiElon FusionHD Startup Script
Initializes and starts the complete AiElon FusionHD system
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.system_integration import main

if __name__ == "__main__":
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║                                                            ║
    ║              AiElon FusionHD System                        ║
    ║              Version 1.0.0                                 ║
    ║                                                            ║
    ║  AiElon Living OS • Fusion HD UI • Halal Wallet           ║
    ║  HCare • Ummah Hub                                        ║
    ║                                                            ║
    ╚════════════════════════════════════════════════════════════╝
    """)
    
    exit(main())
