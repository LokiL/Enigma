__author__ = 'Арслан'
class enigmawheel():
    def __init__(self, wheel, i, trigger): #инициализация вводом [значений], начального поворота, триггера поворота
        self.wheelpermutation = wheel
        for k in range(i): #начальный поворот колеса
            self.rotate()
        self.currentposition = 0 #обнуляем начальную позицию
        self.nextwheeltrigger = (trigger-i)%26 #установка триггера на поворот следующего колеса
    def rotate(self): #поворот на 1
        t = self.wheelpermutation.pop(0)
        self.wheelpermutation.append(t)
        self.currentposition = (self.currentposition+1)%26 #отсчет позиции и сброс на 26
        pass
    def setdefault(self): #сброс на начальную позицию
        for i in range(26-self.currentposition): #поворачиваем на начало
            self.rotate()
        pass
    def getcif(self, i): #вывод шифра по номеру
        return self.wheelpermutation[i]
    def getplain(self, j): #операция, обратная getcif, вывод номера по шифру
        for i in range(26):
            if (i+self.wheelpermutation[i])%26 == j:
                return i
    def changecurrent(self, l, trigger): #смена текущей позиции
        for k in range(l): #начальный поворот колеса
            self.rotate()
        self.currentposition = 0 #обнуляем начальную позицию
        self.nextwheeltrigger = (trigger-l)%26 #установка триггера на поворот следующего колеса


    currentposition = 0 #текущая позиция
    nextwheeltrigger = 0 #триггер поворота следующего колеса
    wheelpermutation = [] #набор шифров
    pass

#создаем колесики ^_^'
def createnullwheels():
    global Rl, Rm, Rr, T
    Rl = enigmawheel([4,9,10,2,7,1,23,9,13,16,3,8,2,9,10,18,7,3,0,22,6,13,5,20,4,10], 0, 0)
    Rm = enigmawheel([1,2,3,4,5,6,22,8,9,10,13,10,13,0,10,15,18,5,14,7,16,17,24,21,18,15], 0, 16)
    Rr = enigmawheel([4,17,12,18,11,20,3,19,16,7,10,23,5,20,9,22,23,14,1,13,16,8,6,15,24,2], 0, 22)
    T = enigmawheel([24,16,18,4,12,13,5,22,7,14,3,21,2,23,24,19,14,10,13,6,8,1,25,12,2,20], 0, 0)
    pass

def getciftext(k): # получение шифротекста
    #проход по колесам
    buff = Rr.getcif(k)
    buff = Rm.getcif(buff)
    buff = Rl.getcif(buff)
    buff = T.getcif(buff)
    buff = Rl.getplain(buff)
    buff = Rm.getplain(buff)
    buff = Rr.getplain(buff)
    rotatewheels(1)
    return buff

def rotatewheels(i):#поворот колес i раз
    for j in range(i):
        Rr.rotate()
        if Rr.currentposition == Rr.nextwheeltrigger:
            Rm.rotate()
            if Rm.currentposition == Rm.nextwheeltrigger:
                Rl.rotate()
    pass

def createcif(text): #кодировка
    for i in range(len(text)):
        text.insert(i, getciftext(i))
    return text

def decodecombinations():
    decodedpositions = []
    for i in range(26):
        for j in range(26):
            for k in range(26):
                print('Первоначальный подбор: ', i,j,k)
                createnullwheels()
                Rl.changecurrent(i, 0)
                Rm.changecurrent(j, 16)
                Rr.changecurrent(k, 22)
                for letter in range(26):
                    rotatewheels(6)
                    buff1 = getciftext(letter)
                    rotatewheels(3)
                    buff1 = getciftext(buff1)
                    if buff1 == letter:
                        '''
                        Rl.setdefault()
                        Rm.setdefault()
                        Rr.setdefault()
                        rotatewheels(27)

                        buff2 = getciftext(letter)
                        rotatewheels(11)
                        buff2 = getciftext(buff2)
                        if buff2 == letter:
                        '''
                        Rl.setdefault()
                        Rm.setdefault()
                        Rr.setdefault()
                        rotatewheels(1)
                        buff3 = getciftext(letter)
                        rotatewheels(42)
                        buff3 = getciftext(buff3)
                        Rl.setdefault()
                        Rm.setdefault()
                        Rr.setdefault()
                        rotatewheels(15)
                        buff3 = getciftext(buff3)
                        rotatewheels(11)
                        buff3 = getciftext(buff3)
                        Rl.setdefault()
                        Rm.setdefault()
                        Rr.setdefault()
                        rotatewheels(10)
                        buff3 = getciftext(buff3)
                        Rl.setdefault()
                        Rm.setdefault()
                        Rr.setdefault()
                        rotatewheels(9)
                        buff3 = getciftext(buff3)
                        if buff3 == letter:
                            decodedpositions.append([i,j,k,letter])
    return decodedpositions

def decode(combinations):
    lst = []
    createnullwheels()
    for i in combinations:
        print('Вторичный подбор', i)
        Rl.changecurrent(i[0], 0)
        Rm.changecurrent(i[1], 16)
        Rr.changecurrent(i[2], 22)
        for letter in range(26):
            rotatewheels(27)
            buff = getciftext(letter)
            rotatewheels(11)
            buff = getciftext(buff)
            if buff == letter:
                lst.append([i, letter])




print(decode(decodecombinations()))

