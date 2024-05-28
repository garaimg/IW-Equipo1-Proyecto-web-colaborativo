# IW-Equipo1-Proyecto-web-colaborativo

**RETO 2: GESTIÓN DE PEDIDOS**

○ Enlace al repositorio de Github:

    https://github.com/garaimg/IW-Equipo1-Proyecto-web-colaborativo

○ Funcionalidades principales:

    - Gestión de productos: creación, visualización (listado y detalle), actualización y baja.
    - Gestión de pedidos: creación, visualización (listado y detalle), actualización y baja.
    - (EXTRA) Gestión de clientes: creación, visualización (listado y detalle), actualización y baja.
    - (EXTRA) Gestión de componentes que componen cada producto: creación, visualización (listado y detalle), actualización y baja.
    - (EXTRA) Gestión de productos que componen cada pedido: creación, visualización (listado y detalle), actualización y baja.

○ Funcionalidades añadidas en E3:

    - Python: 
        - Envío de emails
        - Autenticación de usuarios
    - JavaScript: 
        - Crear un evento al hacer click en un botón o enlace que produzca el cambio (aumentar/disminuir) el tamaño de los elementos de texto (<h1>, <h2>, <p>, ...). 
        - Autocalcular un campo desde un formulario (cambiar un valor numético "precio" para añadir un descuento en función de un código de descuento insertado en un formulario).
        - Capturar un evento en el DOM y producir un cambio en el estilo/contenido de la página (mostrar/ocultar un bloque al hacer click en “expandir información”).
    - Fetch JS: 
        - Envío de datos de un formulario mediante AJAX para su almacenamiento en BBDD y posterior visualización del resultado (cambiar el estado de un registro de “en proceso” a “completado” en pedidos y mostrarlo en pantalla sin necesidad de recarga de la página).

○ Fuentes:

    - ALUD Ingeniería Web
    - W3 Schools (https://www.w3schools.com/django/index.php)
    - Documentación oficial de Django (https://docs.djangoproject.com/)
    - Repositorio github de jon vadillo (https://github.com/jvadillo/curso-django-paso-a-paso)
    - ED Team (https://ed.team/blog/como-aumentar-y-disminuir-el-tamano-de-fuente-con-variables-css-y-javascript)
    - Conocimientos propios

○ Documentación adicional sobre funcionalidades principales:

    Para el tratamiento de los productos incluidos en cada pedido, hemos creado una segunda tabla que relaciona cada pedido con los productos disponibles. 
    Por lo tanto, es necesario ingresar los productos uno por uno, pudiendo especificar la cantidad de cada uno de ellos. 
    Para mostrar los pedidos existentes, hemos desplegado todas las líneas del modelo de Pedidos, donde cada pedido aparece una sola vez con toda la información relacionada. 
    Para visualizar los detalles de cada pedido, hemos utilizado los modelos Pedidos y PedidosProducto,
    permitiéndonos mostrar los detalles de cada pedido con el primer modelo y los productos asociados a cada pedido con el segundo. 
    Para lograr esto último, hemos exhibido todos los productos correspondientes al pedido que estábamos buscando.
    
    Nota: la documentación completa se encuentra adjunta a la entrega, en el apartado E4. 
    