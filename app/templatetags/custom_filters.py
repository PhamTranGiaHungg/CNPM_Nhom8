from django import template

register = template.Library()

@register.filter
def format_currency(value):
    """
    Định dạng số thành định dạng tiền tệ có dấu chấm phân tách hàng nghìn.
    Ví dụ: 1500000 -> 1.500.000
    """
    try:
        value = int(value)
    except (ValueError, TypeError):
        return value  # Trả lại nguyên giá trị nếu không phải số

    formatted_value = f"{value:,}".replace(",", ".")
    return f"{formatted_value} đồng"