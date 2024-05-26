    const botonesDetalles = document.querySelectorAll('button[id^="detalles-"]');

    for (const boton of botonesDetalles) {
        boton.addEventListener('click', () => {
            const idProducto = boton.id.replace('detalles-', '');
            const contenidoDetalles = document.getElementById(`detalles-contenido-${idProducto}`);
            contenidoDetalles.style.display = contenidoDetalles.style.display === 'none' ? 'block' : 'none';
        });
    }