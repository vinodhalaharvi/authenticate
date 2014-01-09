# Copyright (c) 2013, RTP Network Services, Inc.
# All Rights Reserved      (904-236-6993)
# Vinod Halaharvi / vinod.halaharvi@rtpnet.net, vinod.halaharvi@gmail.com
# 
# http://www.rtpnet.net / codesupport@rtpnet.net
#
# There is NO warranty for this software.  If this software is used by
# someone else and passed on, the recipients should know that what they
# have is not the original, so that any problems introduced by others will
# not reflect on the original authors' reputations. This is *not* authorization
# to copy or distribute this software to others!

import sys
import hashlib

class CreateUser(object):
	"""docstring for """
	def __init__(self, filename):
		self.file = open(filename, 'a')

	def _make_pw_hash(self, user, password):
		"""docstring for _make_pw_hash"""
		return user, hashlib.md5(user + password).hexdigest()

	def write(self, user, password):
		"""docstring for write"""
		user, _hash = self._make_pw_hash(user, password)
		self.file.write("%s:%s\n" %(user, _hash))

	def close(self):
		"""docstring for close"""
		self.file.close()
		

class Authenticate(object):
	"""docstring for Authenticate"""
	def __init__(self, filename):
		self.filename = filename
		self.passfile = list(open(filename).readlines())

	def _make_pw_hash(self, user, password):
		"""docstring for _make_pw_hash"""
		return user, hashlib.md5(user + password).hexdigest()

	def is_valid_user(self, user, password):
		"""docstring for checkpassword"""
		user, _hash = self._make_pw_hash(user, password)
		for entry in self.passfile:
			user, phash = entry.strip().split(":", 1)
			if user == user and _hash == phash:
				return True
		return False


if __name__ == '__main__':
	assert len(sys.argv) > 1, "Hash Password file  is needed"
	if sys.argv[1] == "-h":
		print "Usage:\npython scriptname.py  passwdfile"
		print "Example:\npython passwordTest.py  passwd.txt user"
		print
		exit(0)

	passfilename, user = sys.argv[1:]
	#cu = CreateUser(passfilename)
	#cu.write("test", "test")
	#cu.close()
	auth = Authenticate(passfilename)
	password = raw_input()
	print  auth.is_valid_user("test", password)
