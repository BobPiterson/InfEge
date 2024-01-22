count = 0
# 1. перебираем все точки в прямоугольнике 10х20 (левый угол в точке 1,1), в который с запасом помещается ромб
for x in range(1, 20):
    for y in range(1, 10):
        # 2. проверяем условие попадания точки в область, ограниченной границами ромба:
        # нижняя граница ромба x = y * sqrt(3)
        # верхняя граница ромба x = (y-8) * sqrt(3)
        # правая граница ромба x = sqrt(64-16)
        # левая граница не задается, так как прямоугольник ограничен осью ординат
        if (y < x * 3 ** 0.5) and (y > (x - 8) * 3 ** 0.5) and (y < (64 - 16)**(1/2)):
            count += 1
print(count)