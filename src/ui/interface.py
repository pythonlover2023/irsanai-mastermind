from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, RichLog, Static, Button
from textual.containers import Container, Horizontal

class StatusDisplay(Static):
    """Zeigt verbundene LLMs an"""
    def compose(self) -> ComposeResult:
        yield Static("🔌 [bold green]Gemini: Ready[/] | 🔌 [bold yellow]Claude: Standby[/] | 🔋 [bold blue]Free Quota: 85%[/]")

class IrsanAITerminal(App):
    CSS = \"\"\"
    Screen { background: #0a0a12; }
    Header { color: #00f2ff; background: #1a1a2e; text-style: bold; }
    Input { dock: bottom; border: tall #7000ff; background: #000000; color: #00f2ff; }
    RichLog { background: #0e0e16; color: white; border: heavy #7000ff; }
    Button { background: #2d00f7; color: white; margin: 1; }
    Button:hover { background: #7000ff; }
    .status-bar { background: #1a1a2e; height: 3; padding: 1; border-bottom: solid #444; }
    \"\"\"

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True, title="IRSANAİ CLI | v1.0.0 [Shadow-Mode]")
        yield Container(StatusDisplay(), classes="status-bar")
        yield RichLog(highlight=True, markup=True, id="main_log")
        yield Input(placeholder="Befehl an die Factory senden (z.B. 'auth gemini' oder 'analyze @file.py')...")
        yield Footer()

    def on_mount(self) -> None:
        log = self.query_one(RichLog)
        log.write("[bold cyan]IrsanAI System initialisiert.[/]")
        log.write("[dim]Warte auf Verbindung zur lokalen Browser-Session...[/]")
        log.write("[bold magenta]Tipp: Nutze 'auth' um Browser-Cookies zu importieren.[/]")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        log = self.query_one(RichLog)
        cmd = event.value
        log.write(f"[bold yellow]USER >[/] {cmd}")
        event.input.value = ""
        
        # Simulierter Response (Später hier Bridge Logic)
        if cmd == "auth":
            log.write("[bold green]IrsanAI >[/] Öffne Browser für Authentifizierung...")
        elif cmd == "exit":
            self.exit()
        else:
            log.write("[bold cyan]IrsanAI >[/] Befehl empfangen. Orchestriere Antwort...")

        else:
            if cmd.startswith("mastermind"):
                log.write("[bold magenta]IrsanAI Mastermind >[/] Evolution gestartet – Teamwork auf Augenhöhe!")
                log.write("[dim]Aktuelles Modell: " + self.app.current_model + " | Analysiere Logs... Generiere Optimierungen...[/]")
                log.write("[bold green]Warte auf dein Okay: 'evolve yes' zum Fortfahren.[/]")
                # Hier kommt später der echte Loop (Analyse → Vorschläge → dein Okay → auto-commit)
            else:
                log.write("[bold cyan]IrsanAI >[/] Befehl empfangen. Routing zu " + self.app.current_model + "...")
