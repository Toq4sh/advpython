# Класс банковского счёта
class BankAccount:
    def __init__(self, owner, balance=0):
        # Приватное поле владельца счёта
        self.__owner = owner

        # Приватное поле баланса
        self.__balance = balance

    def deposit(self, amount):
        # Пополнение счёта (только если сумма положительная)
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        # Снятие денег (если хватает средств и сумма корректная)
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        # Возвращает текущий баланс
        return self.__balance


# Создаём банковский счёт
acc = BankAccount("Tom", 1000)

# Пополняем счёт на 500
acc.deposit(500)

# Снимаем 300
acc.withdraw(300)

# Выводим текущий баланс
print(acc.get_balance())
