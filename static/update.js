function addComponent() { 
    let part = document.getElementById('part').value;
    let price = document.getElementById('price').value;

    fetch('/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 'hardware_part': part, 'price': parseFloat(price) })
    })
    .then(response => response.text())
    .then(data => {
        alert(data);
        location.reload();
    });
}

function clearAll() {
    fetch('/clear', {
        method: 'POST'
    })
    .then(response => response.text())
    .then(data => {
        alert(data);
        location.reload();
    });
}
