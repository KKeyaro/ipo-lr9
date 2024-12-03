from collision.function import( 
    isCorrectRect,
    isCollisionRect, 
    intersectionAreaRect, 
    intersectionAreaMultiRect, 
    RectCorrectError 
    )


print(f"Корректно ли введены результаты? {isCorrectRect([(-3.4, 1),(9.2, 10)])}") 
print(f"Корректно ли введены результаты? {isCorrectRect([(-7, 9),(3, 6)])}") 


print(f"Пересекаются ли прямоугольники? {isCollisionRect([(-3.4, 1),(9.2, 10)], [(-7.4, 0),(13.2, 12)])}") 
print(f"Пересекаются ли прямоугольники? {isCollisionRect([(1, 1),(2, 2)], [(3, 0),(13, 1)])}")

try: 
    print(f"Пересекаются ли прямоугольники? {isCollisionRect([(1, 1),(2, 2)], [(3, 17),(13, 1)])}") 
except RectCorrectError as e: 
    print(e) 


print(f"Площадь пересечения: {intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)])}")
print(f"Площадь пересечения: {intersectionAreaRect([(1, 1), (2, 2)], [(3, 0), (13, 1)])}") 


try: 
    print(f"Площадь пересечения: {intersectionAreaRect([(1, 1), (2, 2)], [(3, 17), (13, 1)])}") 
except ValueError as e: 
    print(e) 


rects = [ 
    [(-3, 1), (9, 10)], 
    [(-7, 0), (13, 12)], 
    [(0, 0), (5, 5)], 
    [(2, 2), (7, 7)] 
] 
print(f"Общая площадь пересечения: {intersectionAreaMultiRect(rects)}") 

rects2 = [ 
    [(-3, 1), (9, 10)], 
    [(3, 17), (13, 1)]
] 
try: 
    print(f"Общая площадь пересечения: {intersectionAreaMultiRect(rects2)}") 
except RectCorrectError as e: 
    print(e)
