from helpers import alphabet_position, rotate_character
def encrypt(mess,enc):
    r=len(mess)
    n=len(enc)
    alpha="abcdefghijklmnopqrstuvwxyz"
    new=""
    enc=enc.lower()
    enc=enc*50
    cnt=0   
    special="!@#$%^&*()<>?':; \/.,1234567890"
    for i in range(0,r):
        if mess[i] in special:         
            new=new+mess[i]      
    
        else :
            new=new+rotate_character(mess[i],alpha.index(enc[cnt]))
            cnt=cnt+1           
    return new  
        
        

def main():
    mess=input("Type a message:")
    enc=input("Encryption key")
    print(encrypt(mess,enc))
if __name__=="__main__":
    main() 

    
        
        
            
