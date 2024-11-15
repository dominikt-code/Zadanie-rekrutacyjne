import openai

openai.api_key = "API_KEY" # Ustaw tutaj swój klucz API lub przekaż przez zmienną środowiskową

# Funkcja zwracająca zawartość wybranego pliku
def read_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return None
    
# Funkcja zapisująca tekst w wybranym pliku
def save(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated text saved in file {file_name}")

# Funkcja wykonywująca określony prompt
def generate(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},

        ]
    )

    return response['choices'][0]['message']['content']

# Prompty niezbędne do wykonania zadania
# Pompt tworzący pusty szablon HTML składający się z prostych znaczników
prompt_create_sheet = "Wygeneruj szablon HTML składający sie ze znaczników <html>, <body> i <head>. Kod powinien być gotowy do użycia i nie powinien zawierać dodatkowych oznaczeń ani komentarzy."
# Prompt wykonujący podstawowe zadanie, określenie miejsc gdzie warto wstawić grafiki i wstawianie odpowiednich tagów HTML do strukturyzacji danych
prompt_generate_content = "Użyj odpowiednich tagów HTML do strukturyzacji treści. Określ i wstaw w miejsce, gdzie warto wstawić grafiki tagiem <img src=\"image_placeholder.jpg\"> i dodaj atrybut alt do każdego obrazka z dokładnym promptem, który możemy użyć do wygenerowania grafiki. Umieśc podpisy pod grafikami używając odpowiedniego tagu HTML. Nie używaj CSS ani JavaScript. Zwrócony kod powinien zawierać wyłącznie zawartośc do wstawienia pomiędzy tagami <body> i </body>. Nie dołączaj znaczników <html>, <head>, ani <body>. Tekst artykułu: " + read_file("artykul.txt")
# Prompt wykonujący zadanied odatkowe, wkleja tekst do sekcji <body> w szablonie i opracowuje style CSS
prompt_insert_into_sheet = "Wklej tekst z artykułu do sekcji body w szablonie i opracuj style CSS i kod JS do wizualizacji tekstu. Kod powinien być gotowy do użycia i nie powinien zawierać dodatkowych oznaczeń ani komentarzy. Artykuł: " + read_file("artykul.html") + "\n Szablon: " + read_file("szablon.html")

# Zapisywanie wszystkich wygenerowanych promptów do konkretnych plików
save("szablon.html", generate(prompt_create_sheet))
save("artykul.html", generate(prompt_generate_content))
save("podglad.html", generate(prompt_insert_into_sheet))
