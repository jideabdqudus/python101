class User: #Class Blueprint
    def __init__(self, id, username): #Initializing the CLass
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user): #Methods
        user.followers +=1
        self.following +=1



user_1 = User("001", "Jide") #Objects
user_2 = User("002", "Sameerah")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
