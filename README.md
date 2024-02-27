import os
os.system("cls")
f = open('back.txt', 'w')
def main():
        
    while True:
        ism = input("ismingizni kiriting: ")
        if str(ism):
            f.write(f'\nIsm: {ism}')
            break
        else:
            print("\nKiritilgan ma'lumo str tayipida bo'lishi kerak !!!")
            continue   
        
        
    while True:
        fam = input("Familyangizni kiritng kiriting: ")
        if str(fam):
            f.write(f'\nFamiliya: {fam}')
            break
        else:
            print("\nFamiliyangizda faqat hariflar ishtirog etishi kerak !!!")
            continue     
    
    
    while True:
        tel_raqam = input("Tel raqamingizni kiriting: ")
        if tel_raqam.startswith('+'):
            f.write(f'\nTel: {tel_raqam}')
            break
        else:
            print("\nTel raqamingiz + belgisi bilan boshlanishi kerak!")
            continue
      
    while True:
        gmail = input("email po'chtangizni kiriting:  ")
        if gmail.endswith('@gmail.com'):
            f.write(f'\nEmail pochta: {gmail}')
            break
        else:
            print("\nemail poschtangizni oxri @gmail.com bilan tugashi kerak !")
            continue   
    
    
    while True:
        pacword = input("parol yarating:  ")
        if int(pacword):
             f.write(f'\nparol: {gmail}')
             break     
        else:
            print('Faqat Raqamlar qatnashishi kerak !')     
         


if __name__ == "__main__":
    main()
f.close()
print("\n\nMa'lumotlar muovfaqiyatli saqlandi")
