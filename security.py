from hmac import compare_digest
from user import User

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    print("Authenticate, ",username, ", ",password)
    user = username_table.get(username, None)
    if user and compare_digest(user.password, password):
        return user

def identity(payload):
    print("Identity", payload)
    user_id = payload['identity']
    return userid_table.get(user_id, None)

# if __name__ == "__main__":
#     print(username_table)
#     ut = {}
#     for u in users:
#       ut[u.username] = u
#     print(ut)