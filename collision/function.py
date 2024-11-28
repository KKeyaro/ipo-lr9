def isCorrectRect(coords):
    if len(coords) != 2:
        return False

    (x1, y1), (x2, y2) = coords

    return x1 < x2 and y1 < y2


