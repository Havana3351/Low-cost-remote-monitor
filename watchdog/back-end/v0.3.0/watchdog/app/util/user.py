from werkzeug.security import generate_password_hash, check_password_hash

class User() :
    username = 'admin'
    password_hash = 'admin'
    phonenum = ''
    dorm = ''
    room = ''
    campus = ''

    def set_password(self, password):
            self.password_hash = generate_password_hash(password)
            print(self.password_hash)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
