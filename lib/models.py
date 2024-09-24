from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Define custom naming convention for foreign keys
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

# Create a declarative base class with the custom metadata
Base = declarative_base(metadata=metadata)

# Define the Role model
class Role(Base):
    __tablename__ = 'roles'
    
    id = Column(Integer, primary_key=True)
    character_name = Column(String, nullable=False)

    # Relationship to the Audition model
    auditions = relationship('Audition', back_populates='role')

    # Methods for role
    def actors(self):
        return [audition.actor for audition in self.auditions]

    def locations(self):
        return [audition.location for audition in self.auditions]

    def lead(self):
        lead_audition = next((audition for audition in self.auditions if audition.hired), None)
        return lead_audition if lead_audition else 'no actor has been hired for this role'

    def understudy(self):
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        return hired_auditions[1] if len(hired_auditions) > 1 else 'no actor has been hired for understudy for this role'


# Define the Audition model
class Audition(Base):
    __tablename__ = 'auditions'
    
    id = Column(Integer, primary_key=True)
    actor = Column(String, nullable=False)
    location = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    
    # Relationship to the Role model
    role = relationship('Role', back_populates='auditions')

    # Method to hire an actor
    def call_back(self):
        self.hired = True
