def cifrado_cesar(texto, desplazamiento):
    resultado = ""

    for char in texto:
        if char.isalpha():
            # Determinar si es mayúscula o minúscula
            start = ord("A") if char.isupper() else ord("a")

            # Aplicar desplazamiento dentro del alfabeto
            nueva_letra = chr((ord(char) - start + desplazamiento) % 26 + start)
            resultado += nueva_letra
        else:
            # No modificar caracteres no alfabéticos
            resultado += char

    return resultado