import os
import platform

def get_user():
  try:
      user = os.getlogin()
  except:
      user = 'UnknownUser'
  return user

def get_hostname():
  return platform.node()
