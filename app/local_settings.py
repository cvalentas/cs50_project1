import os

# *****************************
# Environment specific settings
# *****************************

# DO NOT use "DEBUG = True" in production environments
DEBUG = True

# DO NOT use Unsecure Secrets in production environments
# Generate a safe one with:
#     python -c "import os; print repr(os.urandom(24));"
SECRET_KEY = 'This is an UNSECURE Secret. CHANGE THIS for production environments.'

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'postgres://gudadzvdlavsry:b9da08b0b491acd85e544a7dadecd60aa4ceba6827a1f337a04256dc2c3caac3@ec2-54-83-197-230.compute-1.amazonaws.com:5432/dflif9ikh0ildt'
SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids a SQLAlchemy Warning

# Flask-Mail settings
# For smtp.gmail.com to work, you MUST set "Allow less secure apps" to ON in Google Accounts.
# Change it in https://myaccount.google.com/security#connectedapps (near the bottom).
MAIL_SERVER = 'mail.valentas.com'
MAIL_PORT = 587
MAIL_USE_SSL = False
MAIL_USE_TLS = True
MAIL_USERNAME = 'verify@valentas.com'
MAIL_PASSWORD = 'fHF&;#]4$rli3s+O'

# Sendgrid settings
SENDGRID_API_KEY='place-your-sendgrid-api-key-here'

# Flask-User settings
USER_APP_NAME = 'Valentas: CS50_Project1'
USER_EMAIL_SENDER_NAME = 'CS50 Project1'
USER_EMAIL_SENDER_EMAIL = 'verify@valentas.com'

ADMINS = [
    '"Admin One" <admin1@gmail.com>',
    ]
