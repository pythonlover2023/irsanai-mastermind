import httpx
import browser_cookie3
from typing import Dict

class ProxyBridge:
    """Zero-API Bridge: Nutzt deine realen Browser-Cookies für direkte Requests"""
    def __init__(self, model: str = "gemini"):
        self.model = model.lower()
        self.client = httpx.AsyncClient(timeout=60.0)
        self.cookies = self.load_cookies()

    def load_cookies(self) -> Dict:
        """Lädt Cookies aus Chrome (Android/Windows) – passe bei Bedarf auf firefox() um"""
        try:
            return browser_cookie3.chrome(domain_name=self.get_domain())
        except:
            return {}

    def get_domain(self) -> str:
        domains = {
            "gemini": "gemini.google.com",
            "claude": "claude.ai",
            "chatgpt": "chat.openai.com",
            "grok": "grok.x.ai",
            "mistral": "chat.mistral.ai",
            "deepseek": "chat.deepseek.com",
            "qwen": "chat.qwen.ai",
            # Ergänze deine anderen...
        }
        return domains.get(self.model, "gemini.google.com")

    async def send_prompt(self, prompt: str, history: list = None) -> str:
        """Placeholder – hier kommt das reverse-engineerte Endpoint rein"""
        # Beispiel für Gemini (muss via DevTools angepasst werden)
        url = "https://gemini.google.com/v1/chat"  # Real: echtes Backend finden!
        payload = {"prompt": prompt, "history": history or []}
        response = await self.client.post(url, cookies=self.cookies, json=payload)
        if response.status_code == 200:
            return response.json().get("response", "Error: No response")
        return f"Error: {response.status_code} – {response.text}"
