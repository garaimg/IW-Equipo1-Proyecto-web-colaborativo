// Funcionalidad de autocalcular un campo desde un formulario. Aplica un descuento a los pedidos al clickar un botón.

const descuentoForm = document.getElementById('descuentoForm');
const codigoDescuentoInput = document.getElementById('codigoDescuento');
const precioTotalElement = document.getElementById('precioSinDescuento');
const precioDescuentoElement = document.getElementById('precioConDescuento');

descuentoForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const codigoDescuento = codigoDescuentoInput.value.toUpperCase();

    if (codigoDescuento === 'PRIMAVERA24') {
        let precioTotal = parseFloat(precioTotalElement.textContent);
        let descuento = precioTotal * 0.2;
        let precioDescuento = precioTotal - descuento;

        precioDescuentoElement.textContent = `Precio Total con Descuento: ${precioDescuento.toFixed(2)} €`;
    } else {
        alert('Código de descuento incorrecto.');
    }
});
