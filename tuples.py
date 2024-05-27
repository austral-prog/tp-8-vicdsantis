def get_coordinate(record):
    return record [-1]

def convert_coordinate(coordinate):
    x = coordinate [0]
    y = coordinate [1]
    return (f"{x}", f"{y}")


def create_record(azara_record, rui_record):
    coordenada_1 = azara_record [-1]
    x1 = coordenada_1 [0]
    y1 = coordenada_1 [-1]

    coordenada_2 = rui_record [-2]
    x2 = coordenada_2 [0]
    y2 = coordenada_2 [-1]
    
    if x1 == x2 and y1 == y2:
        return azara_record + rui_record

    else:
        return "not a match"
