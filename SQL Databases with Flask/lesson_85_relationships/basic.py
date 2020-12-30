# BASIC.py
# CREATE ENTRIES INTO THE TABLES

from models import db, Puppy, Owner, Toy

# Creating 3 puppies
beka = Puppy('Beka')
beethoven = Puppy('Beethoven')
neal = Puppy('Neal')

# Add puppies to db
db.session.add_all([beka, neal, beethoven])
db.session.commit()

# Check!
print(Puppy.query.all())

beethoven = Puppy.query.filter_by(name='Beethoven').all()[0]

# Create Owner Object
marcela = Owner('Marcela', beethoven.id)

# Give Beethoven some toys
toy1 = Toy('Chew Toy', beethoven.id)
toy2 = Toy('Ball', beethoven.id)

db.session.add_all([marcela, toy1, toy2])
db.session.commit()

# Grab Beethoven after those additions
beethoven = Puppy.query.filter_by(name='Beethoven').first()
print(beethoven)

print(beethoven.report_toys())