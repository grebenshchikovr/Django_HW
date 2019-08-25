from django import template
register = template.Library()

@register.filter
def basket_total_quantity(basket):
    # "return total quantity for user"
    return sum(list(map(lambda basket_slot: basket_slot.quantity, basket)))

@register.filter
def basket_total_cost(basket):
    # "return total cost for user"
    return sum(list(map(lambda basket_slot: basket_slot.product_cost, basket)))
