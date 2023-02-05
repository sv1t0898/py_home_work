from functions import Fun

bus = Fun("./bus.txt")
driver = Fun("./driver.txt")
route = Fun("./marshrut.txt")


def print_bus():
    bus.file(bus.prnt)

def add_bus():
    print("Введите запись в формате - 'bus№, гос.номер,':")
    bus.file(bus.add, "a")

def print_driver():
    driver.file(driver.prnt)

def add_driver():
    print("Введите запись в формате - 'drive№, фамилия,':")
    driver.file(driver.add, "a")

def print_route():
    bus_list = bus.file()
    driver_list = driver.file()
    route_list = route.file()
    for i in range(len(route_list)):
        for n in range(len(bus_list)):
            if route_list[i][2] == bus_list[n][0]:
                route_list[i][2] = bus_list[n][1]
        for m in range(len(driver_list)):
            if route_list[i][3] == driver_list[m][0]:
                route_list[i][3] = driver_list[m][1]
    for i in route_list: print(" ".join(i))

def add_route():
    print("Введите запись в формате - 'm№, номер маршрута, bus№, driver№,':")
    route.file(route.add, "a")

def clear_screen():
    print("7")