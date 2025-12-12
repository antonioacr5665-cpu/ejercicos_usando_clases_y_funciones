class CuentaBancaria:
    def __init__(self, titular, balance=0):
        self.titular = titular
        self.balance = balance
    
    def depositar(self, cantidad):
        """Depositar dinero en la cuenta"""
        if cantidad > 0:
            self.balance += cantidad
            print(f" Depósito exitoso: +${cantidad:.2f}")
            self.mostrar_balance()
        else:
            print(" Error: La cantidad a depositar debe ser positiva")
    
    def retirar(self, cantidad):
        """Retirar dinero de la cuenta"""
        if cantidad <= 0:
            print(" Error: La cantidad a retirar debe ser positiva")
        elif cantidad > self.balance:
            print(f" Error: Fondos insuficientes. Balance disponible: ${self.balance:.2f}")
        else:
            self.balance -= cantidad
            print(f" Retiro exitoso: -${cantidad:.2f}")
            self.mostrar_balance()
    
    def mostrar_balance(self):
        """Mostrar el balance actual"""
        print(f" Balance actual de {self.titular}: ${self.balance:.2f}")
    
    def __str__(self):
        return f"Cuenta de {self.titular} - Balance: ${self.balance:.2f}"
#


if __name__ == "__main__":
    print("=== CREANDO CUENTA BANCARIA ===")
    cuenta = CuentaBancaria("Antonio Carvajal", 1000)
    
    print("\n=== ESTADO INICIAL ===")
    cuenta.mostrar_balance()
    
    print("\n=== OPERACIONES DE DEPÓSITO ===")
    cuenta.depositar(500)
    cuenta.depositar(400.75)
    cuenta.depositar(-100) 
    
    print("\n=== OPERACIONES DE RETIRO ===")
    cuenta.retirar(300)
    cuenta.retirar(1000)  
    cuenta.retirar(800)
    
    print("\n=== ESTADO FINAL ===")
    print(cuenta)