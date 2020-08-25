from decimal import Decimal as dc
from dataclasses import dataclass
print("\n\tFIRST TASK\n")


@dataclass
class Value:
    amount: float
    currency: str


class ATM:
    min_limit = 0
    max_limit = 0
    bank_name = 'Mono'

    def __init__(self, amount):
        self.initial_amount = self._validate_amount(amount)
        self.max_limit = 1000
        self.currency = 'UAH'
        self.curr_map = {'UAH': 1, 'USD': 27.8, 'EUR': 32.2}

    def _validate_amount(self, amout):
        if amout < 0:
            raise ValueError
        return amout

    def add_money(self, value, cur='UAH'):
        if cur == "USD" or cur == "EUR" or cur == "UAH":
            value = float(dc(str(value)) * dc(str(self.curr_map[cur])))
        else:
            return ValueError

        self.initial_amount += value
        return self.initial_amount

    def withdraw(self, amount, cur="UAH"):
        if self.initial_amount < amount:
            raise ValueError('Not enough money')
        elif amount > self.max_limit:
            raise ValueError(')))))')
        if cur == "USD" or cur == "EUR" or cur == "UAH":
            amount = float(dc(str(amount)) * dc(str(self.curr_map[cur])))
        else:
            return ValueError

        self.initial_amount -= amount
        return self.initial_amount


# MAIN
card = ATM(1000)
print(card.initial_amount)
card.add_money(100, "USD")
print(card.initial_amount)
print(card.withdraw(123, "EUR"))