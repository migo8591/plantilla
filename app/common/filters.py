# from babel.dates import format_date
from babel.dates import format_date

def format_datetime(value, format='short', locale='es'):
    if not value:
        return ''
    if format == 'short':
        return format_date(value, format='short', locale=locale)
    elif format == 'full':
        return format_date(value, format='long', locale=locale)
    return ''

# ayuda de chatGPT utilizando babel.dates:
#     https://chatgpt.com/share/68a6d845-4fb0-800d-9d73-47b11557af80

# def format_datetime(value,format='short', locale='es'):
#     value_str = None
#     if not value:
#         value_str = ''
#     if format == 'short':
#         value_str = value.strftime('%d/%m/%Y')
#     elif format == 'full':
#         value_str = value.strftime('%d de %B de %Y')
#     else:
#         value_str = ''    
#     return value_str