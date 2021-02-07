class Robot:
    ''' Представляет робота с именем. '''
    # Переменная класса -  количество роботов ( доступ имеет как класс, так и инстанс )
    population  = 0

    def __init__(self, name):
        ''' Инициализация данных.'''
        self.name = name
        print('(Инициализация {0})'.format(self.name))

        Robot.population += 1

# спец метод __del__, который запускается тогда,
# когда объект больше не использ. и занимаемая им
# оперативная память освобождается:
# 1) Принуд. стирание  - del
# 2) Нет больше ссылки( имени) на этот объект.

    def __del__(self):
        '''Я умираю. '''
        print('{0} уничтожается!'.format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print('{0} был последним.'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов'.format(Robot.population))

    def sayHi(self):
        ''' Приветствие робота.

        Да, они это могут!'''
        print('Приветствую. Мои хозяева называют меня {0}.'.format(self.name))

    @staticmethod      # равнознано howMany = staticmethod(howMany) -  предоставляет доступ к этому методу инстансам класс
    def howMany():
        ''' Выводит численность роботов.'''
        print('У нас всего {0:d} роботов'.format(Robot.population))


droid1 = Robot('R2-D2')
droid1.sayHi()
droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()

print('\n Здесь роботы могут проделать какую-то работу \n')
print('Роботы закончили работу. Давайте их уничтожим')

droid1 = 'droid1 dead'    # Robot('R2-D2') - уничтожен, так как на него нет больше ссылки
del droid2                        # Robot('C-3PO') - уничтожен принудительно.

Robot.howMany()

r_1 = Robot('R1')
r_2 = Robot('R2')
r_3 = Robot('R3')
r_4 = Robot('R4')
r_5 = Robot('R5')
r_6 = Robot('R6')
r_7 = Robot('R7')

r_1.howMany()



