import fdb
from fdb import services

#con = fdb.connect(host='localhost', database='fit5', user='SYSDBA', password='metalink')
con = services.connect(host='localhost', user='SYSDBA', password='metalink')

bakcupname = 'd:\\Projects\\data\\11.fbk'
con.backup('fit5', bakcupname, metadata_only=False, collect_garbage=False, )
#con.local_backup()

