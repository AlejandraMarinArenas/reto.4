from datetime import date
import matplotlib.pyplot as plt
import numpy as np


class User():
    def __init__(self, id:int, user_name:str, balance:float):
        self.user_name = user_name
        self.id = id
        self.balance = balance
        self.orders_list = []
        self.products_in_car = []

    def __str__(self):
        txt = "El usuario {0} con id {1} cuenta con un balance de {2} con una orden de{3}"
        return txt.format(self.user_name, self.id, self.balance, self.order_list)

    def add_product_to_car(self, products):
        for x in range(len(products)):
            self.products_in_car.append(products[x])

    def consolidate_order(self, id, date, stat:bool):
        total=0
        for i in range(len(self.products_in_car)):
            total=self.products_in_car[i].price + total

        if self.balance >= total:
            NOrder=Order(id, date, total, stat, self.products_in_car)
            self.orders_list.append(NOrder)
            self.balance = total
            self.products_in_car=[]
        else:
            print("Saldo insuficiente")
        
    def add_to_balance(self, NBalance:int):
        self.balance = self.balance + NBalance

    def plot_order_history(self):
        xp = np.array([])
        yp = np.array([len(self.orders_list), len(Usuario1.order_list[0].product_list)])

        plt.plot(xp, yp, 'o')
        return plt.show()

class Order():
    def __init__(self, id:int, date:date, total:float, status:bool,products_list=[]):
        self.id = id
        self.date = date
        self.total = total
        self.status = status
        self.products_list = products_list

    def __str__(self):
        txt = "La orden con id {0} con una lista de ({1}) con fecha de {2} tiene un precio total de {3} con un estado {4}"
        return txt.format(self.id, self.products_list, self.date, self.total, self.status)

class Product():
    def __init__(self, id:int, name:str, price:float):
        self.name = name
        self.id = id
        self.price = price
        self.price_history={}

    def __str__(self):
        txt = "El id del producto {1} con nombre {0} tiene un precio de {2} con un historial de precios desde {3}"
        return txt.format(self.name, self.id, self.price, self.price_history)

    def update_price(self, date, New_price:float):
        self.price_history[date] = self.price
        self.price = New_price


Usuario1 = User(1, "Flavia", 51023)
Usuario2 = User(2, "Jhon", 69003)
Usuario3 = User(3, "Felipe", 125000)
Usuario4 = User(4, "Samuel", 23450)

producto1 = Product(1000, "Pollo a la brasa", 2500)
producto2 = Product(1001, "Turrón", 2000)
producto3 = Product(1002, "Alfajores", 3000)
producto4 = Product(1003, "Causa", 1500)
producto5 = Product(1004, "Tallarines rojos", 1500)
producto6 = Product(1005, "Mazamorra", 1800)

Usuario1.add_product_to_car([producto1, producto3, producto4])
Usuario1.consolidate_order(1, "27/01/2022", True)

Usuario3.add_product_to_car([producto1, producto5, producto6])
Usuario3.consolidate_order(2, "18/4/2022", True)

Usuario1.add_product_to_car([producto4, producto1, producto2])
Usuario1.consolidate_order(3,"26/12/2022", True)

Usuario4.add_product_to_car([producto2, producto6, producto3])
Usuario4.consolidate_order(4, "10/08/2022", True)


print(Usuario1.orders_list[0].total)
print(Usuario3.orders_list[0].total)
print(Usuario4.orders_list[0].total)


print(Usuario2.balance)
Usuario2.add_to_balance(1101010)
print(Usuario2.balance)

producto2.update_price((4,12,2022), 7000)
print(producto2)


producto2.update_price((1,10,2022),8000)
print(producto2)
print(producto3)