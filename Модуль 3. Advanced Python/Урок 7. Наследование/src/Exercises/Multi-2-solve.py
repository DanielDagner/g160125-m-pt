# Описание задачи:
#
# Создайте четыре класса: A, B, C и D. Класс D должен наследовать от классов B и C,
# которые в свою очередь наследуют от класса A. В каждом классе переопределите метод say_hello(),
# который выводит уникальное сообщение для каждого класса. Используйте множественное наследование и вызовы super() в
# методах классов B и C.
#
# Определите порядок вызова методов при вызове метода say_hello() для экземпляра класса D и объясните результат,
# используя метод разрешения порядка (MRO).
#
# Требования:
# Классы должны переопределять метод say_hello().
# Класс D должен корректно наследовать от классов B и C.
# Используйте метод разрешения порядка (MRO) для объяснения порядка вызова методов.

class A:
    def say_hello(self):
        print("Hello from A")
        super().say_hello()


class B(A):
    def say_hello(self):
        print("Hello from B")
        super().say_hello()


class C(A):
    def say_hello(self):
        print("Hello from C")
        super().say_hello()


class D(B, C):
    def say_hello(self):
        print("Hello from D")
        super().say_hello()


def main():
    # Тестирование
    d = D()
    d.say_hello()

    # Проверка MRO
    print(D.__mro__)


if __name__ == "__main__":
    main()
