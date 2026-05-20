import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
METRICS_PATH = os.path.join(BASE_DIR, "logs", "metrics.txt")
HTML_OUTPUT = os.path.join(BASE_DIR, "web", "index.html")

def build_dashboard():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Começa a montar a string do HTML (Unindo Python com HTML/CSS)
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>NetPulse Infrastructure Status</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #1e1e2e; color: #cdd6f4; margin: 40px; }}
            h1 {{ color: #89b4fa; text-align: center; }}
            .timestamp {{ text-align: center; color: #a6adc8; margin-bottom: 30px; }}
            .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; max-width: 1000px; margin: 0 auto; }}
            .card {{ background-color: #313244; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); text-align: center; }}
            .ONLINE {{ border-top: 5px solid #a6e3a1; }}
            .OFFLINE {{ border-top: 5px solid #f38ba8; }}
            .status {{ font-weight: bold; font-size: 1.2em; }}
            .status.ONLINE {{ color: #a6e3a1; }}
            .status.OFFLINE {{ color: #f38ba8; }}
        </style>
    </head>
    <body>
        <h1>NetPulse Live Infrastructure Dashboard</h1>
        <div class="timestamp">Last Scan: {now}</div>
        <div class="grid">
    """
    
    # Lê as métricas geradas pelo Shell
    if os.path.exists(METRICS_PATH):
        with open(METRICS_PATH, "r") as f:
            lines = f.readlines()
            
        for line in lines:
            name, host, status, latency = line.strip().split("|")
            
            # Adiciona um card HTML dinâmico para cada servidor
            html_content += f"""
            <div class="card {status}">
                <h3>{name}</h3>
                <p style="color: #bac2de;">{host}</p>
                <p class="status {status}">{status}</p>
                <p>Latency: {latency} ms</p>
            </div>
            """
            
    # Fecha as tags do HTML
    html_content += """
        </div>
    </body>
    </html>
    """
    
    # Grava o arquivo HTML final
    with open(HTML_OUTPUT, "w") as f:
        f.write(html_content)
    print(f"[PYTHON SUCCESS] Live Dashboard updated at: {HTML_OUTPUT}")

if __name__ == "__main__":
    build_dashboard()