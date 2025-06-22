from flask import request, session, redirect, url_for, render_template

def login_view():
    if request.method == 'POST':
        username = request.form.get('username')
        if username == 'admin':
            session.permanent = True
            session['user'] = username
            return redirect(url_for('profile_view'))

    # ⬇️ Tu renderujesz stronę logowania
    return render_template('session_demo.html')

def profile_view():
    user = session.get('user')
    if user:
        return f"Siema, {user}!"
    return "Nie jesteś zalogowany"