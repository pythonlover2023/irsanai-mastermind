import sys
import os
import atexit
from textual.app import App
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.interface import IrsanAITerminal
from router.router import LLMRouter
from bridge.proxy import ProxyBridge

def cleanup():
    print("[IrsanAI] Shutting down factory processes...")

atexit.register(cleanup)

class MastermindApp(IrsanAITerminal):
    def __init__(self):
        super().__init__()
        self.router = LLMRouter()
        self.bridge = ProxyBridge()
        self.current_model = self.router.get_next_model()
        self.log_file = "logs/session.log"
        self.write_log("Mastermind started")

    def write_log(self, message: str):
        timestamp = datetime.now().strftime("%H:%M:%S")
        with open(self.log_file, "a") as f:
            f.write(f"[{timestamp}] {message}\n")

if __name__ == "__main__":
    app = MastermindApp()
    app.title = "IRSANAİ MASTERMIND | v0.1 [Evolution Mode]"
    app.run()
