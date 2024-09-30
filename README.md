# Proyecto 1

El código de este proyecto se divide en diferentes secciones que abarcan diferentes partes:

- Leds
- Botones
- Buzzer
- Consola
- Guardado de puntos

## Leds y Botones

Utilizamos 5 luces RGB y 5 botones. Al contar con limitados pines de la **rasberrypi**, el uso del RGB para el color verde, es el mismo para todos los leds. Es decir, que de un solo pin sale el color verde que alimenta todo los leds.

Los botones y leds están programados con la librería **RPi.GPIO** y la detección de los botones es a traves de una función ``detectButtons`` que devuelve una lista con **True** o **False** dependiendo si se presionó un u otro botón, en orden de como están dispuesto. Es decir si yo presionó el primer botón devuelve una lista:

``` python
[True, False, False, False, False]
```

## Buzzer

El buzzer esta programado para correr en segundo plano respecto al  hilo principal del programa. Para esto se usa la librería ``multiprocessing`` que nos permite crear procesos apartes en el sistema.

**Para el correcto funcionamiento del programa, es mejor esperar a estar en el menu principal y forzar el cerrado con ``Crt+C`` para no crear código que se quede ejecutando infinitamente.**

hay un total de 4 sonidos que se reproducen en distintos momentos. cada uno de ellos se encuentran almacenados y etiquetados en la carpeta de buzzer_melodys.

para la escritura de las melodías se ocupa una lista que contenga las notas etiquetadas de la siguiente forma:

``` python
  [
    'G4','B4','D5',
    '0','F4','F5','E5','DS5',
    'D5','F4','E4','DS4',
    'D4','C4','B2','C4',
  ]
```

Luego al pasar por la función ``play`` creada en el archivo ``buzzer.py`` se obtiene la frecuencia de la nota y se calcula el tiempo en ms que debe encender y apagar el pin para hacer vibrar el buzzer.

``` python
  period = 1.0 / frequency
  delayValue = period / 2
  numCycles = int(length * frequency)
```

## Consola y menú interactivo

El menu desplegado en la consola se construye a partir de 3 funciones que están contenidas en el archivo ``menu.py``:

- printMenu ( item, select, title )
- printGraph ( item, l )
- printTable ( title, item, encabezado, num )

Cada una de estas funciones imprimen en consola barras que contienen el contenido, ademas del contenido que varia según la función:

### printMenu

Imprime el menu principal y recibe como parámetros: **item**, **select**, **title**.

#### Item

Es una ``lista`` que describe cada item

``` python
['primer item', 'segundo item', 'tercer item']
```

esto lo imprime de la siguiente forma:

``` shell
====================Menu====================

primer item
segundo item
tercer item

============================================
```

#### Select

Este es un parámetro de tipo ``number``, que indica cual de los items esta seleccionado.

si el select es igual a 2, entonces se vería de la siguiente forma:

``` shell
====================Menu====================

  primer item
> segundo item
  tercer item

============================================
```

#### Title

Este parámetro de tipo ``String`` recibe el nombre del titulo de la sección y la imprime encima de los items.

lo imprime de la siguiente forma

``` shell
====================Menu====================

  Titulo de la sección

> primer item
  segundo item
  tercer item

============================================
```

### printGraph

Esta función imprime el texto intacto que se le entregue como parámetro, calculando la distancia de como debe imprimirlo y agregándole los limites del menu. Recibe como parámetros: **item**, **l**.

#### item

Es un string que contiene lo que se quiere imprimir

#### l

l es la cantidad de espacio de margen.

#### ejemplo

``` python
PrintGraph('\t_____\n\t|___ /\n\t  |_ \ \n\t ___) |\n\t|____/\n', 6)
```

``` shell
====================Menu====================

    _____
    |___ /
      |_ \ 
     ___| |
    |____/


============================================
```

### printTable

Imprime en consola una tabla con datos variables. Recibe como parámetros **title**, **item**, **encabezado**, **num**.

#### Title o legenda

Muestra un titulo o legenda de la tabla en cuestión.

#### Items

Es una ``lista`` que describe cada item como clave y valor.

``` python
[['Juan', 19],['Humberto', 21],['Cristian', 28]]
```

#### Encabezado

El encabezado es una ``lista`` que muestra el encabezado de la tabla.

``` python
['nombre', 'Edad']
```

#### num

Este parámetro de tipo ``boolean`` se utiliza para indicar si se quiere que los items estén enumerados del 1 a la n-esimo item.

``` shell
====================Menu====================

  Edades de usuarios

    nombre    Edad

  1 Juan        19
  2 Humberto    21
  3 Cristian    28

============================================
```

## Guardado de puntos

Para el guardado de puntos se utiliza un archivo llamado ``puntos.txt`` que permite almacenar la información de los puntos. Para esto existen dos funciones en python que permiten escribir y obtener los puntos desde el archivo. Estas funciones que están contenidas en el archivo ``puntos.py`` son **getPuntos** y **addScore**.

Las funciones **getPuntos** y **addScore** ocupan la función ``open()`` de python que permite abrir y editar archivos. De esta forma obtiene el texto plano el cual a traves de la funciones de texto como ``split`` empieza a convertir los datos en listas.

## The Game

Para todo lo que es el juego, existe la función ``Game()`` que esta en el archivo ``main.py``. En esta función se dispone una cantidad de rondas y tiempo. Luego con una función ``genAleatorio`` que se encuentra en el archivo ``utils.py``  que devuelve una lista con **True** o **False** de forma aleatoria.

```python
[False, True, True, False, True]
```

Cada True hace que se encienda la luz de color azul y cada false encienda la luz de color rojo. De esta forma generamos cada ronda donde con la función ``detectButtons`` detecta los botones que se presionaron y toma una dicción a partir de si era de color azul o rojo, agregando un punto o retándolo según corresponda.
