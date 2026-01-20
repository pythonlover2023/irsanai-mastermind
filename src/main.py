import sys
import os
import atexit
from textual.app import App

# Sicherstellen, dass wir Module finden
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.interface import IrsanAITerminal

def cleanup():
    print("[IrsanAI] Shutting down factory processes...")
    # Hier später echte Cleanup-Logic (z. B. Proxy close)

atexit.register(cleanup)

if __name__ == "__main__":
    app = IrsanAITerminal()
    app.title = "IRSANAİ MASTERMIND | v0.1 [Evolution Mode]"  # Title hier setzen
    app.run()
