class BankAccount():
  accounts = []
  def __init__(self, int_rate, balance): 
    self.int_rate = int_rate
    self.balance = balance
    BankAccount.accounts.append(self)

  def deposit(self, amount):
    self.balance += amount
    return self

  def withdraw(self, amount):
    if(self.balance - amount) >= 0:
      self.balance -= amount
    else:
      print("Insuffcient Funds: Charging a $5 fee")
      self.balance -= 5
    return self

  def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

  def yield_interest(self):
    if self.balance > 0:
      self.balance += (self.balance * self.int_rate)
      return self

  @classmethod
  def print_all_accounts(cls):
    for account in cls.accounts:
      account.display_account_info()


checking = BankAccount (.03, 500)
savings = BankAccount (.05, 1000)

checking.deposit(30).deposit(50).deposit(20).withdraw(50).display_account_info()
savings.deposit(25).deposit(50).withdraw(25).withdraw(25).display_account_info()

BankAccount.print_all_accounts()