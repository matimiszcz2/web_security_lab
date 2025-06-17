# LFI.py
from flask import request, render_template
import os

def lfi_view():
    included_content = None
    message = ""

    page = request.args.get("page")  # Pobieramy parametr z URL np. ?page=about

    # # BEZPIECZNA WERSJA Z WHITELISTĄ
    #
    # # Słownik dozwolonych plików — tylko te można wczytać
    # allowed_pages = {
    #     "about": "pages/about.txt",
    #     "home": "pages/home.txt",
    #     "contact": "pages/contact.txt"
    # }
    #
    # if page:
    #     if page in allowed_pages:
    #         try:
    #             with open(allowed_pages[page], 'r', encoding='utf-8') as f:
    #                 included_content = f.read()
    #         except Exception as e:
    #             message = f"Błąd podczas wczytywania pliku: {e}"
    #     else:
    #         message = "Nieznana strona lub próba ataku LFI!"

    # NIEBEZPIECZNA WERSJA


    if page:
        try:
            # UWAGA: ta wersja jest PODATNA NA LFI!
            # Można np. wpisać:
            # /lfi?page=../../../../etc/passwd (Linux)
            # /lfi?page=../../../../Windows/system.ini (Windows)
            file_path = f"{page}.txt"  # Brak walidacji!
            with open(file_path, 'r', encoding='utf-8') as f:
                included_content = f.read()
        except Exception as e:
            message = f"Błąd podczas wczytywania pliku: {e}"


    return render_template("lfi.html", included_content=included_content, message=message)
