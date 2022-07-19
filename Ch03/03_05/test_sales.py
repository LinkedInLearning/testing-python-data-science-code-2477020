from hypothesis import given
from hypothesis.strategies import composite, from_regex, integers, lists
from sales import Sale, sku_sales


@composite
def sales(draw):
    sku = draw(from_regex(r'[A-F0-9]{8}', fullmatch=True))
    amout = draw(integers(min_value=1, max_value=10_000))
    return Sale(sku, amout)


@given(lists(elements=sales()))
def test_sku_sales(sales):
    by_sku = sku_sales(sales)
    unknown = set(by_sku) - set(sale.sku for sale in sales)
    assert not unknown