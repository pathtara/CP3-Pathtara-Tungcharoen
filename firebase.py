import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('fir-test001-c68d7-firebase-adminsdk-941fb-ccc50a1f29.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://fir-test001-c68d7.firebaseio.com/'
})
ref = db.reference('')
users_ref = ref.child('Users')
users_ref.push({
    'alanisawesome1': {
        'date_of_birth': 'June 23, 1912',
        'full_name': 'Alan Turing'
    },
    'gracehop1': {
        'date_of_birth': 'December 9, 1906',
        'full_name': 'Grace Hopper'
    }
})


# As an admin, the app has access to read and write all data, regradless of Security Rules

print(ref.get())