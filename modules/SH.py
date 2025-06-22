from flask import request, session, redirect, url_for, render_template

# Widok logowania – podatny na Session Fixation
def login_view():
    if request.method == "POST":
        username = request.form.get("username")

        # Przypisanie użytkownika do sesji (bez regeneracji ID – podatność!)
        session['user'] = username

        # Symulowane przejęcie ID sesji z parametru URL (?sid=...)
        session['user_session_id'] = request.args.get('sid', 'brak')

        return redirect(url_for('profile_view'))  # Przekierowanie do profilu

    # Widok formularza logowania
    return render_template("SH.html", user=session.get('user'))

# Widok profilu – pokazuje przechwycony ID sesji oraz faktyczny ID sesji z cookie
def profile_view():
    user = session.get("user")
    sid = session.get("user_session_id", "brak")

    # Faktyczny ID sesji (z ciasteczka "session")
    real_session_id = request.cookies.get('session', 'brak')

    if user:
        return f"""
        <h1>Witaj, {user}!</h1>
        <p><strong>Przechwycone ID sesji (z URL):</strong> {sid}</p>
        <p><strong>Prawdziwe session cookie (Flask):</strong> {real_session_id}</p>
        <a href='/logout'>Wyloguj</a>
        """
    return redirect(url_for("login_view"))

# Wylogowanie – wyczyszczenie sesji
def logout_view():
    session.clear()
    return redirect(url_for("login_view"))
