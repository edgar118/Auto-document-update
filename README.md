
# Auto-document-update

Requisitos:
Para ejecutar este proyecto correctamente, necesitas tener instalados los siguientes requisitos:

**pandas**: Para manipulación de datos y procesamiento de archivos CSV/JSON.

**watchdog**: Para monitorear los cambios en el sistema de archivos.

**re**: Para trabajar con expresiones regulares (usado en el primer código).

**math**: Para realizar operaciones matemáticas, como productos de números.

Instalación

1. **Clona el Repositorio**

   Clona el repositorio en tu máquina local:

   ```bash
   git clone https://github.com/edgar118/Auto-document-update.git
   cd business_check-in

2. **Instalación librerias**
   ```bash
   pip install pandas watchdog
   
**Descripcion**

**Ejercicio 1**

**ListAverage(numbers: list)**: Calcula el promedio de una lista de números enteros, alternando entre incluir o excluir números cuando aparece un 10. Retorna el promedio truncado o 0 si no se incluyen números.

**multipliesNumbers(text: str)**: Extrae todos los números de un texto dado, los convierte a enteros y retorna el producto de estos. Si no se encuentran números, retorna "Numbers not Found".

**christmas_tree(n: int)**: Genera y muestra un patrón de árbol de Navidad con estrellas (*), basado en la altura impar n dada. Si n es par, imprime un mensaje de error.

**Ejercicio2**

Este script monitorea una carpeta para detectar archivos nuevos, eliminados o modificados, y procesa archivos .csv o .json para actualizarlos en un DataFrame. Utiliza la librería watchdog para observar cambios en el sistema de archivos y actualiza el DataFrame de manera continua, almacenándolo en un archivo pickle.


