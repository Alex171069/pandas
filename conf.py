from bestconfig import Config

config = Config("App.ini")
Ppin = config['Path']['pin']
print(Ppin)
setPath = '/home/NSO.LOC/bobav/share/Диск H/112/_Служба-112/_COVID/'
config.set('pin', setPath)
config.insert('App.ini')