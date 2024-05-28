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

○ Fuentes:

    - ALUD Ingeniería Web
    - W3 Schools (https://www.w3schools.com/django/index.php)
    - Documentación oficial de Django (https://docs.djangoproject.com/)
    - Repositorio github de jon vadillo (https://github.com/jvadillo/curso-django-paso-a-paso)
    - ED Team (https://ed.team/blog/como-aumentar-y-disminuir-el-tamano-de-fuente-con-variables-css-y-javascript)
    - Conocimientos propios

○ Documentación adicional:

    Para el tratamiento de los productos incluidos en cada pedido, hemos creado una segunda tabla que relaciona cada pedido con los productos disponibles. 
    Por lo tanto, es necesario ingresar los productos uno por uno, pudiendo especificar la cantidad de cada uno de ellos. 
    Para mostrar los pedidos existentes, hemos desplegado todas las líneas del modelo de Pedidos, donde cada pedido aparece una sola vez con toda la información relacionada. 
    Para visualizar los detalles de cada pedido, hemos utilizado los modelos Pedidos y PedidosProducto,
    permitiéndonos mostrar los detalles de cada pedido con el primer modelo y los productos asociados a cada pedido con el segundo. 
    Para lograr esto último, hemos exhibido todos los productos correspondientes al pedido que estábamos buscando.