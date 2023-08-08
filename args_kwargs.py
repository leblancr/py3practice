# def order_pizza(size, *args, **kwargs):
def order_pizza(size, *toppings, **details):    
    print(f"ordering a {size} pizza with the following toppings")
    
    for topping in toppings:
        print(f" - {topping}")
        
    print("order details") 
    for k, v in details.items():
        print(f"- {k}: {v}")
        
        
order_pizza('large', 'pepperoni', 'olives', delivery=True, tip=5)
