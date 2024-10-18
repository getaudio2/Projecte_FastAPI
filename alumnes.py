def alumne_schema(alumne) -> dict:
    return {"idAlumne": alumne[0],
            "idAula": alumne[1],
            "nomAlumne": alumne[2],
            "cicle": alumne[3],
            "curs": alumne[4],
            "grup": alumne[5]
            }

def alumnes_schema(alumnes) -> dict:
    return [alumne_schema(alumne) for alumne in alumnes]

def alumnesYAules_schema(alumnesYAules) -> dict:
    return [alumneYAula(alumne) for alumne in alumnesYAules]

def alumneYAula(alumnesYAules) -> dict:
    return {"idAlumne": alumnesYAules[0],
            "idAula": alumnesYAules[1],
            "nomAlumne": alumnesYAules[2],
            "cicle": alumnesYAules[3],
            "curs": alumnesYAules[4],
            "grup": alumnesYAules[5],
            "descAula": alumnesYAules[7],
            "edifici": alumnesYAules[8],
            "pis": alumnesYAules[8]
    }