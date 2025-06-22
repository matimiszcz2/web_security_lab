from flask import request, render_template

# Symulacja bazy danych z e-mailem użytkownika
email_db = {"admin": "admin@example.com"}

# Widok podatny na CSRF
def csrf_view():
    message = ""
    if request.method == "POST":
        # Pobieramy nowy adres e-mail z formularza
        new_email = request.form.get("email")
        # Nadpisujemy istniejący e-mail bez żadnej weryfikacji
        email_db["admin"] = new_email
        message = f"Zmieniono e-mail na: {new_email}"
    # Przekazujemy komunikat o zmianie do szablonu
    return render_template("CSRF.html", message=message)
