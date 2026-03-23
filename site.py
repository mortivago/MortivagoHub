import psutil
from flask import Flask, render_template

app = Flask(__name__)

# Função para checar se o bot está rodando
def get_bot_status():
    for proc in psutil.process_iter(['cmdline']):
        try:
            if proc.info['cmdline'] and any('bot.py' in s for s in proc.info['cmdline']):
                return "online"
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return "offline"

@app.route('/')
def index():
    status = get_bot_status()
    return render_template('index.html', status=status)

# ESSA É A ROTA QUE ESTAVA FALTANDO (O erro da imagem):
@app.route('/mortiscan')
def mortiscan_page():
    status = get_bot_status()
    return render_template('mortiscan.html', status=status)

@app.route('/portfolio/<lang>')
def portfolio(lang):
    return render_template('portfolio.html', lang=lang)

if __name__ == '__main__':
    app.run(port=5000, debug=True)