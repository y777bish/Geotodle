import pandas as pd
import plotly.express as px
import chart_studio.plotly as py

username = 'bartsmo430'  # Twoja nazwa użytkownika
api_key = 'bzsfPDm7XI9ycRmHrC8n'  # Twój klucz API

file_path = 'predykcjaLudnosci2060.xlsx'

miasta = ["Gliwice", "Kędzierzyn-Koźle", "Ruda Śląska", "Zamość", "Warszawa", "Zakopane", "Szczecin"]

# Wykresy dla predykcji ludności
for miasto in miasta:
    data_miasto = pd.read_excel(file_path, sheet_name=miasto)
    
    # Twórz wykres słupkowy
    fig_miasto = px.bar(data_miasto, x='Lata', y='Ogółem', color_discrete_sequence=['orange'])
    fig_miasto.update_layout(
        title=f'Wykres słupkowy obrazujący predykcję ludności do roku 2060 dla miasta: {miasto}',
        xaxis_title='Lata',
        yaxis_title='Ilość osób',
        width=800,
        height=300,
        yaxis_range=[30000, 160000],
        plot_bgcolor='#242424',  # Tło wykresu na czarno
        paper_bgcolor='#242424',  # Tło całego wykresu na ciemnoszare
        font=dict(color='white'),  # Kolor czcionki na biały
    )
    fig_miasto.update_layout(bargap=0.3)

    # Twórz wykres z trendlinią
    trend_fig = px.scatter(data_miasto, x='Lata', y='Ogółem', trendline='ols')
    
    # Nakładanie linii trendu na wykres słupkowy
    for trace in trend_fig.data:
        trace.mode = 'lines'
        trace.y = [y + 8000 for y in trace.y]
        fig_miasto.add_trace(trace)

    if miasto == "Warszawa":
        fig_miasto.update_layout(
            yaxis_range=[1500000, 2300000]
        )

    if miasto == "Szczecin":
        fig_miasto.update_layout(
            yaxis_range=[200000, 480000]
        )

    if miasto == "Zamość":
        fig_miasto.update_layout(
            yaxis_range=[10000, 160000]
        )
    
    fig_miasto.show()

# Wykresy dla bezrobocia
for miasto in miasta:
    data_miasto = pd.read_excel(file_path, sheet_name=miasto)
    
    # Twórz wykres słupkowy
    fig_miasto_bezrobocie = px.bar(data_miasto, x='Jednostka', y='osoba', color_discrete_sequence=['orange'])
    fig_miasto_bezrobocie.update_layout(
        title=f'Wykres słupkowy obrazujący ilość bezrobocia zarejstrowanego w mieście: {miasto}',
        xaxis_title='Lata',
        yaxis_title='Ilość osób',
        width=800,
        height=300,
        yaxis_range=[0, 3000],
        plot_bgcolor='#242424',  # Tło wykresu na czarno
        paper_bgcolor='#242424',  # Tło całego wykresu na ciemnoszare
        font=dict(color='white'),  # Kolor czcionki na biały
    )

    if miasto == "Warszawa":
        fig_miasto_bezrobocie.update_layout(
            yaxis_range=[0, 40000]
        )

    if miasto == "Gliwice":
        fig_miasto_bezrobocie.update_layout(
            yaxis_range=[0, 6000]
        )

    if miasto == "Szczecin":
        fig_miasto_bezrobocie.update_layout(
            yaxis_range=[0, 13000]
        )
    
    fig_miasto_bezrobocie.show()

# Prześlij wykres na swoje konto w Chart Studio
# py.plot(fig, filename='nazwa-wykresu', username=username, api_key=api_key)