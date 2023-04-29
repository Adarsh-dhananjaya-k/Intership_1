import sys
#import lcd
import time

def read_code():
    valid_code = True
    c=[]
    length_meas = 0
    length_barcode = int(10) #input("Enter barcode Length: "))
    print("SCAN THE BARCODE")
    time.sleep(2)
    #lcd.lcd_putdata("SCAN THE BARCODE")
    #lcd.sleep(2)
    while True:
        temp_data = sys.stdin.read(1)
        
        if temp_data == "\n":
            if valid_code== True:
                print("VALID BARCODE")
                #lcd.lcd_putdata("VALID BARCODE")
                if abs((length_meas - length_barcode)) <2:
                    #print("LENGTH MATCH: M-",length_meas,"  E-",length_barcode)
                    #print(c)
                    return(c)
                else:
                    print("LENGTH INVALID")
                    #lcd.lcd_putdata("BARCODE ERROR")
                    #lcd.sleep(2)
                    time.sleep(2)
                    return(0x49)
                    
            else:
                print("INVALID BARCODE")
                #lcd.lcd_putdata("BARCODE ERROR")
                #lcd.sleep(2)
                time.sleep(2)
                return(0x49)
                
        if temp_data.isalnum():
            length_meas = length_meas+1
            c.append(temp_data)
        else:
            valid_code = False
            print("Invalid Variable : ", temp_data)
            #lcd.lcd_putdata("BARCODE ERROR")
            #lcd.sleep(2)
            time.sleep(2)
    
            
#read_code()  
        
