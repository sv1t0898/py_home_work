
class Fun():

    def __init__(self, path):
        self.path = path

    def file(self, funct=lambda x:x, mode="r+"):
        self.funct = funct
        self.mode = mode
        with open(self.path, mode, encoding="utf-8") as f:
            funct(f)
            f.seek(0)
            if mode != "a":
                return self.get_file(f)

    def get_file(self, file):
        result = []
        for line in file:
            result.append(line.split())
        return result

    def prnt(self, file):
        f = file.read()
        print(f)

    def search(self, file):
        lst = self.get_file(file)
        inp = str(input())
        a = []
        l = []
        for i in range(len(lst)):
            for n in range(len(lst[i])):
                if inp.lower() in lst[i][n].lower():
                    print(" ".join(lst[i]))
                    a.append(i)
                    l = list(lst)
                    break
        return a, l
                    

    def add(self, file):
        file.write("\n" + input())

    def delit(self, f):
        l, dirr = self.search(f)
        dir = []
        for i in range(len(dirr)):
            if i not in l:
                dir.append(dirr[i])
        self.file(lambda file:file.writelines("\n" + " ".join(i) for i in dir), "w")

    def change(self, f):
        l, dir = self.search(f)
        for i in l:
            dir[i][3] = input("введите новый номер: ")
        self.file(lambda file:file.writelines("\n" + " ".join(i) for i in dir), "w")