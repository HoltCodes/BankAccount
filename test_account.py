class BankAccount():
  accounts = []
  def __init__(self, int_rate, balance): 
    self.int_rate = int_rate
    self.balance = balance

  def deposit(self, amount):
    self.deposit += amount
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


checking = BankAccount (.03, 500)
savings = BankAccount (.05, 1000)