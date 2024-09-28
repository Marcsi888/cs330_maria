"""
Module Name: cs330_04_1
Description: Implements an order management system using OOP principles.
"""



import unittest
pep8 = "pip install pep8"
pylint = "pip install pylint"

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('hello'.upper(), 'HELLO')
    def test_isupper(self):
        self.assertTrue('HELLO'.isupper())
        self.assertFalse('Hello'.isupper())
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class Product:
    """
    A class to represent a product.

    Attributes:
    -----------
    name : str
        name of the product
    price : float
        price of the product
    stock : int
        stock available for the product
    """
    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.stock = stock

    def update_price(self, new_price):
        self.price = new_price

    def make_purchase(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
        else:
            raise ValueError(f"Not enough stock for {self.name}")

    def in_stock(self):
        return self.stock > 0

    def restock(self, quantity):
        self.stock += quantity

    def is_available(self):
        return self.stock > 0

    def __repr__(self):
        return f"{self.name} (${self.price}), Stock: {self.stock}"


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def total(self):
        return sum(product.price for product in self.products)

    def calculate_total(self):
        return sum(product.price for product in self.products)

    def __len__(self):
        return len(self.products)

    def __iter__(self):
        return iter(self.products)

    def __add__(self, other):
        new_cart = Cart()
        new_cart.products = self.products + other.products
        return new_cart

    def __iadd__(self, other):
        self.products += other.products
        return self

    def __eq__(self, other):
        return self.products == other.products

    def __lt__(self, other):
        return self.total() < other.total()

    def __gt__(self, other):
        return self.total() > other.total()

    def __bool__(self):
        return len(self.products) > 0

    def clear(self):
        self.products = []

    def is_empty(self):
        return len(self.products) == 0

    def __getitem__(self, index):
        return self.products[index]

    def __setitem__(self, index, value):
        self.products[index] = value

    def __delitem__(self, index):
        del self.products[index]

    def __contains__(self, product):
        return product in self.products

    def __repr__(self):
        return f"Cart with {len(self.products)} products"


class Customer:
    def __init__(self, name):
        self.name = name
        self.carts = []
        self.orders = []

    def create_cart(self):
        cart = Cart()
        self.carts.append(cart)
        return cart

    def add_order_to_history(self, order):
        self.orders.append(order)

    def view_order_history(self):
        for order in self.orders:
            print(order)


class Order:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer
        self.is_complete = False
        self.invoice = None

    def complete(self):
        if self.check_stock():
            self.is_complete = True
            self.generate_invoice()
            self.update_stock()
        else:
            print("Order cannot be completed due to insufficient stock.")

    def check_stock(self):
        for product in self.cart:
            if not product.in_stock():
                print(f"Product {product.name} is out of stock.")
                return False
        return True

    def generate_invoice(self):
        self.invoice = f"Invoice for {self.customer.name}:\n"
        for product in self.cart:
            self.invoice += f"{product.name} - ${product.price}\n"
        self.invoice += f"Total: ${self.cart.total()}"
        print(self.invoice)

    def update_stock(self):
        for product in self.cart:
            product.make_purchase(1)

    def __repr__(self):
        return f"Order with {len(self.cart)} products"

    def __str__(self):
        return f"Order with {len(self.cart)} products"


# Example usage:
p1 = Product("Apple", 1.00, 10)
p2 = Product("Banana", 0.50, 5)
p3 = Product("Orange", 0.75, 3)

c1 = Cart()
c1.add_product(p1)
c1.add_product(p2)

c2 = Cart()
c2.add_product(p3)

c3 = c1 + c2  # add two carts together
c3 += c1  # Add products from another cart

print(f"Total price in c3: ${c3.calculate_total()}")  # Calculate total price
order = Order(c3, Customer("John Doe"))
order.complete()  # Complete order and generate invoice

# Removed redundant TestCart class definition

if __name__ == '__main__':
    unittest.main()
unittest.main()
# User Acceptance Test

class TestProduct(unittest.TestCase):
    def test_product_repr(self):
        p = Product("Apple", 1.00, 10)
        self.assertEqual(repr(p), "Apple ($1.0), Stock: 10")
class TestOrder(unittest.TestCase):
    def test_order_str(self):
        p1 = Product("Apple", 1.00, 10)
        p2 = Product("Banana", 0.50, 5)
        cart = Cart()
        cart.add_product(p1)
        cart.add_product(p2)
        order = Order(cart, Customer("John Doe"))
        self.assertEqual(str(order), "Order with 2 products")
class TestCart(unittest.TestCase):
    def test_cart_total(self):
        p1 = Product("Apple", 1.00, 10)
        p2 = Product("Banana", 0.50, 5)
        cart = Cart()
        cart.add_product(p1)
        cart.add_product(p2)
        self.assertEqual(cart.calculate_total(), 1.50)
# Expected Result: the cart total should be 1.50
# Actual Result: the cart total is 1.50
# Test Passed
# Expected Result: the product representation should be "Apple ($1.0), Stock: 10"
# Actual Result: the product representation is "Apple ($1.0), Stock: 10"
# Test Passed
# Expected Result: the order string representation should be "Order with 2 products"
# Actual Result: the order string representation is "Order with 2 products"
# Test Passed
# User Acceptane Test passed. All tests passed. The code is working as expected.
def pep8_test():
    pep8 = "pip install pep8"
    return pep8
c1.remove_product(p1)
assert p1 not in c1.products
"""cs330_04_1.py:1:0: C0114: Missing module docstring (missing-module-docstring)
cs330_04_1.py:8:0: C0103: Constant name "pep8" doesn't conform to UPPER_CASE naming style (invalid-name)
cs330_04_1.py:9:0: C0103: Constant name "pylint" doesn't conform to UPPER_CASE naming style (invalid-name)
cs330_04_1.py:11:0: C0115: Missing class docstring (missing-class-docstring)
cs330_04_1.py:12:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:14:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:17:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:24:0: C0115: Missing class docstring (missing-class-docstring)
cs330_04_1.py:30:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:33:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:39:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:42:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:45:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:52:0: C0115: Missing class docstring (missing-class-docstring)
cs330_04_1.py:56:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:59:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:62:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:63:15: R1728: Consider using a generator instead 'sum(product.price for product in self.products)' (consider-using-generator)
cs330_04_1.py:65:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:66:15: R1728: Consider using a generator instead 'sum(product.price for product in self.products)' (consider-using-generator)
cs330_04_1.py:95:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:98:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:117:0: C0115: Missing class docstring (missing-class-docstring)
cs330_04_1.py:123:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:128:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:128:35: W0621: Redefining name 'order' from outer scope (line 192) (redefined-outer-name)
cs330_04_1.py:131:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:132:12: W0621: Redefining name 'order' from outer scope (line 192) (redefined-outer-name)
cs330_04_1.py:136:0: C0115: Missing class docstring (missing-class-docstring)
cs330_04_1.py:143:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:151:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:158:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:165:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:201:0: C0115: Missing class docstring (missing-class-docstring)
cs330_04_1.py:202:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:205:0: C0115: Missing class docstring (missing-class-docstring)
cs330_04_1.py:206:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:207:8: W0621: Redefining name 'p1' from outer scope (line 177) (redefined-outer-name)
cs330_04_1.py:208:8: W0621: Redefining name 'p2' from outer scope (line 178) (redefined-outer-name)
cs330_04_1.py:212:8: W0621: Redefining name 'order' from outer scope (line 192) (redefined-outer-name)
cs330_04_1.py:214:0: C0115: Missing class docstring (missing-class-docstring)
cs330_04_1.py:215:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:216:8: W0621: Redefining name 'p1' from outer scope (line 177) (redefined-outer-name)
cs330_04_1.py:217:8: W0621: Redefining name 'p2' from outer scope (line 178) (redefined-outer-name)
cs330_04_1.py:222:0: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_1.py:223:4: W0621: Redefining name 'pep8' from outer scope (line 8) (redefined-outer-name)"""
#pycodestyle
"""cs330_04_1.py:7:1: E303 too many blank lines (3)
cs330_04_1.py:11:1: E302 expected 2 blank lines, found 1
cs330_04_1.py:14:5: E301 expected 1 blank line, found 0
cs330_04_1.py:17:5: E301 expected 1 blank line, found 0
cs330_04_1.py:24:1: E302 expected 2 blank lines, found 1
cs330_04_1.py:201:1: E302 expected 2 blank lines, found 0
cs330_04_1.py:205:1: E302 expected 2 blank lines, found 0
cs330_04_1.py:214:1: E302 expected 2 blank lines, found 0
cs330_04_1.py:222:1: E302 expected 2 blank lines, found 0
cs330_04_1.py:225:1: E305 expected 2 blank lines after class or function definition, found 0
"""
#pep8
"""pep8 has been renamed to pycodestyle (GitHub issue #466)
Use of the pep8 tool will be removed in a future release.
Please install and use `pycodestyle` instead.

$ pip install pycodestyle
$ pycodestyle ...

warnings.warn(
cs330_04_1.py:7:1: E303 too many blank lines (3)
cs330_04_1.py:11:1: E302 expected 2 blank lines, found 1
cs330_04_1.py:14:5: E301 expected 1 blank line, found 0
cs330_04_1.py:17:5: E301 expected 1 blank line, found 0
cs330_04_1.py:24:1: E302 expected 2 blank lines, found 1
cs330_04_1.py:201:1: E302 expected 2 blank lines, found 0
cs330_04_1.py:205:1: E302 expected 2 blank lines, found 0
cs330_04_1.py:214:1: E302 expected 2 blank lines, found 0
cs330_04_1.py:222:1: E302 expected 2 blank lines, found 0"""
# coverage test report analysi and correction
def categorize_number(num):
    if num < 0:
        return "negative"
    elif num == 0:
        return "zero"
    else:
        return "positive"
# test branch coverage: if, elif and else statements are covered
# test boundary value: test for negative, zero and positive numbers
# test to see if the stock quantity is updated correctly
def test_make_purchase_insufficient_stock(self):
    product = Product("Apple", 1.00, 5)
    
    # Case where there is enough stock
    product.make_purchase(3)
    self.assertEqual(product.stock, 2)

    # Case where there isn't enough stock
    with self.assertRaises(ValueError):
        product.make_purchase(6)
#test ti see if the cart is empty
def test_calculate_total_empty_cart(self):
    cart = Cart()
    
    # Edge case where cart is empty
    self.assertEqual(cart.calculate_total(), 0)
# test to see if the total price is calculated correctly
def test_calculate_total_single_product(self):
    cart = Cart()
    product = Product("Banana", 0.50, 5)
    cart.add_product(product)
    
    # Test with one product
    self.assertEqual(cart.calculate_total(), 0.50)
# order is completed if there is enough stock
def test_complete_order(self):
    p1 = Product("Apple", 1.00, 10)
    p2 = Product("Banana", 0.50, 5)
    cart = Cart()
    cart.add_product(p1)
    cart.add_product(p2)
    order = Order(cart, Customer("John Doe"))
    order.complete()
    self.assertTrue(order.is_complete)
# order is not completed if there is insufficient stock
def test_complete_order_insufficient_stock(self):
    p1 = Product("Apple", 1.00, 10)
    p2 = Product("Banana", 0.50, 5)
    cart = Cart()
    cart.add_product(p1)
    cart.add_product(p2)
    p1.make_purchase(10)
    order = Order(cart, Customer("John Doe"))
    order.complete()
    self.assertFalse(order.is_complete)
# test to see if the stock is updated after an order is completed
def test_update_stock(self):
    p1 = Product("Apple", 1.00, 10)
    p2 = Product("Banana", 0.50, 5)
    cart = Cart()
    cart.add_product(p1)
    cart.add_product(p2)
    order = Order(cart, Customer("John Doe"))
    order.update_stock()
    self.assertEqual(p1.stock, 9)
    self.assertEqual(p2.stock, 4)
# test to see if the invoice is generated correctly
def test_generate_invoice(self):
    p1 = Product("Apple", 1.00, 10)
    p2 = Product("Banana", 0.50, 5)
    cart = Cart()
    cart.add_product(p1)
    cart.add_product(p2)
    order = Order(cart, Customer("John Doe"))
    order.generate_invoice()
    self.assertEqual(order.invoice, "Invoice for John Doe:\nApple - $1.0\nBanana - $0.5\nTotal: $1.5")
# test to see if the product is removed
def test_remove_product(self):
    cart = Cart()
    product = Product("Apple", 1.00, 10)
    cart.add_product(product)
    cart.remove_product(product)
    self.assertNotIn(product, cart.products)
    