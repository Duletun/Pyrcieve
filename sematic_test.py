import typing


class A:
    class_attrs = None

    def __init__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        self.__test_arg = None

    def __len__(self) -> int:
        return len(self.args) + len(self.kwargs)

    def __bool__(self) -> bool:
        return bool(self.__test_arg)

    def main(self) -> None:
        print('Вызов внутри: A')

    @property
    def test_arg(self) -> typing.Any:
        return self.__test_arg

    @test_arg.setter
    def test_arg(self, value: typing.Any):
        self.__test_arg = value

class B0(A):

    def main(self) -> None:
        print('Вызов внутри: B0 до super')
        super().main()
        print('Вызов внутри: B0 после super')

    @classmethod
    def create(cls, *args, **kwargs) -> 'B':
        return cls(*args, **kwargs)

    @staticmethod
    def get_test() -> str:
        return 'test'

    pass

class B1(A):

    def main(self) -> None:
        print('Вызов внутри: B1 до super')
        super().main()
        print('Вызов внутри: B1 после super')

    @classmethod
    def create(cls, *args, **kwargs) -> 'B':
        return cls(*args, **kwargs)

    @staticmethod
    def get_test() -> str:
        return 'test'

    pass


class B12(B0):

    def main(self) -> None:
        print('Вызов внутри: B12 до super')
        super().main()
        print('Вызов внутри: B12 после super')

    @classmethod
    def create(cls, *args, **kwargs) -> 'B':
        return cls(*args, **kwargs)

    @staticmethod
    def get_test() -> str:
        return 'test'

    pass


class B2(B1, B12):

    def main(self) -> None:
        print('Вызов внутри: B2 до super')
        super().main()
        print('Вызов внутри: B2 после super')

    @classmethod
    def create(cls, *args, **kwargs) -> 'B':
        return cls(*args, **kwargs)

    @staticmethod
    def get_test() -> str:
        return 'test'


class C(B2):

    def main(self) -> None:
        print('Вызов внутри: C до super')
        super().main()
        print('Вызов внутри: C после super')


class F(A):

    def main(self) -> None:
        print('Вызов внутри: F до super')
        super().main()
        print('Вызов внутри: F после super')


class D(F, B1):

    def main(self) -> None:
        print('Вызов внутри: D до super')
        super().main()
        print('Вызов внутри: D после super')


class QWE(C, D):

    def main(self) -> None:
        print('Вызов внутри: QWE до super')
        super().main()
        print('Вызов внутри: QWE после super')


if __name__ == '__main__':
    qwe = QWE()
    qwe.main()
    print(QWE.mro())
    print(dir(QWE))
