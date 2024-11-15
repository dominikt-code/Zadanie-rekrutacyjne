# Zadanie-rekrutacyjne
Opis działania aplikacji:

Aplikacja wczytuje treść z pliku artykul.txt.

Treść artykułu, wraz z odpowiednim promptem, jest przesyłana do API OpenAI w celu przetworzenia na kod HTML.

OpenAI zwraca kod HTML, który zawiera:

    Odpowiednią strukturę HTML (nagłówki, akapity, listy itp.).
    Miejsca na grafiki oznaczone tagami <img src="image_placeholder.jpg" alt="prompt do grafiki">.
    Podpisy pod grafikami.
    Zapis do pliku: Wygenerowany kod HTML jest zapisywany w pliku artykul.html.

Plik szablon.html pozwala na wizualizację treści przez wklejenie kodu do sekcji <body>.
Plik podglad.html jest pełnym podglądem artykułu, zawierającym stylizację i wygenerowany kod HTML.

Instrukcja uruchomienia:

W wierszu poleceń zainstaluj biblioteke openia:
pip install openai

W pliku głównym main.py w 3 linijce do openai.api_key przypisz swój klucz API

Uruchom program:
python main.py
