# Documentación: Encuentra el Subarreglo de Longitud Máxima con Suma Igual al Objetivo

## Descripción
Esta función en Python encuentra el subarreglo de longitud máxima dentro de un arreglo de números enteros cuya suma sea igual a un número objetivo dado. Si no se encuentra ningún subarreglo que cumpla con la condición, la función devuelve una lista vacía.

---

## Sintaxis
```python
get_target_num(listNumber, target)
```

### Argumentos
- `listNumber` (list): Lista de números enteros.
- `target` (int): Número objetivo para la suma.

### Retorno
- `list`: El subarreglo de longitud máxima cuya suma sea igual al objetivo, o una lista vacía `[]` si no se encuentra ningún subarreglo.

---

## Implementación
```python
def get_target_num(listNumber, target):
    max_length = 0
    subarray = []
    
    for start in range(len(listNumber)):
        current_sum = 0
        for end in range(start, len(listNumber)):
            current_sum += listNumber[end]
            
            if current_sum == target:
                current_length = end - start + 1
                
                if current_length > max_length:
                    max_length = current_length
                    subarray = listNumber[start:end + 1]
                    
    return subarray if max_length > 0 else []
```

---

## Ejemplo de Uso

```python
# Ejemplo 1: Subarreglo encontrado
listNumber = [2, 4, 6, 8, 10]
target = 12

result = get_target_num(listNumber, target)
print(f"El subarreglo es: {result}, para el objetivo: {target}")
```
**Salida:**
```
El subarreglo es: [2, 4, 6], para el objetivo: 12
```

```python
# Ejemplo 2: Sin subarreglo válido
listNumber = [-3, -7, -2, -5, -8]
target = -10

result = get_target_num(arr, target)
print(f"El subarreglo es: {result}, para el objetivo: {target}")
```
**Salida:**
```
El subarreglo es: [-3, -7], para el objetivo: -10
```

---

## Notas Adicionales
- Si hay múltiples subarreglos con la misma longitud máxima que cumplen con la condición, la función devuelve el primer subarreglo encontrado.
- Asegúrate de probar el algoritmo con diferentes combinaciones de entradas para verificar su robustez.

