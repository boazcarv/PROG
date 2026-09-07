"""Exercícios sobre Circle, Point e Rectangle."""

# Questão 1 — Escreva uma definição para uma classe denominada Circle, com os
# atributos center e radius, onde center é um objeto Point e radius é um número.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


# Questão 2 — Instancie um objeto Circle, que represente um círculo com o
# centro em (150, 100) e raio 75.
circle = Circle(Point(150, 100), 75)


# Questão 3 — Escreva uma função denominada point_in_circle, que tome um Circle
# e um Point e retorne True se o ponto estiver dentro ou no limite do círculo.
def point_in_circle(circle, point):
    distancia = hypot(point.x - circle.center.x, point.y - circle.center.y)
    return distancia <= circle.radius


# Questão 4 — Escreva uma função chamada rect_in_circle, que tome um Circle e
# um Rectangle e retorne True se o retângulo estiver totalmente dentro ou no
# limite do círculo.
def rect_in_circle(circle, rectangle):
    return all(point_in_circle(circle, corner) for corner in rectangle.corners)


# Questão 5 — Escreva uma função denominada rect_circle_overlap, que tome um
# Circle e um Rectangle e retorne True se algum dos cantos do retângulo cair
# dentro do círculo. Nesta versão, também são considerados os casos em que
# alguma parte do retângulo atravessa ou contém o centro do círculo.
def rect_circle_overlap(circle, rectangle):
    if any(point_in_circle(circle, corner) for corner in rectangle.corners):
        return True

    nearest_x = max(rectangle.x, min(circle.center.x, rectangle.x + rectangle.width))
    nearest_y = max(rectangle.y, min(circle.center.y, rectangle.y + rectangle.height))
    nearest_point = Point(nearest_x, nearest_y)
    return point_in_circle(circle, nearest_point)