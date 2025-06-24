// ✅ Add to Cart
function addToCart(id, name, price) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    const index = cart.findIndex(item => item.id === id);
    if (index !== -1) {
        cart[index].quantity += 1;
    } else {
        cart.push({ id, name, price, quantity: 1 });
    }

    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
    alert(`${name} added to cart! 🛒`);
}

// ✅ Update Cart Count in Header
function updateCartCount() {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    const count = cart.reduce((sum, item) => sum + item.quantity, 0);
    const cartCountEl = document.getElementById("cartCount");
    if (cartCountEl) {
        cartCountEl.textContent = count;
    }
}

// ✅ Remove Item from Cart
function removeItem(index) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.splice(index, 1);
    localStorage.setItem('cart', JSON.stringify(cart));
    loadCart();
    updateCartCount();
}

// ✅ Load Cart Items (Cart Page Only)
function loadCart() {
    const cartList = document.getElementById('cartList');
    const totalPriceEl = document.getElementById('totalPrice');
    const placeOrderBtn = document.getElementById('placeOrderBtn');

    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    if (!cartList || !totalPriceEl) return;

    cartList.innerHTML = '';
    let total = 0;

    cart.forEach((item, index) => {
        total += item.price * item.quantity;
        const li = document.createElement('li');
        li.innerHTML = `
            <h3>${item.name}</h3>
            <p>₹${item.price} × ${item.quantity}</p>
            <button onclick="removeItem(${index})">🗑 Remove</button>
        `;
        cartList.appendChild(li);
    });

    totalPriceEl.textContent = total.toFixed(2);

    if (placeOrderBtn) {
        placeOrderBtn.style.display = cart.length > 0 ? 'inline-block' : 'none';
    }
}

// ✅ Handle Place Order
function placeOrder() {
    const isLoggedIn = document.body.getAttribute('data-logged-in') === 'true';

    if (!isLoggedIn) {
        alert("Please log in to place an order.");
        window.location.href = "/login";
        return;
    }

    const address = prompt("Enter your delivery address:");
    if (!address) return alert("Order cancelled. No address provided.");

    const phone = prompt("Enter your phone number:");
    if (!phone) return alert("Order cancelled. No phone number provided.");

    const payment = prompt("Choose payment method:\n1. UPI\n2. Card\n3. Cash on Delivery");
    if (!payment) return alert("Order cancelled. No payment method selected.");

    alert(`✅ Order placed! Your food will be delivered to:\n${address}`);
    localStorage.removeItem('cart');
    updateCartCount();
    window.location.href = "/";
}

// ✅ DOM Ready: Attach Events
document.addEventListener('DOMContentLoaded', () => {
    updateCartCount();
    loadCart();

    // Handle Add to Cart Buttons
    const buttons = document.querySelectorAll('.add-to-cart');
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const id = parseInt(button.getAttribute('data-id'));
            const name = button.getAttribute('data-name');
            const price = parseFloat(button.getAttribute('data-price'));
            addToCart(id, name, price);
        });
    });

    // Handle Place Order Button
    const orderBtn = document.getElementById('placeOrderBtn');
    if (orderBtn) {
        orderBtn.addEventListener('click', placeOrder);
    }
});
