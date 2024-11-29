# Use pydantic to check data

from pydantic import BaseModel

class User(BaseModel):
  id: int
  name: str
  
user1 = User(id=1, name="Ann")
print(user1)

# un_named_user = User()
# print(un_named_user)

# what are the benefits of using pydantic
# what data types does pydantic support

# user2 = User(id="2.3", name="Joe")
print(user2)