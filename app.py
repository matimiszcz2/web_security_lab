from flask import Flask, render_template
from modules.sql import sql_injection_view

app = Flask(__name__)

# Główna strona
@app.route('/')
def index():
    return render_template('index.html')

# Widok z SQL Injection
app.add_url_rule('/sql', view_func=sql_injection_view, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True)
