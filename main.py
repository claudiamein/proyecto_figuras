
from lib import cuadrado, triangulo
from lib import cuadrado, rectangulo

print("Proyecto figuras")
lado = 4
print(f"El area de un cuadrado de lado {lado} es :{cuadrado.get_area(lado)} y el perímetro es {cuadrado.get_perimetro(lado)}")

base = 4
altura = 2

print(triangulo.get_identificador())
print(f"El area de un triangulo de base {base} y altura {altura} es :{triangulo.get_area(base, altura)} y el perímetro es {triangulo.get_perimetro(base, base, base)}")

print(rectangulo.get_identificador())
print(f"El área de un {rectangulo.get_identificador()} de base{base} y altura {altura} es: {rectangulo.get_area(base,altura)} y el perímetro {rectangulo.get_perimetro(base,altura)}")

