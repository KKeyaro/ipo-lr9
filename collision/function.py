class RectCorrectError(Exception):
    pass


def isCorrectRect(coords):
    if len(coords) != 2:
        return False

    (x1, y1), (x2, y2) = coords

    return x1 < x2 and y1 < y2


def isCollisionRect(rect1, rect2):
    if not isCorrectRect(rect1):
        raise RectCorrectError("1й прямоугольник некорректный")
    if not isCorrectRect(rect2):
        raise RectCorrectError("2й прямоугольник некорректный")
    
    (x1_min, y1_min), (x1_max, y1_max) = rect1
    (x2_min, y2_min), (x2_max, y2_max) = rect2
    
    return not (x1_max < x2_min or x2_max < x1_min or y1_max < y2_min or y2_max < y1_min)


def intersectionAreaRect(rect1, rect2):
    if not isCorrectRect(rect1):
        raise ValueError("1й прямоугольник некорректный")
    if not isCorrectRect(rect2):
        raise ValueError("2й прямоугольник некорректный")
    
    if not isCollisionRect(rect1, rect2):
        return 0
    
    (x1_min, y1_min), (x1_max, y1_max) = rect1
    (x2_min, y2_min), (x2_max, y2_max) = rect2
    
    x_overlap = max(0, min(x1_max, x2_max) - max(x1_min, x2_min))
    y_overlap = max(0, min(y1_max, y2_max) - max(y1_min, y2_min))
    
    return x_overlap * y_overlap



