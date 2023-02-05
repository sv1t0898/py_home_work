from os import system

class Menu: # Класс меню
    """
    класс меню
    elements = список кортежей
        кортеж = ("маркер", "описание", метод)
        если метод в кортеже ==-1 то menu.run() возвращает True
        это нужно для реализации выхода из меню реализованых
        во вложении методах"""

    def __init__(self, element=[]):
        self.element = element
    def print(self):
        for (mark, text, _) in self.element:
            print("{} - {}".format(mark, text))

    def run(self, prompt="выберете команду: "):
        def clrscr(): 
            return system("cls")
        while (True):
            clrscr()
            self.print()
            user_chice = input(prompt)
            for (mark, _, rummethod) in self.element:
                if user_chice == mark:
                    if rummethod ==-1:
                        return True
                    clrscr()
                    rummethod()
                    input("Нажми 'Enter' для возврата в меню.")
                    break

    def __len__(self): # размер меню
        return len(self.element)