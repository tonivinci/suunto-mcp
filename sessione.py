import fitdecode

percorso = "data/corsa1.fit"

with fitdecode.FitReader(percorso) as fit:
    for frame in fit:
        if frame.frame_type == fitdecode.FIT_FRAME_DATA and frame.name == "session":
            for campo in frame.fields:
                print (campo.name, campo.value, campo.units)