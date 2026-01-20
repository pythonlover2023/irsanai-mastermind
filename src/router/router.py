import json
import os

class LLMRouter:
    """Orchestriert bis zu 10 LLMs + Quota-Tracking"""
    def __init__(self, config_file: str = "config/llms.json"):
        self.config_file = config_file
        self.llms = self.load_config()
        os.makedirs("config", exist_ok=True)

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file) as f:
                return json.load(f)
        # Default: 10 Slots (passe deine Modelle an)
        default = [
            {"name": "gemini", "quota_left": 100},
            {"name": "claude", "quota_left": 100},
            {"name": "chatgpt", "quota_left": 100},
            {"name": "grok", "quota_left": 100},
            {"name": "mistral", "quota_left": 100},
            {"name": "deepseek", "quota_left": 100},
            {"name": "qwen", "quota_left": 100},
            # Füge bis 10 hinzu...
        ]
        return {f"slot_{i}": default[i % len(default)] for i in range(10)}

    def get_next_model(self) -> str:
        """Wählt das Modell mit meiste Quota"""
        best = max(self.llms.values(), key=lambda x: x["quota_left"])
        return best["name"]

    def update_quota(self, model: str, used: int = 15):
        for slot in self.llms.values():
            if slot["name"] == model:
                slot["quota_left"] = max(0, slot["quota_left"] - used)

    def save_config(self):
        with open(self.config_file, "w") as f:
            json.dump(self.llms, f, indent=4)
