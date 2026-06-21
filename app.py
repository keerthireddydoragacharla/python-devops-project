from flask import Flask, render_template

app = Flask(__name__)

cart = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/product/<name>")
def product_details(name):
    return render_template("product.html", product=name)

@app.route("/add-to-cart/<product>")
def add_to_cart(product):
    cart.append(product)
    return f"{product} added to cart! <br><br> <a href='/cart'>View Cart</a>"

@app.route("/cart")
def view_cart():
    return render_template("cart.html", cart=cart)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)