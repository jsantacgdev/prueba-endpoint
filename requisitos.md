# Prueba técnica Merlin Software

Desarrollo de un Endpoint para Ordenación
Automática de Productos

## Contexto:

En nuestra pequeña empresa de venta de productos en línea,
ofrecemos una amplia variedad de artículos agrupados en distintas
categorías, como libros, videoconsolas, portátiles, relojes,
camisetas, entre otros.

Recientemente, cerramos acuerdos con cinco proveedores de
productos comestibles, lo que aumentará considerablemente el número
de categorías que gestionamos.

Hasta ahora, el departamento de marketing ordenaba los productos
manualmente en cada categoría, basándose en criterios intuitivos
para maximizar las ventas. Con la expansión, marketing ha solicitado
al departamento de sistemas que automatice la ordenación de productos.

Como ingeniero de software, aceptas el reto y te comprometes a
tener una demostración del algoritmo antes de terminar el día.

## Requisitos:

Objetivo:

- Crear un endpoint que reciba datos de productos y devuelva una
  lista ordenada de productos según ciertos criterios.

Entrada del Endpoint:

- Dos listas en formato JSON:
  - ProductSales: productos con ventas en euros (€) en las
    últimas 72 horas.
  - ProductStock: productos con su stock actual
    (número de unidades).

Salida del Endpoint:

- Lista ordenada de identificadores de productos, de mayor a menor
  prioridad.

Criterios de Ordenación:

- Basar la ordenación en ventas recientes y stock disponible.
- Las ponderaciones de ventas y stock deben ser configurables
  (ej. 25% para ventas y 75% para stock).

Configurabilidad:

- El endpoint debe permitir configurar ponderaciones para
  ventas y stock.

Consideraciones Adicionales:

- No se requiere autenticación o seguridad.
- Documentación básica sobre el uso del endpoint.

## Ejemplo de Uso:

Prueba del endpoint mediante `cURL`:

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

## Tarea:

1. Implementar `/sort-products` según la especificación.
2. Crear un algoritmo que combine las ventas y el stock de cada
   producto utilizando ponderaciones configurables.
3. Incluir un archivo README con instrucciones para ejecutar y
   probar el código.

## Entregables:

- Código fuente del endpoint.
- Archivo README con instrucciones y dependencias.
- Casos de prueba que demuestren el funcionamiento del endpoint.

## Notas:

No buscamos un picateclas, sino a un ingeniero de software capaz de:

- Elegir y justificar las herramientas y tecnologías.
- Escribir código claro, escalable y mantenible.
- Implementar pruebas unitarias o de integración significativas.
- Documentar de forma precisa y concisa, solo cuando aporte valor.
