from flask import request, session, redirect, url_for, render_template_string, render_template


#wersja podatna - brak regeneracji, sesja może być przeklejona przez URL
def login_unsafe():
    if request.method == "POST":
        username = request.form.get("username")
        session["user"] = username #nie regenerujemy sesji
        #dla demonstracji: kopiujemy sid_from_url + user_session_id
        session['user_session_id'] = session.get('sid_from_url', 'brak')
        return redirect(url_for('profile_view'))

    return render_template_string('''
        <h2>Logowanie (podatne)</h2>
        <form method="post">
            <input name="username" placeholder="Nazwa użytkownika">
            <button>Zaloguj</button>
        </form>
        <p>Symuluj atak: dodaj ?sid=XYZ do URL przed logowaniem</p>
    ''')

#wersja bezpieczna - czysta sesja i regeneracja
def login_safe():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == 'admin' and password == 'admin':
            session.clear()                 # czyścimy starą sesję
            session.permanent = True        # aktywujemy trwałość
            session['user'] = username
            session['user_session_id'] = 'nowa_sesja'   # czysta ID
            return redirect(url_for('profile_view'))

    return render_template("SH.html", user=session.get('user'), sid=session.get('user_session_id'))


#widok profilu - pokazuje stan sesji i ewentualne przejecia
def profile_view():
    user = session.get('user')
    sid = session.get('user_session_id', 'brak')
    if user:
        return render_template_string(f'''
        <h2>Witaj, {user}!</h2>
        <p><strong>ID sesji użytkownika:</strong> {sid}</p>
        <a href="/logout">Wyloguj</a>
    ''')
    return redirect(url_for('login_unsafe'))

#wylogowanie
def logout_view():
    session.clear()
    return redirect(url_for('login_unsafe'))