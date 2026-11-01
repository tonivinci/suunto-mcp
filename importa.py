from fit_reader import leggi_sessione
from database import crea_tabella, salva_allenamento

crea_tabella()
scheda = leggi_sessione("data/corsa2.fit")
salva_allenamento(scheda)