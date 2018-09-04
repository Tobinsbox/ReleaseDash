from MongoDA import DataAccess

_DB = DataAccess.GetDB();

class MachineScript:

    def __init__(self,id,branch_name,machine_name,ip_address,username,password,program,script,usage):
        self.id=id
        self.Branch_Name=branch_name
        self.Machine_Name=machine_name
        self.Ip_Address=ip_address
        self.User_Name=username
        self.Password=password
        self.Script=script
        self.Usage=usage
        self.Program=program

    def insert(self):
        _DB.MachineScript.insert_one({'Branch_Name':self.Branch_Name,
                                 'Machine_Name': self.Machine_Name,
                                 'Ip_Address': self.Ip_Address,
                                 'User_Name': self.User_Name,
                                 'Password': self.Password,
                                 'Script': self.Script,
                                 'Usage': self.Usage,
                                 'Program':self.Program});
    @classmethod
    def returnAllData(self):
        msList=[]
        for i in _DB.MachineScript.find():
            ms=MachineScript(branch_name=i.get('Branch_Name',''),
                     machine_name=i.get('Machine_Name',''),
                     ip_address=i.get('Ip_Address',''),
                     username=i.get('User_Name',''),
                     password=i.get('Password',''),
                     script=i.get('Script',''),
                     usage=i.get('Usage',''),
                     program=i.get('Program',''),
                     id=i.get('_id',''))
            msList.append(ms)
        return msList


if __name__ == '__main__':
    for i in MachineScript.returnAllData():
        print(i)
