# Aplikacja edukacyjna: Demonstracja podatności webowych

Ten projekt demonstruje najczęstsze podatności aplikacji webowych. Każda strona prezentuje konkretny typ ataku, z prostym interfejsem i formularzem testowym.

## 🔍 Dostępne podatności

### 1. SQL Injection (`/sql`)
**Opis:** Atak polega na wstrzyknięciu złośliwego kodu SQL do zapytania wysyłanego do bazy danych. Jeśli dane użytkownika nie są odpowiednio filtrowane, napastnik może ominąć logowanie lub wyciągnąć dane z bazy.

### 2. Local File Inclusion – LFI (`/lfi`)
**Opis:** Pozwala użytkownikowi zażądać pliku z serwera, często z użyciem ścieżek względnych (`../`). Może prowadzić do odczytu poufnych plików systemowych.

### 3. Cross-Site Scripting – XSS (`/xss`)
**Opis:** Wstrzyknięcie kodu JavaScript do strony, który wykona się po stronie przeglądarki innego użytkownika. Może być użyte np. do kradzieży sesji.

### 4. CSRF – Cross-Site Request Forgery (`/csrf`)
**Opis:** Atak, w którym ofiara nieświadomie wysyła żądanie do aplikacji w imieniu napastnika (np. zmienia e-mail bez zgody użytkownika).

### 5. Session Hijacking / Fixation (`/sh`)
**Opis:** Atak polega na przejęciu sesji użytkownika poprzez manipulację identyfikatorem sesji (np. przekazanym w adresie URL).

---

## 🧭 Jak się poruszać po aplikacji?

- Po uruchomieniu serwera Flask przejdź do `http://localhost:5000/`
- Z głównej strony możesz przejść do każdej z podatności.
- Formularze są przygotowane do testów — możesz wpisywać dane ręcznie (np. payloady SQL Injection).
- Niektóre strony (np. LFI) używają parametru GET w URL — np. `?page=pages/home.txt`

---

## 💡 Dodatkowe informacje

Kod źródłowy każdej podatności zawiera komentarze opisujące:
- mechanizm działania ataku,
- sposób jego wykorzystania,
- oraz wersję bezpieczną (czasem zakomentowaną do porównania).

Zachęcamy do czytania kodu plików `.py` i `.html`, by lepiej zrozumieć działanie aplikacji i ryzyka bezpieczeństwa.

---

📁 Folder `db/users.db` zawiera przykładową bazę danych wykorzystywaną przez moduł SQL Injection.

---

✅ Projekt przeznaczony **wyłącznie do celów edukacyjnych**.
