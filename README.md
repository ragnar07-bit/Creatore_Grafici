# Creatore di Grafici per Risultati Partite

Questo piccolo programma prende in input il numero di partite vinte, pareggiate e perse e genera due grafici (istogramma e torta).

I file creati:
- `Main.py`: script principale (interattivo). Espone anche la funzione `create_charts(wins, draws, losses, save_path, show)` per test non interattivi.
- `requirements.txt`: dipendenza `matplotlib`.

Installazione e uso (PowerShell):

```powershell
python -m pip install -r requirements.txt
python Main.py
```

Esempio di uso non interattivo (da Python):

```python
from Main import create_charts
create_charts(10, 5, 2, save_path='grafico_test.png', show=False)
```

Il file immagine verrà salvato nella directory corrente come `grafico_partite.png` (o come specificato in `save_path`).