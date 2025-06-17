from flask import request, render_template


def lfi_view(): # Tworzy funkcję widoku Flaska – ta funkcja będzie wywoływana, gdy użytkownik wejdzie na konkretną stronę, np. /lfi
    included_content = None #
    message = ""
    # Tworzy zmienne, które będą później przekazane do szablonu HTML:
    # included_content – zawartość wczytanego pliku (jeśli się uda)
    # message – komunikat błędu (jeśli coś pójdzie nie tak)

    page = request.args.get("page")  # Jeśli użytkownik wpisze http://localhost:5000/lfi?page=about, to page będzie równe "about"

    # # BEZPIECZNA WERSJA Z WHITELISTĄ
    #
    # # Słownik dozwolonych plików — tylko te można wczytać
    # allowed_pages = {
    #     "about": "pages/about.txt",
    #     "home": "pages/home.txt",
    #     "contact": "pages/contact.txt"
    # }
    # # Zamiast pozwalać użytkownikowi wczytać dowolny plik, mamy białą listę (whitelist) — czyli sami decydujemy, które pliki mogą być wczytane
    # if page:
    #     if page in allowed_pages:
    #         try:
    #             with open(allowed_pages[page], 'r', encoding='utf-8') as f:
    #                 included_content = f.read()
    #         except Exception as e:
    #             message = f"Błąd podczas wczytywania pliku: {e}"
    #     else:
    #         message = "Nieznana strona lub próba ataku LFI!"
    # # Jeśli wartość page znajduje się na białej liście – wtedy otwieramy konkretny, przypisany plik
    # # Bezpieczeństwo:
    # # Użytkownik nie ma możliwości wpisania ../../etc/passwd ani ścieżki do pliku .py – bo taka wartość nie jest w słowniku allowed_pages.
    # NIEBEZPIECZNA WERSJA

    if page:
        try:
            file_path = page  # bezpiecznie byłoby to sprawdzać!
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                included_content = f.read()
        except Exception as e:
            message = f"Błąd podczas wczytywania pliku: {e}"

    # Wartość parametru page jest bezpośrednio używana jako ścieżka do pliku. Czyli jeśli wpiszesz ?page=pages/about.txt,
    # to Python otworzy plik pages/about.txt.
    # Dlaczego to niebezpieczne?
    # Użytkownik może podać ścieżkę względną jak ../../../../etc/passwd (na Linuksie) lub
    # C:\\Windows\\system.ini (na Windowsie) i aplikacja spróbuje ten plik otworzyć.


    return render_template("lfi.html", included_content=included_content, message=message)


