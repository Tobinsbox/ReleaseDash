from MongoDA import DataAccess

_DB = DataAccess.GetDB();

class MachineScript:

    def __init__(self,branch_name,machine_name,ip_address,username,password,script,usage):
        self.Branch_Name=branch_name
        self.Machine_Name=machine_name
        self.Ip_Address=ip_address
        self.User_Name=username
        self.Password=password
        self.Script=script
        self.Usage=usage

    def insert(self):
        print(self.Branch_Name)
        _DB.MachineScript.insert_one({'Branch_Name':self.Branch_Name,
                                 'Machine_Name': self.Machine_Name,
                                 'Ip_Address': self.Ip_Address,
                                 'User_Name': self.User_Name,
                                 'Password': self.Password,
                                 'Script': self.Script,
                                 'Usage': self.Usage});

if __name__ == '__main__':
    test=MachineScript(branch_name='MOD',machine_name='Build',ip_address='localhost',username='root',password='tobin',
                       script='/temp/autobuild.vbs',usage='start build')
    test.insert()

