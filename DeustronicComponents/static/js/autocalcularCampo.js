// Funcionalidad de autocalcular un campo. Aplica un descuento a los pedidos al clickar un botón.

let aplicarDescuentoBtn = document.getElementById('aplicarDescuentoBtn');
let precioTotalElement = document.getElementById('precioSinDescuento');
let precioDescuentoElement = document.getElementById('precioConDescuento');

aplicarDescuentoBtn.addEventListener('click', () => {
    let precioTotal = parseFloat(precioTotalElement.textContent);
    let descuento = precioTotal * 0.2; //20% de descuento por rebajas de primavera
    let precioDescuento = precioTotal - descuento;

    precioDescuentoElement.textContent = `Precio Total con Descuento: ${precioDescuento} €`;
});
