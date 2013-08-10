#use your own email address
email = 'irsnooze@hotmail.com'

#include the Dwolla REST Client
from dwolla import DwollaUser

#Instantiate a new Dwolla User Client
# And, Seed a previously generated access token
#you need to authenticate into your account using an OAuth token and a 4-digit PIN
Dwolla = DwollaUser('OAUTH_TOKEN')

transaction = Dwolla.send_funds(0.01, email, 'PIN', dest_type = 'Email')
print('Transaction ID: %s' % transaction)
