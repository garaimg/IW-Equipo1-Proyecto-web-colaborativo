document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.btn-completar').forEach(function (button) {
        button.addEventListener('click', function () {
            let pedidoId = this.getAttribute('data-id');
            let url = this.getAttribute('data-url');

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    'pedido_id': pedidoId,
                    'estado': 'completado'
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    let listItem = document.getElementById(`pedido-${pedidoId}`);
                    let tick = document.createElement('span');
                    tick.textContent = '\u2714';
                    tick.classList.add('estado-completado');
                    listItem.removeChild(button);
                    listItem.appendChild(tick);
                } else {
                    console.error('Error:', data.error);
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
});