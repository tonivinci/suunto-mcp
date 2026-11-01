from pathlib import Path
from fit_reader import leggi_sessione
from database import crea_tabella, salva_allenamento

cartella = Path("data")

crea_tabella()
for file in sorted(cartella.glob("*.fit")):
    scheda = leggi_sessione(file)
    salva_allenamento(scheda)
    print("Importato:", file)
    
