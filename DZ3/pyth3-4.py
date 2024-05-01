class Wallet:
    payment_system = "Visa"  
    
    def __init__(self, name: str, currency: str):
        
        self._balance = 0  
        self.name = name
        self.currency = currency
    
    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Сумма должна быть положительной")
        
        self._balance += amount
        print(f"Успешно внесено {amount} {self.currency}")
    
    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Сумма должна быть положительной")
        
        if self._balance >= amount:
            self._balance -= amount
            print(f"Успешно выведено {amount} {self.currency}")
        else:
            print("Недостаточно средств")
    
    def get_balance_info(self):
        print(f"Баланс: {self._balance} {self.currency}")
    
    def close_account(self):
        self._balance = 0
        print("Аккаунт закрыт")


my_wallet = Wallet("Мой кошелёк", "USD")
my_wallet.deposit(100)
my_wallet.get_balance_info()
my_wallet.withdraw(50)
my_wallet.get_balance_info()
my_wallet.withdraw(70)  
my_wallet.close_account()
my_wallet.get_balance_info()

