# Geotodle

Stworzenie aplikacji edukacyjnej z wykorzystaniem narzędzi takich jak Three.js czy Plotly stało się dla Nas w tym semestrze celem zarówno poprzez możliwość nauczenia się użytecznych technologii jak i stworzenie aplikacji która będzie dopracowana w jak największej ilości obszarów oraz będzie gwarantowała prostą obsługę każdemu użytkownikowi.

### Wybór danych

Zdecydowaliśmy się na dane reprezentujące predykcję ludności do roku 2060 oraz procent bezrobocia rejestrowanego wśród meiszkańców danego miasta. Przy wyborze wzięliśmy pod uwagę to jakie zbiory są ciekawe w kontekście wizualizacji, jakie zbiory pasują do naszego projektu oraz ilość danych w nich zawartych.
\n
Danych szukaliśmy na platformie kaggle oraz na stronach rządowych, takich jak [GUS](https://bdl.stat.gov.pl/bdl/dane/teryt/jednostka). Wybierając konkretne typy danych *(np. wśród grupy 'rynek pracy' zaznaczyliśmy 'bezrobocie rejestrowane')* mogliśmy pobrać pełne dane dla danego miasta zapisane w pliku .csv lub .xlsx.

### Obróbka danych

Dla ułatwienia procesu szukania danych oraz optymalizacji wielkości projektu, przenieśliśmy interesujące nas dane do jednego arkusza kalkulacyjnego excel o rozszerzeniu .xlsx, który to został podzielony na arkusze nazwane nazwami miast których dane reprezentował. Ułatwiło nam to stworzenie wykresów w jednym pliku Python.

```
# Wczytujemy arkusz Excel
excel_file = 'predykcjaLudnosci2060.xlsx'

# Odczytujemy wszystkie arkusze
arkusze = pd.read_excel(excel_file, sheet_name=None)

# Teraz 'arkusze' jest słownikiem, w którym kluczami są nazwy arkuszy, a wartościami są DataFrame'y Pandas
arkusz_data = arkusze['Gliwice']
print(arkusz_data)
```

Wynikiem tej operacji są dane:
|   Lata  |  Ogółem  | Jednostka | osoba |
|---------|----------|-----------|-------|
|   2022  |  113223  |   2003.0  |  0.0  |
|   2023  |  112973  |   2004.0  |  0.0  |
|   2024  |  112713  |   2005.0  |  0.0  |
|   2025  |  112429  |   2006.0  | 4757.0|
|   2026  |  112134  |   2007.0  | 2686.0|
|   2027  |  112067  |   2008.0  | 1257.0|
|   2028  |  112098  |   2009.0  | 1076.0|
|   2029  |  111905  |   2010.0  | 1394.0|
|   2030  |  111603  |   2011.0  | 1947.0|

### Tworzenie wykresów

### Tworzenie modeli

### Działanie aplikacji

### Uruchamianie aplikacji

```bash
npm run dev
```

format apki

```bash
npm run format
```
