# Abstraction hides the complex logic of an online shopping system.

"""
Definition: Abstraction hides unnecessary details and shows only the relevant information. It helps in reducing complexity.

Real-Life Example:

ATM Machine: You only see the user interface to withdraw money, but the internal processing remains hidden.

"""



from abc import ABC, abstractmethod

# Abstract Class
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Child Classes
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ₹{amount}")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ₹{amount}")

# Using abstraction
def make_payment(payment_method, amount):
    payment_method.process_payment(amount)

# Payment Process
cc_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

make_payment(cc_payment, 5000)
make_payment(paypal_payment, 3000)


"""
Explanation
Abstraction: The Payment class abstracts payment methods using the @abstractmethod.

Polymorphism: process_payment() is implemented differently in CreditCardPayment and PayPalPayment.

Loose Coupling: The make_payment() function works with any payment class implementing Payment.
"""