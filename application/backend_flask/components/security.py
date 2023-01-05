import argon2
from os import environ
from components.config import SecurityConfig as scfg, AuthConfig as acfg


passwordhasher = argon2.PasswordHasher(time_cost=scfg.ARGON_TIMECOST, 
                                       hash_len=scfg.ARGON_HASHLEN, 
                                       salt_len=scfg.ARGON_SALTLEN, 
                                       type=scfg.ARGON_TYPE)

def make_hash(psw):
   SALT = environ.get('HASHSALT')
   psw += SALT
   hash = passwordhasher.hash(psw)
   return hash.encode('utf-8')


def check_hash(old_hash, psw):
   SALT = environ.get('HASHSALT')
   psw += SALT
   try:
      passwordhasher.verify(old_hash, psw)
      if (passwordhasher.check_needs_rehash(old_hash)): 
         return [True, True]  # correct pass, need rehash
      else: 
         return [True, False] # correct pass, don't need rehash
   except:
      return [False] # incorrect pass