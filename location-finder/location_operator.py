# If you do not have this package, please install it. 
# (write 'pip install phonenumbers' to terminal)
import phonenumbers

# You have to replace it with the number you want to find.
number1 = '+11111111111'

from phonenumbers import geocoder

number = phonenumbers.parse(number1)
print(geocoder.description_for_number(number, 'en'))


from phonenumbers import carrier

number = phonenumbers.parse(number1)
print(carrier.name_for_number(number, 'en'))
