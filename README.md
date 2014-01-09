	from Authenticate import Authenticate, CreateUser
	if __name__ == '__main__':
		# you may create users in the password file as such
		#cu = CreateUser("passwd.txt")
		#cu.write("test", "test")
		#cu.close()

		auth = Authenticate("passwd.txt")
		password = raw_input()
		print  auth.is_valid_user("test", password)

