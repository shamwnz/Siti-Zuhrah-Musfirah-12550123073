class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise ValueError("Deposit amount must be greater than zero")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError("Insufficient funds or invalid withdrawal amount")

    def get_balance(self):
        return self.balance

# unittest

import unittest

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Zura", 150)

    def test_deposit(self):
        result = self.account.deposit(50)
        self.assertEqual(result, 200)
    
    def test_withdraw(self):
        result = self.account.withdraw(50)
        self.assertEqual(result, 100)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 150)

    def test_deposit_invalid(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_withdraw_invalid(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)
if __name__ == '__main__':
    unittest.main()
