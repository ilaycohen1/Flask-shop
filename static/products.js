function allProducts() {
    fetch(`/products/all`).then(response => response.json()).then(data     => {
        document.getElementById('products').innerHTML = printProducts(data.products);
})
}

function selectCategory() {
    var selected_category = document.getElementById("category").value;

    fetch(`/products/category/${selected_category}`).then(response => response.json()).then(data => {document.getElementById('products').innerHTML = printProducts(data);
})
}

function selectBrand() {
    var selected_brand = document.getElementById("brand").value;

    fetch(`/products/brand/${selected_brand}`).then(response => response.json()).then(data => {document.getElementById('products').innerHTML = printProducts(data);
})
}

function selectPrice() {
    var priceOperator = document.getElementById("priceOperator").value;
    var priceInput = document.getElementById("priceInput").value;

    fetch(`/products/price/${priceOperator}/${priceInput}`).then(response => response.json()).then(data => {document.getElementById('products').innerHTML = printProducts(data);
})
}

function addToCart(productID) {
    fetch(`/cart/add/${productID}`).then(response => response.json()).then(data => {
        alert(data.messageAdd);
    })
}


function printProducts(products) {
    var html = `<div class="allProducts">`

    products.forEach(product => {
        html += 
                `<div style="display: flex; flex-direction: column; gap:5px;">
                    <div class="product">
                        <div style="display: flex; flex-direction: column;  margin: 3px;">
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
                </div>
                    <button style="margin: auto; text-align: center; width: 40px; height: 40px;" onclick="addToCart('${product.product_id}')"><img class="cartImage" src="/static/images/shopping-cart.png"></button>
                </div>`;
    });
    
    html += `</div>`;

    return html;
}

allProducts()