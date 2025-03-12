from config import SessionLocal
from models import Role, Audition

session = SessionLocal()

# create a new role
new_role = Role(character_name="Hamlet")
session.add(new_role)
session.commit()

# create an audition
new_audition = Audition(actor="John Doe", location="New York", phone=1234567890, role_id=new_role.id)
session.add(new_audition)
session.commit()

# query a role and its auditions
role = session.query(Role).filter_by(character_name="Hamlet").first()
print("Actors auditioned:", role.actors())
print("Locations:", role.locations())

# hire an actor
audition = session.query(Audition).first()
audition.call_back()
session.commit()

# check lead role
print("Lead:", role.lead())

session.close()
