import sys,time
usname,passwd,encrypted,decrypted,sessionStatus,key,mode,login=[],[],[],[],False,0,False,False
fakename,fakepwd,keypass=[],[],[]
register = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
            '8', '9']

#############################################################################################################
# Service Codes here...

def SignUp():
    global usname,mode,passwd,encrypted,key
    if not mode:
        print('Hello User, Please Create a new Account!')
        usname.append(input('Please enter your name: '))
        passwd.append(input('Please enter your password (4 characters only): '))
        key=int(input('Enter a Encryption Key: '))
        encrypted=encryption(passwd[-1],key)
        print("Encrypted Password:",encrypted)
        mode=True
        print('Account created successsfully!\n')
    if mode:
        print(f'Welcome {usname}, Please Login to your existing account!')
        mdata=[]
        mdata.append(input('Please enter your User Name in the registered account: '))
        if mdata == usname:
            ndata=[]
            ndata.append(input('Please enter your "Encryption Key" for Login: '))
            Login(ndata)
        else:
            print(f'Account with User Name {mdata} not found in Service Database!')

def Login(ticket):
    global usname,passwd,mode,key
    if mode:
        chsk=decryption(ticket[-1],key)
        if chsk==passwd[-1]:
            print('\n==============================================================')
            print(f'{usname} has successfully logged in!')
            print(f'All CONFIDENTIAL DATA of {usname} here!')
            print('==============================================================\n')
            return True
        else:
            print('Login Failed! Try Again!')
            return False
        
def encryption(text,key): 
    encrypt=''
    for i in text:
        encrypt+=register[(register.index(i)-key)%len(register)]
    return encrypt

def decryption(text,key):
    decrypt=''
    for i in text:
        decrypt+=register[(register.index(i)+key)%len(register)]
    return decrypt

#############################################################################################################


#############################################################################################################
#Hacker's Codes here...

def Brute_Force(register,mode):
    i=0
    start=time.time()
    for a in register:
        for b in register:
            for c in register:
                for d in register:
                    i=i+1
                    key=a+b+c+d
                    passcode=[]
                    passcode.append(key)
                    print('>>',key)
                    status=Login(passcode)
                    if not status:
                        continue
                    else:
                        print('The Encrypted Key is:',key)
                        print("Successful after",i,"trials!")
                        stop=time.time()
                        print('Time Taken:',stop-start,'seconds!')
                        sys.exit()

def hackAccess():
    global mode,register,usname
    mode=True
    name=[]
    name.append(input('Enter User Name to Login: '))
    if usname==name:
        print("Starting BRUTE FORCE Attack!!!")
        Brute_Force(register,mode)
    else:
        print(f'Account with User Name {name} not found in Service Database!')
    
#############################################################################################################


#############################################################################################################
#Supporting Codes here...
    
def StartService():
    while(True):
        enter=int(input('Type 0 to let "User" into the service.\nType 1 to let "Hacker" into the service.\nEnter your choice:'))
        if enter==0:
            print('\nUser Session starts...')
            time.sleep(1)
            userData()
            print('\nWarning! You will be automatically Logged Out in 10 seconds!')
            time.sleep(10)
            sys.stdout.write('\033[H\033[J')
            sys.stdout.flush()
        if enter==1:
            print('\nHacker Session starts...Alert! Hacker is trying to attack and gain Password!')
            time.sleep(1)
            hackAccess()

def userData():
    global mode
    mode=False
    SignUp()

StartService()

#############################################################################################################