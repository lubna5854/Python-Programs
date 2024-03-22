import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier

phone_number=input("Enter the phone number with countrycode: ")
pn=phonenumbers.parse(phone_number)
tz=timezone.time_zones_for_number(pn)
print("Timezone: ",str(tz))

# Location service
location=geocoder.description_for_number(pn,'en')
print("Location: ",str(location))

# Service provider
sp=carrier.name_for_number(pn,'en')
print("Service Provider:",str(sp))