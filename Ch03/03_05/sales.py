from dataclasses import dataclass


@dataclass
class Sale:
    sku: str
    price: int  # US cents


def sku_sales(sales: list[Sale]):
    by_sku = {}  # sku -> amount
    for sale in sales:
        by_sku[sale.sku] = by_sku.get(sale.sku, 0) + sale.price
    return by_sku
