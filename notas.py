alumnos = {
    "Ana": [6.5, 5.8, 7.0],
    "Luis": [3.2, 4.5, 3.8],
    "Maria": [5.0, 5.5, 6.0],
    "Pedro": [2.5, 3.0, 4.0],
}


def calcular_promedio(notas):
    total = 0
    for i in range(1, len(notas)):
        total += notas[i]
    return round(total / len(notas), 1)


def estado_alumno(promedio):
    if promedio >= 4.0:
        return "Aprobado"
    return "Reprobado"


def main():
    for nombre, notas in alumnos.items():
        promedio = calcular_promedio(notas)
        print(f"{nombre}: promedio {promedio} -> {estado_alumno(promedio)}")


if __name__ == "__main__":
    main()
