

database = []
class user :
    def __init__(self, username, password) :
        self.__username = username
        self.__password = password
        database.append(self)

    def get_username(self) :
        return self.__username

    def get_password(self) :
        return self.__password

user1 = user("admin", "admin")
user2 = user("Dono", "213456")
user3 = user("Putin", "rudal123")

def login(username, password) :
    if username == "" and password == "":
        return "Username dan Password tidak boleh kosong"
    else :
        found = None
        for user in database :
            if user.get_username() == username and user.get_password() == password : 
                found =user.get_username()

        if found is not None:
            print("login berhasil")
            return 1
        else :
            print("login gagal")
            return "login tidak berhasil, Username atau Password salah"




