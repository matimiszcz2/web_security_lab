from flask import Flask, render_template, session, request
from modules.sql import sql_injection_view
from modules.LFI import lfi_view
from modules.session_demo import login_view as demo_login, profile_view as demo_profile
from modules.session_hijack_demo import(
    login_unsafe,
    login_safe,
    profile_view as hijack_profile,
    logout_view
)

app = Flask(__name__)

#ustawienia klucza dla sesji
app.secret_key = 'MgrZaworskiBylNaErazmusie2137'

app.add_url_rule('/login', view_func=demo_login(), methods=['GET', 'POST'])
app.add_url_rule('/profile', view_func=demo_profile(), methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=logout_view())
app.add_url_rule('/login-unsafe', view_func=login_unsafe(), methods=['GET', 'POST'])
app.add_url_rule('login-safe', view_func=login_safe(), methods=['GET', 'POST'])
app.add_url_rule('/profile-hijack', view_func= hijack_profile())

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
