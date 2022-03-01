from django import template

register = template.Library()

@register.filter()
def in_purchase(purchases, id):
    return purchases.filter(order_id=id)