from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, RichLog, Static
from textual.containers import Container

class StatusDisplay(Static):
    """Zeigt verbundene LLMs an"""
    def compose(self) -> ComposeResult:
        yield Static("🔌 [bold green]Gemini: Ready[/] | 🔌 [bold yellow]Claude: Standby[/] | 🔋 [bold blue]Free Quota: 85%[/]")

class IrsanAITerminal(App):
    CSS = """
    Screen { background: #0a0a12; }
    Header { color: #00f2ff; background: #1a1a2e; text-style: bold; }
    Input { dock: bottom; border: tall #7000ff; background: #000000; color: #00f2ff; }
    RichLog { background: #0e0e16; color: white; border: heavy #7000ff; }
    .status-bar { background: #1a1a2e; height: 3; padding: 1; border-bottom: solid #444; }
    """

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)  # Kein title mehr hier
        yield Container(StatusDisplay(), classes="status-bar")
        yield RichLog(highlight=True, markup=True, id="main_log")
        yield Input(placeholder="Befehl an das Mastermind (z.B. 'mastermind evolve' oder normaler Prompt)...")
        yield Footer()

    def on_mount(self) -> None:
        log = self.query_one(RichLog)
        log.write("[bold cyan]IrsanAI Mastermind initialisiert.[/]")
        log.write("[dim]Warte auf Verbindung zu deinen Free-Tier LLMs (Proxy ready)...[/]")
        log.write("[bold magenta]Tipp: 'mastermind evolve' für den Selbst-Optimierungs-Loop.[/]")
        # Current Model aus Router (falls init)
        log.write(f"[dim]Start-Modell: {getattr(self, 'current_model', 'gemini')}[/]")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        log = self.query_one(RichLog)
        cmd = event.value.strip()
        log.write(f"[bold yellow]CAPTAIN >[/] {cmd}")
        event.input.value = ""

        if cmd.lower().startswith("mastermind evolve"):
            log.write("[bold magenta]IrsanAI Mastermind >[/] Evolution gestartet – Teamwork auf Augenhöhe!")
            log.write(f"[dim]Aktuelles Modell: {getattr(self, 'current_model', 'gemini')} | Logs analysieren... Vorschläge generieren...[/]")
            log.write("[bold green]Bereit für erste Optimierung. Warte auf 'evolve yes' zum Fortfahren.[/]")
            # Hier kommt später der echte Loop
        else:
            log.write(f"[bold cyan]IrsanAI >[/] Befehl empfangen. Routing zu {getattr(self, 'current_model', 'gemini')}... (Response kommt bald)")
            # Placeholder für Proxy-Call
