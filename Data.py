import  json
class Pizza():
    name = '';
    price = 0;
    ingredients = set();
    def __str__(self):
        out = "";
        for ingridient in self.ingredients:
            out += str(ingridient) + " ";
        out = self.name+ " " + str(self.price)+ " " + out;
        return out;
    def __init__(self,name,price,ingredients):
        self.name = name;
        self.price = price;
        self.ingredients = ingredients;
        self.data = []
    def __init__(self):
        self.name = "nil";
        self.price = 0;
        self.ingredients = set();
    def count_ingridient_type(self,ingridient_type):
        return len(self.ingredients & ingridient_type.ingridients)
    def count_ingridents_like(self,ingredient_pattern):
        count_ingredient_pattern = 0;
        for ingrident in self.ingredients:
            if(ingrident.find(ingredient_pattern) != -1):
                count_ingredient_pattern += 1;
                continue;
        return count_ingredient_pattern;        
    
class Data:
    pizzas = [];
    def __init__(self,input_file):

        with open(input_file) as json_file:
            data = json.load(json_file)
        data_pizzas = data["pizzas"]
        pizzas = []
        for pizza in data_pizzas:
            addThis = Pizza();
            for value in pizza:
                if(value == "price"):
                    addThis.price = pizza[value]
                if(value != "price" and value != "nil"):
                    addThis.name = value;
                    for ingridient in pizza[value]["ingredients"]:
                        addThis.ingredients.add(ingridient)
            if(addThis.name != 'nil'):
                pizzas.append(addThis);
        self.pizzas =  pizzas;
    def __str__(self):
        out = "";
        for pizza in self.pizzas:
            out+=str(pizza)
            out+="\n"
        return out;
    
class IngridientType:
    name = "";
    ingridients = set();
    def __init__(self,name,ingridients):
        self.name = name;
        self.ingridients = ingridients;
        
def cheapest(pizzas):
    min = 9999999;
    minPizza = Pizza();
    for pizza in pizzas:
        if(pizza.price < min):
            min = pizza.price;
            minPizza = pizza;
    return minPizza;

def percentage(pizzas,count):
    return len(pizzas) / float(count) * 100

def printPizzas(pizzas):
    for pizza in pizzas:
        print(pizza)
        
def printPizzaResults(pizzas,numberOfPizzas):
    print("Najeftinija: " + str(cheapest(pizzas)))
    print("cine posto " + str(percentage(pizzas, numberOfPizzas)) + "%")
    
data = Data("pizza.json");
meat = IngridientType("Meat", set(["minced_meat","cocktail_sausages","minced_beef","ham","kebab","salami","sausage"]));
chees = IngridientType("Chees", set(["mozzarella_cheese","mozzarella","parmesan_cheese","blue_cheese","goat_cheese"]));
seaFruit = IngridientType("Sea fruit", set(["crab_meat","tuna","mussels","shrimps"]));
mushrooms = IngridientType("Mushroom", set(["mushrooms"]));
pizzasChees = []
pizzasMeat = []
pizzaMeatOlive = []
pizzaMozarelaMushrooms = []
for pizza in data.pizzas:
    chessCount = pizza.count_ingridient_type(chees);
    meatCount = pizza.count_ingridient_type(meat)
    oliveCount = pizza.count_ingridents_like("olives")
    mozzarelaCount = pizza.count_ingridents_like("mozzarella")
    mushroomsCount = pizza.count_ingridient_type(mushrooms);
    if(chessCount > 1):
        pizzasChees.append(pizza)
    if(meatCount):
        pizzasMeat.append(pizza)
    if(meatCount and oliveCount):
        pizzaMeatOlive.append(pizza);
    if(mozzarelaCount and mushroomsCount):
        pizzaMozarelaMushrooms.append(pizza)
totalNumberOfPizzas = len(data.pizzas);
pizza_results = [pizzasChees, pizzasMeat, pizzaMeatOlive, pizzaMozarelaMushrooms]
iterator = 0;
answers = []
for pizza_solution in pizza_results:
    print(percentage(pizza_solution,totalNumberOfPizzas))
    solutions = {"percentage" : str(percentage(pizza_solution,totalNumberOfPizzas))+"%", "cheapest" : str(cheapest(pizza_solution))}
    addThis = {"group_"+str(iterator) : solutions}
    answers.append(addThis)
    iterator += 1;

full_name = "Mihajlo Racic"
email = "mihajlo.rac@gmail.com"
code_link = "www.google.com"
pythonDictionary = {'full_name':'Mihajlo Racic', 'email':'mihajlo.rac@gmail.com', 'code_link':'www.google.com'}
pythonDictionary = {'personal_info':pythonDictionary,"answer" : answers}
dictionaryToJson = json.dumps(pythonDictionary)
personal_info = [full_name, email, code_link];
data_string = personal_info
print(dictionaryToJson)
