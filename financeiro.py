def calcular_saldo(transacoes):
    saldo = 0
    for transacao in transacoes:
        if transacao["tipo"] == "receita":
            saldo += transacao["valor"]
        else:
            saldo -= transacao["valor"]

    return saldo