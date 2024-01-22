function allProducts() {
    fetch(`/admin/products_manager/all`).then(response => response.json()).then(data     => {
        document.getElementById('products').innerHTML = printProducts(data.products);
})
}

function selectCategory() {
    var selected_category = document.getElementById("category").value;

    fetch(`/admin/products_manager/category/${selected_category}`).then(response => response.json()).then(data => {document.getElementById('products').innerHTML = printProducts(data);
})
}

function selectBrand() {
    var selected_brand = document.getElementById("brand").value;

    fetch(`/admin/products_manager/brand/${selected_brand}`).then(response => response.json()).then(data => {document.getElementById('products').innerHTML = printProducts(data);
})
}

function selectPrice() {
    var priceOperator = document.getElementById("priceOperator").value;
    var priceInput = document.getElementById("priceInput").value;

    fetch(`/admin/products_manager/price/${priceOperator}/${priceInput}`).then(response => response.json()).then(data => {document.getElementById('products').innerHTML = printProducts(data);
})
}

function printProducts(products) {
    var html = `<div class="allProducts">`

    products.forEach(product => {
        html += 
                `<div class="product">
                <div style="display: flex; flex-direction: column;  margin: 3px;">
                <div><strong>ID:</strong> ${product.product_id}<br></div>
                <div><strong>Category:</strong> ${product.category}<br></div>
                <div><strong>Brand:</strong> ${product.brand}<br></div>
                <div><strong>Price:</strong> ${product.price} USD$<br></div>
                <div><strong>Left In Stock:</strong> ${product.stock}<br></div>
                <div><strong>Times Ordered:</strong> ${product.ordered}<br></div>
                </div>
                <div class="nameImage">
                <div style="margin: auto;"><strong>${product.name}</strong><br></div>
                <div class="imageIncard"><img class="productImage" src="/static/images/${product.image}" alt="Image"><br></div>
                </div>
                </div>`;
    });
    
    html += `</div>`;

    return html;
}

allProducts()