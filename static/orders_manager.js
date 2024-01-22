function allOrders() {
    fetch(`/admin/orders_manager/all`).then(response => response.json()).then(data => {
        console.log(data);
        document.getElementById('orders').innerHTML = printOrders(data);
})
}

function selectProduct() {
    var selected_product = document.getElementById("byProduct").value;

    fetch(`/admin/orders_manager/product/${selected_product}`).then(response => response.json()).then(data => {document.getElementById('orders').innerHTML = printOrders(data);
})
}

// function selectBrand() {
//     var selected_brand = document.getElementById("brand").value;

//     fetch(`/admin/products_manager/brand/${selected_brand}`).then(response => response.json()).then(data => {document.getElementById('products').innerHTML = printProducts(data.orders);
// })
// }

// function selectPrice() {
//     var priceOperator = document.getElementById("priceOperator").value;
//     var priceInput = document.getElementById("priceInput").value;

//     fetch(`/admin/products_manager/price/${priceOperator}/${priceInput}`).then(response => response.json()).then(data => {document.getElementById('products').innerHTML = printProducts(data);
// })
// }

function printOrders(orders) {
    var html = `<table class="table">
                    <tr class="tableHead">
                        <th>Order ID</th>
                        <th>Order Date</th>
                        <th>Ordered By</th>
                        <th>Product</th>
                        <th>Status</th>
                        <th>Address</th>
                        <th></th>
                    </tr>`;

    console.log(orders);

    orders.forEach(order => {

        html += `<tr class="tableBody">
                <td>${order.order_id}</td>
                <td>${order.order_date}</td>
                <td>${order.user}</td>
                <td>${order.product}</td>
                <td>${order.status}</td>
                <td>${order.address}</td>
                <td>Update Status</td>
                </tr>`   
    });
    
    html += `</table>`;

    return html;
}

allOrders()