from lib import cuadrado, triangulo, rectangulo

print("Proyecto Figuras")
print(triangulo.get_identificador())
lado=4
print(f"El área de un {cuadrado.get_identificador()} de lado {lado} es: {cuadrado.get_area(lado)} y el perímetro es {cuadrado.get_perimetro(lado)}")

base=4
altura=2
print(f"El área de un {triangulo.get_identificador()} de base {base} y altura {altura} es: {triangulo.get_area(base,altura)} y el perímetro es {triangulo.get_perimetro(base,base,base)}")

print(f"Área del rectángulo (4x5): {rectangulo.get_area(4, 5)}")