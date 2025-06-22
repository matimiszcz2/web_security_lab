from flask import Flask, render_template
from modules.sql import sql_injection_view
from modules.LFI import lfi_view
from modules.xss import xss_view
from modules.CSRF import csrf_view
from modules.SH import login_view, profile_view, logout_view

app = Flask(__name__)

#ustawienia klucza dla sesji
app.secret_key = 'MgrZaworskiBylNaErazmusie2137'

app.add_url_rule('/xss', view_func=xss_view, methods=['GET', 'POST'])
app.add_url_rule('/csrf', view_func=csrf_view, methods=['GET', 'POST'])
app.add_url_rule('/login', view_func=login_view, methods=['GET', 'POST'])
app.add_url_rule('/profile', view_func=profile_view, methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=logout_view, methods=['GET', 'POST'])

# Główna strona
@app.route('/')
def index():
    return render_template('index.html')

# Widok z SQL Injection
app.add_url_rule('/sql', view_func=sql_injection_view, methods=['GET', 'POST'])

@app.route("/lfi")
def lfi():
    return lfi_view()

if __name__ == '__main__':
    app.run(debug=True)