from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()

# add and commit the actors and roles below
tom_hanks = Actor(name= 'Tom Hanks')
gwyneth_paltrow = Actor(name= 'Gwyneth Paltrow')
bill_murray = Actor(name = 'Bill Murray')

tom_hanks.roles = [Role(character = "Forrest Gump"), Role(character = "Jim Lovell"),
Role(character = "Woody"), Role(character = "Robert Langdon")]

gwyneth_paltrow.roles = [Role(character = "Pepper Potts"),
Role(character = "Margot Tenenbaum")]

bill_murray.roles = [Role(character = "Phil"), Role(character = "Steve Zissou")]

session.add_all([tom_hanks, gwyneth_paltrow, bill_murray])
session.commit()
