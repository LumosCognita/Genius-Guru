import configparser
import os
##--------------- Config -----------------------------------
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

config = configparser.ConfigParser()
config.read(os.path.join(THIS_FOLDER,'config.example.ini'))