# Diseño de un robot seguidor de línea con la capacidad de esterilizar superficies para reducir el riesgo de contagio ante el SARS-COV-2

## Descripción:
Este proyecto se realiza con el objetivo de llevar a cabo el desarrollo de un prototipo robótico seguidor de línea con la capacidad de esterilizar superficies, haciendo uso de un tubo fluorescente de luz ultravioleta que radia la luz de manera omnidireccional en el entorno que se encuentre. Consecuentemente, el robot será capaz de desplazarse siguiendo una trayectoria predefinida en el medio a implementarse, aportando una manera eficiente de desinfección portátil y rápida.
La simulación se llevó a cabo en el software [Webots](https://cyberbotics.com/) donde se utilizó el lenguaje Python para la programación del controlador del robot. A continuación se presenta el diagrama de flujo que obedecerá el prototipo:

![Diagrama de flujo](https://user-images.githubusercontent.com/66179885/131600354-3c8279e1-ab18-45be-858c-16a6417cf299.png)

## Pruebas:
Se realizaron algunos escenarios para la simulación del prototipo.

![Escenario1](https://user-images.githubusercontent.com/66179885/131600456-14f863e8-abfe-4cab-9466-3aafb21f7163.png)
![Escenario2](https://user-images.githubusercontent.com/66179885/131600479-9098f0fe-a038-47ef-adaa-dbbb0232e0c9.png)
![Escenario3](https://user-images.githubusercontent.com/66179885/131600498-d1e7bbab-f27b-4ab7-aa3a-a9a47fc3e614.png)

## Conclusiones:
- Si bien la simulación del robot nos permite visualizar el comportamiento del robot en un espacio, esto no se asemeja a la realidad en su totalidad, es por esto, que se debe realizar pruebas reales del prototipo final para verificar su funcionamiento y calibrar ciertos parámetros, como la distancia de operación de los sensores, para tener un mejor desempeño del robot.
- Resulta de gran importancia realizar un proceso metodológico durante la fase de diseño previo del prototipo a construir y evaluar qué tan factible es, así nos podemos ahorrar tiempo y recursos. Además, esto nos permite identificar posibles problemas y analizarlo sintetizando varias soluciones.
