from flask import request, render_template
import sqlite3
import os

def sql_injection_view(): # Definiujemy funkcję, która będzie pełnić rolę widoku w Flasku — tzn. obsłuży zapytania na trasie /sql
    message = "" # Zmienna message to informacja, która zostanie przekazana do szablonu HTML — np. "Zalogowano pomyślnie", albo "Błędny login"
    db_path = os.path.join("db", "users.db") #  Tworzymy ścieżkę do pliku bazy danych. Dzięki os.path.join() będzie działać poprawnie zarówno na Windows, jak i Linuxie/Macu

    if request.method == 'POST': # Sprawdzamy, czy użytkownik wysłał formularz (czyli metoda HTTP to POST). Jeśli nie — formularz będzie tylko wyświetlony, bez logiki logowania
        username = request.form['username']
        password = request.form['password']
        # request.form — to słownik z polami formularza (name="username" i name="password")
        # Dane są tekstowe

        # UWAGA
        # PODATNA wersja: niebezpieczne łączenie zapytania SQL
        conn = sqlite3.connect(db_path) # Nawiązujemy połączenie z bazą danych (plikiem db/users.db). Zmienna conn to obiekt połączenia
        c = conn.cursor() # Tworzymy tzw. kursor — obiekt, który wykonuje zapytania SQL w tej bazie

        try: # Rozpoczynamy blok try, żeby w razie błędów zapytania nie wysypać całej aplikacji (np. gdy zapytanie będzie miało błędną składnię SQL)

            # Najważniejsza linia – tutaj jest podatność na SQL Injection:
            query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
            # Składamy zapytanie SQL z danych użytkownika bez żadnej walidacji
            # Jeśli ktoś wpisze np. username = ' OR 1=1 --, to zostanie to wstrzyknięte do zapytania jako
            # username = "' OR 1=1 --"
            # password = "cokolwiek"
            # A zapytanie wysłane do serwera wygląda tak:
            # SELECT * FROM users WHERE username = '' OR 1=1 --' AND password = 'cokolwiek'
            # SELECT * FROM users WHERE (username = '') OR (1=1); zawsze da prawde więc
            # -- oznacza komentarz, więc AND password = '...' zostaje zignorowane!
            # Warunek 1=1 jest zawsze prawdziwy → logowanie się udaje!




            print("Wykonuję zapytanie:", query) # Debug — wypisujemy zapytanie, żeby móc zobaczyć w terminalu, co dokładnie zostało wykonane
            c.execute(query) # Wykonujemy zapytanie SQL
            result = c.fetchone() # Odczytujemy pierwszy wynik zapytania (jeśli istnieje). Jeśli coś zostało znalezione — oznacza to,
            # że login i hasło „pasują” (albo: zapytanie zostało zmanipulowane i zwraca dane mimo błędnych loginu i hasła).
            if result: # Jeśli wynik istnieje (czyli użytkownik został "znaleziony"), pokazujemy komunikat o sukcesie i wypisujemy jego login (zakładamy, że result[1] to nazwa użytkownika)
                message = "Zalogowano pomyślnie jako " + result[1] # Jeśli fetchone() nie zwróciło nic — informujemy, że dane są błędne
            else:
                message = "Błędny login lub hasło"
        except Exception as e: # Jeśli wystąpił wyjątek (np. błędna składnia SQL, zła baza), wyświetlamy komunikat z opisem błędu
            message = "Błąd zapytania: " + str(e)

        conn.close() # Zawsze zamykamy połączenie z bazą danych, niezależnie od wyniku

    return render_template('sql.html', message=message)
