import sqlite3

def crea_tabella():
    connessione = sqlite3.connect("data/allenamenti.db")
    connessione.execute("""CREATE TABLE IF NOT EXISTS allenamenti (
        id INTEGER PRIMARY KEY,
        inizio TEXT UNIQUE,
        sport TEXT,
        distanza REAL,
        durata REAL,
        battito_medio INTEGER,
        battito_max INTEGER,
        velocita_media REAL,
        dislivello INTEGER,
        calorie INTEGER
    )""")
    connessione.commit()
    connessione.close()


if __name__ == "__main__":
    crea_tabella()

def salva_allenamento(scheda):
    connessione = sqlite3.connect("data/allenamenti.db")
    connessione.execute("""INSERT OR IGNORE INTO allenamenti (
        inizio, sport, distanza, durata, battito_medio, battito_max,
        velocita_media, dislivello, calorie
    ) VALUES (:inizio, :sport, :distanza, :durata, :battito_medio, :battito_max, :velocita_media, :dislivello, :calorie)""", scheda)
    connessione.commit()
    connessione.close()