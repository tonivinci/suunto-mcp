import fitdecode

percorso = "data/corsa1.fit"
tipi = set()

with fitdecode.FitReader(percorso) as fit:
    for frame in fit:
        if frame.frame_type == fitdecode.FIT_FRAME_DATA:
            tipi.add(frame.name)
            
print(tipi)




