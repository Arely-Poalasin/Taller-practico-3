# Gestión de Mascotas en Python

## Información del estudiante

* **Nombre:** Arely Betzabe Poalasin Shiguango
* **Asignatura:** Programación Orientada a Objetos
* **Semana:** 3
* **Actividad:** Comparación entre Programación Tradicional y Programación Orientada a Objetos

## Descripción del proyecto

El presente proyecto tiene como finalidad desarrollar un pequeño sistema de gestión de mascotas utilizando dos enfoques diferentes de programación: Programación Tradicional y Programación Orientada a Objetos (POO). Ambos programas resuelven el mismo problema, permitiendo registrar y mostrar la información básica de una mascota.

A través de esta actividad se busca identificar las diferencias entre ambos paradigmas de programación, analizando cómo cambia la organización del código, la gestión de los datos y la implementación de las funcionalidades.

## Objetivos

* Aplicar los conceptos básicos de la Programación Tradicional mediante el uso de variables y funciones.
* Implementar los principios fundamentales de la Programación Orientada a Objetos utilizando clases, objetos, atributos y métodos.
* Comparar ambos enfoques para comprender sus características y ventajas.
* Organizar adecuadamente un proyecto en Python utilizando una estructura de carpetas y archivos.

## Datos manejados por cada mascota

Cada mascota registra la siguiente información:

* Nombre.
* Especie.
* Edad.

## Estructura del proyecto

gestion_mascotas/

├── programacion_tradicional/

│   └── tradicional.py

├── programacion_poo/

│   ├── main.py

│   └── mascota.py

└── README.md

## Descripción de los programas

### Programa 1: Programación Tradicional

Este programa fue desarrollado utilizando funciones y variables, sin emplear clases ni objetos. Los datos de la mascota se solicitan mediante el teclado y posteriormente se muestran de forma organizada.

**Características implementadas:**

* Uso de funciones para registrar y mostrar la información.
* Entrada de datos por teclado.
* Uso de variables para almacenar la información.
* Presentación ordenada de los resultados.

### Programa 2: Programación Orientada a Objetos

Este programa utiliza una clase denominada `Mascota`, la cual representa una abstracción de una mascota real. Se crean objetos a partir de esta clase y se utilizan métodos para mostrar información y representar comportamientos.

**Características implementadas:**

* Definición de la clase `Mascota`.
* Implementación de atributos: nombre, especie y edad.
* Implementación de métodos: `mostrar_informacion()` y `hacer_sonido()`.
* Creación de objetos para representar diferentes mascotas.
* Aplicación del principio de abstracción.

## Conceptos de Programación Orientada a Objetos aplicados

* **Clase:** plantilla para la creación de objetos.
* **Objeto:** instancia de una clase.
* **Atributos:** características propias de cada objeto.
* **Métodos:** acciones o comportamientos definidos dentro de la clase.
* **Abstracción:** representación de las características esenciales de una mascota.

## Instrucciones de ejecución

### Programa tradicional

1. Abrir una terminal.
2. Acceder a la carpeta `programacion_tradicional`.
3. Ejecutar el siguiente comando:

```bash
python tradicional.py
```

### Programa orientado a objetos

1. Abrir una terminal.
2. Acceder a la carpeta `programacion_poo`.
3. Ejecutar el siguiente comando:

```bash
python main.py
```

## Conclusiones

La Programación Tradicional resulta adecuada para resolver problemas sencillos mediante funciones y variables. Sin embargo, la Programación Orientada a Objetos proporciona una mejor organización del código, facilita la reutilización y el mantenimiento del software, y permite modelar situaciones del mundo real a través de clases y objetos.

El desarrollo de esta actividad permitió comprender las diferencias entre ambos enfoques y reconocer la importancia de seleccionar el paradigma más apropiado según las necesidades del problema a resolver.
