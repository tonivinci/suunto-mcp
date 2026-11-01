import fitdecode

def leggi_sessione(percorso):
    dati = {}
    with fitdecode.FitReader(percorso) as fit:
        for frame in fit:
            if frame.frame_type == fitdecode.FIT_FRAME_DATA and frame.name == "session":
                dati["sport"] = frame.get_value("sport")
                dati["distanza"] = frame.get_value("total_distance")
                dati["inizio"] = frame.get_value("start_time").isoformat()
                dati["durata"] = frame.get_value("total_timer_time")
                dati["battito_medio"] = frame.get_value("avg_heart_rate")
                dati["battito_max"] = frame.get_value("max_heart_rate")
                dati["velocita_media"] = frame.get_value("enhanced_avg_speed")
                dati["dislivello"] = frame.get_value("total_ascent")
                dati["calorie"] = frame.get_value("total_calories")

    return dati


if __name__ == "__main__":
    risultato = leggi_sessione("data/corsa1.fit")
    print(risultato) 
