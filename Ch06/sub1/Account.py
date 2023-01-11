class Account:

    def __init__(self, bank, id, name, balance):
        self._bank = bank
        self._id = id
        self._name = name
        self._balance = balance

    def deposit(self, money):
        self._balance += money

    def withdraw(self, money):
        self._balance -= money

    def show(self):
        print('은행명 :', self.bank)
        print('계좌번호 :', self.id)
        print('입금주 :', self.name)
        print('현재잔액 :', self.balance)