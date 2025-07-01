class product:
    def __init__(self,name,price,stock):
        self.name=name
        self._price=price
        self.stock=stock
        
    def get_price(self):
        return self._price
    
    def apply_discount(self):
        raise NotImplementedError ("add the discount in the child class")
    
    def reduced_stock(self,quantity):
        if self.stock>quantity:
            self.stock-=quantity
            return True
        else:
            return  False
    
    def __str__(self):
        return f"{self.name} :: price :{self._price}, stock {self.stock}"
class groceries(product):
    def apply_discount(self):
        return self._price
    
class clothing(product):
    def apply_discount(self):
        return self._price*0.8
    
class electronics(product):
    def apply_discount(self):
        return self._price*0.9
    
class shopping_cart:
    def __init__(self):
        self.items={}
        
    def add_to_cart(self,product:product, quantity):
        if product.reduced_stock(quantity):
            if product.name in self.items:
                self.items[product.name]["quantity"]+=quantity
            else:
                self.items[product.name]={
                    'product':product,"quantity":quantity}
        else:
            print(f"not enough stock {product.name}")
    
    def calculate_total_price(self):
        total=0
        for item in self.items.values():
            Product: product=item["product"] 
            total+=Product.apply_discount()*item['quantity']
        return total 

    def checkout(self):
        if self.items:
            print("----------------------------------------- Your order summary ----------------------------------------------")
            message=''
            for key, value in self.items.items():
                message+=f'{value["quantity"]} X {key} \t price: {value["product"].get_price()} rupees \n '
            print(f" the items in the cart are : \n {message} \n Total price {self.calculate_total_price()}")
            self.items.clear()
        else:
            return "add itms in the cart"
              
    def __str__(self):
        if self.items:
            message=''
            for key, value in self.items.items():
                message+=f'{value["quantity"]} X {key} \t price: {value["product"].get_price()} rupees\n '
            return f" the items in the cart are : \n {message} \n Total price {self.calculate_total_price()}"
        else:
            return "add itms in the cart"
        
laptop=electronics("Laptop",50000,20)
laptop.reduced_stock(5)
tshirt=clothing("TShirt",500,100)
soap=groceries("Soap",40,150)
print("------------------------------------------------------------- stock item are ---------------------------------------------------------")
print(laptop)
print(tshirt)
print(soap)
print("---------------------------------------------------------------shopping cart------------------------------------------------------------")
cart=shopping_cart()
cart.add_to_cart(laptop,1)
cart.add_to_cart(laptop,5)
cart.add_to_cart(soap,10)
print(cart)
cart.checkout()
