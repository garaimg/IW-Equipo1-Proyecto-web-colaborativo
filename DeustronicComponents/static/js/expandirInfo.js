/*
(1p) Capturar un evento en el DOM y producir un cambio en el estilo/contenido de
la página (mostrar/ocultar un bloque al hacer click en “expandir información”).
*/

const botonExpandir = document.getElementById('boton-expandir');
const contenedorExpansible = document.getElementsByClassName('contenedor-expansible')[0];

function mostrarOcultarBloque(estado) {
    if (estado === 'mostrar') {
        contenedorExpansible.style.display = 'block';
    } else if (estado === 'ocultar') {
        contenedorExpansible.style.display = 'none';
    }
}
//Lo cambia en el html el style, pero da igual. Hacer que empiece en none como dice el CSS.

botonExpandir.addEventListener('click', () => {
    const estadoActual = contenedorExpansible.style.display === 'none' ? 'mostrar' : 'ocultar';
    mostrarOcultarBloque(estadoActual);
});
