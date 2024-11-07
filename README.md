# Desarrollo de un Endpoint para Ordenación

## Instrucciones

Se ha utilizado Python 3 como lenguaje de programación para desarrollar el ejercicio, utilizando Flask como librería para el desarrollo del endpoint.

Se añade un archivo `requirements.txt` con las dependencias necesarias para ejecutar el proyecto.

## Ejemplo de uso

Para ejecutar el proyecto, siga los siguientes pasos:

1. Abre una terminal y navega hasta el directorio del proyecto.
2. Ejecuta el siguiente comando para instalar las dependencias:
   ```
   pip install -r requirements.txt
   ```
   Esto instalará las dependencias necesarias para ejecutar el proyecto.
3. Ejecuta el siguiente comando para iniciar el servidor web:

   ```
   python main.py
   ```

   Esto iniciará el servidor web y se mostrará un mensaje indicando que el servidor está en ejecución.

4. Abre una nueva terminal y ejecuta el siguiente comando para probar el servidor web:

```
curl -X POST 'http://localhost:8080/sort-products' -H 'Content-Type: application/json' -d '{
  "salesWeight": 0.5,
  "stockWeight": 0.5,
  "productSales": [
    {"productId": "1", "sales": 50000},
    {"productId": "2", "sales": 100000},
    {"productId": "3", "sales": 100000},
    {"productId": "4", "sales": 75000}
  ],
  "productStock": [
    {"productId": "1", "stock": 100000},
    {"productId": "2", "stock": 400000},
    {"productId": "3", "stock": 200000},
    {"productId": "4", "stock": 300000}
  ]
}'

```
