import os
from os.path import abspath, dirname, join


_cwd = dirname(abspath(__file__))

#files directory
FILE_DIRECTORY = os.path.abspath(os.path.join(os.path.split(os.path.abspath(__file__))[0], 'files'))

# Subject of the email sent after purchase 
MAIL_SUBJECT = 'Thanks for your purchase'

# Email address for the 'from' field of the generated email
MAIL_FROM = 'adress@gmail.com'

# Email server address
MAIL_SERVER = 'smtp.gmail.com'

# Email server username
MAIL_USERNAME = 'adress@gmail.com'

# Email server password
MAIL_PASSWORD = '##enter-psw###'

# Email server port
MAIL_PORT = '465'

# Use SSL for email? 
MAIL_USE_SSL = True

# Website address, for use in Stripe purchases and in email
SITE_ADDRESS = 'brokenrecordsband.com'

# Database URI for SQLAlchmey (Default: 'sqlite+pysqlite3:///sqlite3.db')
SQLALCHEMY_DATABASE_URI = 'mysql://#user#:#psw#@127.13.48.2/pi'

# Stripe secret key to be used to process purchases
#STRIPE_SECRET_KEY = 'sk_test_EPuQFdamG8SDE6loD9PVlVOc'
STRIPE_SECRET_KEY = '#str_secret_key#'

# Stripe public key to be used to process purchases
STRIPE_PUBLIC_KEY = '#str_pub_key#'

#FORM CONFIG
WTF_CSRF_ENABLED = True
SECRET_KEY = '#create-a-key#'