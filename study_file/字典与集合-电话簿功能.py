phone_book = {}

phone_book['yyh'] = 13203605121
phone_book['jy'] = 17732179857
print(phone_book['jy'])

print(phone_book.get('yyh','contace not found'))
print(phone_book.get('alica','contace not found'))

phone_book['jy'] = 19933129280
print(phone_book['jy'])

del phone_book['yyh']
print(phone_book)