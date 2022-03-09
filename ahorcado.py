if __name__ == "__main__":
    import random
    import time


tipo_de_frutas = ["pera", "platano", "fresa", "manzana", "melon", "ciruela", "naranja", "papaya"]

marcas_de_moviles = ["xiaomi", "huawei", "iphone", "samsung", "nokia", "alcatel"]

print("Bienvenido al juego de ahorcado")
time.sleep(2)
print("El objetivo del juego es adivinar la palabra secreta letra por letra")
print("tienes 5 vidas, pierdes una vida cada que te equivocas si te quedas sin vidas pierdes")
time.sleep(2)

print("Desea jugar con palabras de que son tipo de frutas o marcas de moviles")
time.sleep(2)

cat_seleccionada = input("Ingrese f para tipo de frutas o m para marcas de moviles:")

while True:
    if cat_seleccionada.lower() == "f":
        print("excelente a seleccionado tipo de frutas")
        palabra_secreta = random.choice(tipo_de_frutas)
        break
    elif cat_seleccionada.lower() == "m":
        print("excelente a seleccionado marcas de moviles")
        palabra_secreta = random.choice(marcas_de_moviles)
        break

    else:
        print("Por favor seleccione una categoria valida")
        cat_seleccionada = input("Ingrese f para tipo de frutas y m para marcas de moviles: ")

vidas = 6

lista_letras_adivinadas = []

print('_' * len(palabra_secreta))

while True:

    while True:
        letra_adivinada = input("Adivina una letra: ")
        if (len(letra_adivinada) != 1 and letra_adivinada.isnumeric()):
            print("Eso no es una letra intenta con una sola letra")
        else:
            if letra_adivinada.lower() in lista_letras_adivinadas:
                print("Ya habias intentado con esa letra intenta con otra por favor")
            else:
                lista_letras_adivinadas.append(letra_adivinada)

                if letra_adivinada.lower() in palabra_secreta:
                    print("Felicidades adivinaste una letra")
                    break
                else:
                    vidas = vidas - 1
                    print("Te haz equivocado y perdido una vida")
                    print("Te quedan " + str(vidas) + " vidas")
                    break

    if vidas == 0:
        print("Haz perdido la palabra secreta era: " + palabra_secreta)
        break

    estatus_actual = ""

    letras_faltantes = 0
    for letra in palabra_secreta:

        if letra in lista_letras_adivinadas:
            estatus_actual = estatus_actual + letra

        else:
            estatus_actual = estatus_actual + "_"
            letras_faltantes = letras_faltantes + 1

    print(estatus_actual)

    if letras_faltantes == 0:
        print("Felicidades haz ganado")
        print("La palabra secreta es: " + palabra_secreta)
        break



