// Crear un evento al hacer click en un botón o enlace que produzca el
// cambio (aumentar/disminuir) del tamaño de los elementos de texto (<h1>,
// <h2>, <p>, ...).

//Fuente: https://ed.team/blog/como-aumentar-y-disminuir-el-tamano-de-fuente-con-variables-css-y-javascript

const aumentarButton = document.getElementById('aumentar');
const disminuirButton = document.getElementById('disminuir');

aumentarButton.addEventListener('click', aumentarTamano);
disminuirButton.addEventListener('click', disminuirTamano);

function aumentarTamano() {
    const htmlFontSize = parseFloat(getComputedStyle(document.documentElement).fontSize);
    const newFontSize = htmlFontSize * 1.1; // Aumenta un 10%
    document.documentElement.style.fontSize = `${newFontSize}px`;
}

function disminuirTamano() {
    const htmlFontSize = parseFloat(getComputedStyle(document.documentElement).fontSize);
    const newFontSize = htmlFontSize * 0.9; // Dismunuye un 10%
    document.documentElement.style.fontSize = `${newFontSize}px`;
}

//________________________________________________________________________________________

