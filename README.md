# Maekawa_Voting_System

## Descripción General
Este programa implementa un sistema de comunicación distribuido con varios nodos. Los nodos se conectan entre sí, envían y reciben mensajes en un intento de coordinarse en la red. Esto simula la funcionalidad del algoritmo de exclusión mutua de Maekawa, donde cada nodo coordina con sus colegas para enviar mensajes de saludo, lo que representa un paso básico en un sistema distribuido más grande, como una simulación de sincronización para acceso a recursos compartidos.

## Cómo Funciona
1. Inicio del Servidor en Cada Nodo: Cada nodo (Node 0, Node 1, Node 2, Node 3) inicia un servidor en un puerto específico (20000, 20001, 20002 y 20003, respectivamente). Este servidor permite que los nodos reciban conexiones y mensajes de otros nodos en la red.

2. Conexiones entre Nodos: Una vez que los servidores están en funcionamiento, los nodos comienzan a establecer conexiones entre sí. Cada nodo acepta conexiones de los demás y registra cada conexión entrante. Esto crea un sistema en el que los nodos pueden comunicarse de manera bidireccional.

3. Inicio del Algoritmo Maekawa Mutex: Después de establecer las conexiones, el programa inicia la ejecución del algoritmo de exclusión mutua de Maekawa. Aquí, cada nodo se ejecuta en modo de "colaboración" con un conjunto específico de nodos que son sus "colegas".

4. Envío de Mensajes a Colegas: Cada nodo envía un mensaje a sus colegas.  En cada mensaje, se incluyen algunos detalles como el tipo de mensaje ("greetings"), el origen y el destino del mensaje ("src" y "dest"), un timestamp ("ts") y un mensaje de saludo en el campo data. Por ejemplo:

    `Node 0 envía un mensaje de "greetings" a sí mismo (Node 0) y a Node 2.`

    `Node 1 envía un mensaje a sí mismo (Node 1) y a Node 3.`

    `Node 2 envía un mensaje a Node 0 y a sí mismo (Node 2).`

    `Node 3 envía un mensaje a Node 1 y a sí mismo (Node 3).`

5. Recepción y Procesamiento de Mensajes: Los nodos que reciben mensajes los registran en la consola, mostrando el contenido recibido. Por ejemplo, cuando Node 0 recibe el mensaje de Node 2, imprime el mensaje, incluyendo el contenido exacto y los datos relevantes.

6. Detención de los Nodos: Después de ejecutar la lógica de mensajes, cada nodo comienza su proceso de "parada". El sistema muestra mensajes como Stopping Node 0, indicando que se está desconectando o finalizando la ejecución del nodo.

7. Tiempo de Espera y Timeout: Tras iniciar el proceso de cierre, el sistema entra en un estado de espera, durante el cual los nodos siguen comprobando la llegada de nuevos mensajes. Como no hay más mensajes, cada nodo finalmente alcanza un timeout (tiempo de espera) en la función select. Esto es indicado por mensajes como NS0 - Timed out, donde NS representa el Node Server de cada nodo (Node Server 0, Node Server 1, etc.).

8. Finalización de la Ejecución: La ejecución termina después de 20 segundos, y el programa imprime Execution finished after 20 seconds, indicando que la ejecución total del sistema ha finalizado.

## Cómo Ejecutar
1. Se arranca una terminal y se accede al directorio que contiene el programa.
2. Lanzamos el programa con: python3 main.py
3. La ejecución empieza sola, con diferentes mensajes en diferentes colores para diferenciar conexiones, mensajes ...
