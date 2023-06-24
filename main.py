#---------------Object oriented programming----------
#structure/organise code
#better for maintenance and evolutions
#reduce dependancies
#   independant parts of code
#   easily reusable
#imperative programming = follow list of instructions
#   split code into objects
#instance (pizza) -> constructor(auto function when object is created)
#veggie pizza inherits from pizza class
#self/this keyword = specifiy which veriable/method refering to
#constructor syntax = init

#class type begins in uppercase

#pizza class:
#name, price, ingredients, type

class Pizza:
    #instance variables:
    #create optional parameter, see line 22 'vegetarian=False
    def __init__(self, name, price, ingredients, vegetarian=False):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.vegetarian =vegetarian
        
        
    def display(self):
        veg_str = ""
        if self.vegetarian:
            veg_str = " - VEGETARIAN"
            
        print(f"Pizza {self.name} : ${self.price}" + veg_str)
        print("Ingregients: " + ", ".join(self.ingredients))
        print()
    
#inheritance

class CustomPizza(Pizza):
    BASE_PRICE = 7
    PRICE_PER_INGREDIENT = 1.2
    #variable common between all custom pizza:
    last_number = 0
    
    def __init__(self):
        #every new custom pizza is incremented. this variable is unique to custom pizza
        CustomPizza.last_number += 1 
        self.number = CustomPizza.last_number #remember value of last number at time creating object
        
        super().__init__("Custom " +str(self.number), 0, [])
        self.ask_for_ingredients()
        self.compute_price()
        
    def ask_for_ingredients(self):
        print()
        print(f"Ingredients for pizza number {self.number}")
        while True:
            ingredient = input("Add an ingredient (or press enter to finish) : ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"You have {len(self.ingredients)} ingredient(s) : {', '.join(self.ingredients)}")
   
    def compute_price(self):
        self.price = self.BASE_PRICE + len(self.ingredients) * self.PRICE_PER_INGREDIENT
        
     

#pizza1 = Pizza("4 Cheeses", 8.99, ("Brie", "Mozarella", "Feta", "Provolone"))
#pizza1.display()

#"Hawaiian", 10.69, ("Ham", "Pinapple")
#"Veggie", 7.99, ("Mushrooms", "Spinach", "Olives")
#"Pepperoni", 14.99, ("Pepperoni")

pizzas = [
    Pizza("4 Cheeses", 8.99, ("Brie", "Mozarella", "Feta", "Provolone")),
    Pizza("Pepperoni", 14.99, ("Pepperoni", "Tomatoe")),
    Pizza("Veggie", 7.99, ("Mushrooms", "Spinach", "Olives", "Tomatoe"), True),
    Pizza("Hawaiian", 10.69, ("Ham", "Pinapple")),
    CustomPizza(),
    CustomPizza()
]

#sort by name
# def pizza_sort(e):
#     return e.name

#sort by price
# def pizza_sort(e):
#     return e.price

#sort by number of ingredients
# def pizza_sort(e):
#     return len(e.ingredients)

# pizzas.sort(key=pizza_sort)

for i in pizzas:
    i.display()

#display only if vegetarian

# for i in pizzas:
#     if i.vegetarian:
#         i.display()

#display only non vegetarian

# for i in pizzas:
#     if not i.vegetarian:
#         i.display()

#display pizza only if it has tomato

# for i in pizzas:
#     if "Tomatoe" in i.ingredients:
#         i.display()

#only display pizzas less than $10

# for i in pizzas:
#     if i.price < 10:
#         i.display()