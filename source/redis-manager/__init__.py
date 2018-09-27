
from settings import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD
from routes import Routes

# Import the necessary packages
from consolemenu import *
from consolemenu.items import *

rout = Routes()
# rout.insert_new_route('perro', ['San Jose', 'Managua', 'New York'], ['11/13/18', '15/12/18'])
# #print(rout.get_route('lala'))
# # rout.get_all_routes()
# rout.plot_graph_route('perro')
# rout.plot_cities_route('perro')
# # print(rout.bloom_filter('Hello22'))


# Seeds Routes

rout.insert_new_route('hmsa48', ['Costa Rica', 'Panama', 'New York'], ['26/09/18-11:00:00', '26/09/18-11:00:00'])



def create_new_route():
    array_places = []
    array_times = []
    name = str(input("Enter your route name (string): "))

    num_places = int(input("Enter number of cities (int): "))
    for i in range(0, num_places):
        array_places.append(str(input("Enter city name (string): ")))
        if i < num_places-1:
            array_times.append(str(input("Enter departure datetime (dd/mm/yyy-hh:mm:ss): ")))
    flag = rout.insert_new_route(
        route_name=name,
        places=array_places,
        times=array_times
    )
    if flag:
        print("Ruta Insertada con éxito")
    else:
        print("Ruta repetida")

def plot_graph():
    name = str(input("Enter your route name (string): "))
    rout.plot_graph_route(name)

def plot_map():
    name = str(input("Enter your route name (string): "))
    try:
        rout.plot_cities_route(name)
    except:
        pass

# Create the menu
menu = ConsoleMenu("Welcome to Airplane System", "Hello World")

# Create some items

# MenuItem is the base class for all items, it doesn't do anything when selected
menu_item = MenuItem("Menu Item")

# A FunctionItem runs a Python function when selected
function_item1 = FunctionItem("Enter New Route", create_new_route)
function_item2 = FunctionItem("Plot graph", plot_graph)
function_item3 = FunctionItem("Plot routes in map", plot_map)


# # A CommandItem runs a console command
# command_item = CommandItem("Run a console command",  "touch hello.txt")

# A SelectionMenu constructs a menu from a list of strings
selection_menu = SelectionMenu([function_item2, function_item3])

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("Plot", selection_menu, menu)

# Once we're done creating them, we just add the items to the menu
menu.append_item(function_item1)
menu.append_item(function_item2)
menu.append_item(function_item3)

# Finally, we call show to show the menu and allow the user to interact
menu.show()