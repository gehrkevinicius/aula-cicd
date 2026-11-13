def calcualr_frete(valor_compra):
  if valor_compra < 0:
    raise ValueError("O valor da compra não pode ser negativo")
  if valor_compra >= 200:
    return 0.00
  return 20.0
