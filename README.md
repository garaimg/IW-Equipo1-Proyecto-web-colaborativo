# IW-Equipo1-Proyecto-web-colaborativo

**RETO 2: GESTIÓN DE PEDIDOS**

○ Enlace al repositorio de Github:

    https://github.com/garaimg/IW-Equipo1-Proyecto-web-colaborativo

○ Funcionalidades:

    - Gestión de productos: creación, visualización (listado y detalle) y baja.
    - Gestión de pedidos: creación, visualización (listado y detalle) y actualización.
    - (EXTRA) Gestión de clientes: creación, visualización y actualización. 
    - (EXTRA) Gestión de componentes que componen cada producto: creación, visualización y actualización.
    - (EXTRA) Gestión de productos que componen cada pedido: creación, visualización y actualización.

○ Fuentes:

    - ALUD Ingeniería Web
    - W3 Schools (https://www.w3schools.com/django/index.php)
    - Documentación oficial de Django (https://docs.djangoproject.com/)
    - Conocimientos propios

○ Documentación adicional:

    Para el tratamiento de los productos que componen cada producto, hemos creado una segunda tabla que relaciona cada 
    pedido con uno de los productos disponibles, haciendo una entrada por cada producto que compone el pedido. Para 
    mostrar los pedidos que hay, hemos mostrado todas las líneas del modelo Pedidos, donde cada pedido aparece una sola 
    vez con toda la información referente al mismo. Para mostrar los detalles del mismo, hemos hecho uso de los modelos 
    Pedidos y PedidosProducto, con los que hemos mostrado los detalles de cada producto con el primer modelo y los
    componentes de cada producto con el segundo. Para hacer esto último, hemos mostrado todos los productos cuyo pedido 
    estuviésemos buscando.