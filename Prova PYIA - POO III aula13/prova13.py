class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        self._saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor

    def exibir_saldo(self):
        print(f"Saldo de {self._titular}: R$ {self._saldo:.2f}")

conta = ContaBancaria("João", 1000)
conta.exibir_saldo()
conta.depositar(500)
conta.exibir_saldo()
conta.sacar(300)
conta.exibir_saldo()
conta.sacar(1500)
conta.exibir_saldo()
