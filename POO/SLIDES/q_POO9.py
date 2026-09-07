class temperatura:
    def __init__(self, celsius: float):
        self.celsius = celsius

    @classmethod
    def de_celsius(cls, valor: float) -> "temperatura":
        return cls(valor)

    @classmethod
    def de_fahrenheit(cls, valor: float) -> "temperatura":
        return cls((valor - 32) * 5 / 9)