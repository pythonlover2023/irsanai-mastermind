import sys
import os
import atexit
from textual.app import App
from ui.interface import IrsanAITerminal

# Sicherstellen, dass wir Module finden
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def cleanup():
    """IrsanAI Cleanup Protocol: Kills zombie processes."""
    print("[IrsanAI] Shutting down factory processes...")
    # Hier würde der Code stehen, um Playwright sauber zu beenden
    pass

atexit.register(cleanup)

if __name__ == "__main__":
    # Windows Terminal Optimierung
    os.system("title IrsanAI | Real-Time Production Factory")
    
    app = IrsanAITerminal()
    app.run()

from router.router import LLMRouter
from bridge.proxy import ProxyBridge

class IrsanAITerminal(App):
    def __init__(self):
        super().__init__()
        self.router = LLMRouter()
        self.bridge = ProxyBridge()
        self.current_model = self.router.get_next_model()
