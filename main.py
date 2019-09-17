from flask import Flask, render_template, request
import json
import uuid


app = Flask(__name__, static_url_path='', static_folder='static')
products=[]

@app.route('/HomePage')
def HomePage():
    global products
    f = open('products.txt', "r")
    products = json.load(f)
    f.close()
    return render_template('HomePage.html', products=products)

@app.route('/NewProduct')
def NewProduct():
    return render_template('NewProduct.html')

@app.route('/About')
def About():
    return render_template('About.html')


@app.route('/send_data', methods=['POST'])
def send_data():
    if "id" not in request.form:
        uu_id = str(uuid.uuid4())
        product={"product_name": request.form["product_name"], "desired_price": request.form["desired_price"], "url": request.form["url"], "id": uu_id }
        products.append(product)
        f=open('products.txt', "w")
        json.dump(products, f)
        f.close()
        return render_template('msg.html', msg="The product was added!")
    else:
        for product in products:
            if product['id'] == request.form["id"]:
                product["product_name"] = request.form["product_name"]
                product["url"] = request.form["url"]
                product["desired_price"] = request.form["desired_price"]
                break
        f = open('products.txt', "w")
        json.dump(products, f)
        f.close()
        return render_template('msg.html', msg="The product was edited!")


@app.route('/delete/<id>')
def delete_item(id):
    for product in products:
        if product['id'] == id:
            products.remove(product)
            break
    f = open('products.txt', "w")
    json.dump(products, f)
    f.close()
    return render_template('msg.html', msg="The product was deleted")


@app.route('/editProduct/<id>')
def edit_product(id):
    for product in products:
        if product['id'] == id:
            return render_template('editProduct.html', product=product)


if __name__ == '__main__':
    f = open('products.txt', "r")
    products = json.load(f)
    f.close()
    app.run()
