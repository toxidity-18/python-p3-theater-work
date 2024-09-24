from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Role, Audition

# Create an engine and bind it to the base
engine = create_engine('sqlite:///moringa_theater.db')
Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Add a new role
new_role = Role(character_name="Hamlet")
session.add(new_role)
session.commit()

# Add a new audition
new_audition = Audition(actor="John Doe", location="New York", phone=1234567890, role=new_role)
session.add(new_audition)
session.commit()

# Call back an audition
new_audition.call_back()
session.commit()

# Fetch and display role's actors
actors = new_role.actors()
print(f"Actors auditioning for {new_role.character_name}: {actors}")
