#import pip
#import virtualenv
#import Django
from dataclasses import dataclass
from typing import List
from enum import Enum, auto
from sqlalchemy import Table, Column, ForeignKey, Integer, VARCHAR, UUID, JSONB, MetaData
#sandman2 https://github.com/jeffknupp/sandman2

from ns_database import DatabaseObject

metadata = MetaData()
user_table = Table(
    "user",
    Column("userID", UUID, primary_key=True),
    Column("name", VARCHAR(200), nullable=False),
    Column("email", VARCHAR(200), nullable=False),
    Column("username", VARCHAR(200), nullable=False),
)
#write custom exceptions as classes, then raise them like 
#raise thisIsMyCustomErrorClass(
#    param1=val1,
#    param2=val2,
#    message="you absolute idiot. How could you do this"
#)

# 'ORM' as a broker between the py classes and your SQL definitions

#POST to mySql instance
## need a model per sql table for django

class Role (Enum):
    """Employee roles, reference like Role.USER"""
    USER = auto()
    ADMIN = auto()

@dataclass
class user(DatabaseObject):
    #https://narrativescience.com/resource/blog/journey-to-database-linked-dataclasses
    table = user_table
    primary_key = table.id
    #

    email: str
    role: Role

    def do_the_thing( self, var1, var2: bool) -> None:
        """"heyyyy this does the thing"""
        """ print(f"Heyy this is a string referencing {self.email}")  """
        """ with open(filename) as f """
        """ f.write("hello!\n") """
        """ x ^ p ## ^ is bitwise xor not power"""
        """ Default mutable arguments: never def l = [] """
        """ def a(l=None) """
        """ if l is None: 
                l = []         """
        """ dictionary, list, set and generator comprehensions """ 
        """ most of the time, case checking with == is BAD  """
        """ in most cases you should be able to replace a subclass with its parent Liskov substitution violation """
        """ use isistance check """
        """ Don't use == to check is True, None or False """
        """ use x is None """
        """ if bool or if len checks usually equivalent to if x: pass"""
        """ range(len(a)) <- bad """
        """ enumerate if you actually need the index, otherwise """
        """ a = [1,2,3] """
        """ for v in a: ... """
        """ instead of using [i] to coordinate between objects use zip """
        """ enumerate () """
        """ not using dictionary items """
        """ for key, val in d.items(): """
        """ not using tuple unpacking """
        """ time.perf_counter() """
        """ pep8 - naming convention """

@dataclass
class start: 


    def __init__(self) -> None:
        self.users: List[user] = []

def main() -> None:
    """Main Function"""
    """instantiate classes"""
    """run some other methods idk"""    

if __name__ == "__main__":
    main()