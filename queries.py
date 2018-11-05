from models import *
from sqlalchemy import *

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()


def return_gwyneth_paltrows_roles():
    gwyneth_paltrow = session.query(Actor).filter(Actor.name == "Gwyneth Paltrow").first()
    return gwyneth_paltrow.roles
def return_tom_hanks_2nd_role():
    tom_hanks = session.query(Actor).filter(Actor.name == "Tom Hanks").first()
    return tom_hanks.roles[1]
