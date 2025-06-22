from flask import request, render_template

# Prosta lista komentarzy (symuluje bazę danych)
comments = []

# Widok XSS – pozwala dodawać komentarze
def xss_view():
    global comments
    if request.method == "POST":
        # Pobieramy komentarz z formularza
        comment = request.form.get("comment")
        comments.append(comment)  # Dodajemy bez żadnej filtracji (intencjonalnie)
    # Renderujemy widok i przekazujemy listę komentarzy
    return render_template("xss.html", comments=comments)