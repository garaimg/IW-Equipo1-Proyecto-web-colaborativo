/*
(1p) Capturar un evento en el DOM y producir un cambio en el estilo/contenido de
la página (mostrar/ocultar un bloque al hacer click en “expandir información”).
*/

const botonExpandir = document.getElementsByClassName('botonExpandir')[0];
const contExp = document.getElementsByClassName('contenedorExpandible')[0];

function mostrarOcultarBloque(estado) {
    if (estado === 'mostrar') {
        contExp.style.display = 'block';
    } else if (estado === 'ocultar') {
        contExp.style.display = 'none';
    }
}

botonExpandir.addEventListener('click', () => {
    const estadoActual = contExp.style.display === 'none' ? 'mostrar' : 'ocultar';
    mostrarOcultarBloque(estadoActual);
});
