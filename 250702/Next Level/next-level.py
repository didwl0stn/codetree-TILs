user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class user:
    def __init__(self,uid="codetree",ulv=10):
        self.id=uid
        self.level=ulv

user1 = user()
user2 = user(user2_id,user2_level)

print(f"user {user1.id} lv {user1.level}\nuser {user2.id} lv {user2.level}")