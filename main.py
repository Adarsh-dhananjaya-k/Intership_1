#import lcd
import barcode_scan
import txt_upload
from datetime import datetime
import time
import serial_com
import colorama
from colorama import Fore,Style, Back
from os import system,name
#Different Bytes for JIG - ROUV
START_B = b'5'
ACK_B ='A'
PUSHB_B ='b'
PASS_B = '!'
FAIL_B = '@'

#------Local Variables---------

inval_barcode =0x49
while True:
    upload_list =[]
    ret_data=[]
    #--------------------Read Barcode-------------------
    #lcd.lcd.clear()
    #print("\n")
    
    barcode_num = barcode_scan.read_code()

    if barcode_num == inval_barcode: #Check Invalid Barcode
        #lcd.lcd_putdata("Invalid Barcode")
        print("Invalid Barcode")
    else:
        barcode_num =''.join(barcode_num)
        barcode_num=str([barcode_num])
        #lcd.lcd.clear()
        #lcd.lcd_putdata("    BARCODE\n"+barcode_num)
        print("Barcode:",barcode_num)
        _ = system('clear')
        now = datetime.now()
        today = now.strftime("%d/%m/%Y")
        current_time = now.strftime("%H:%M:%S")

        #Send "Start Byte = '5'
        serial_com.ser_write(START_B)

        #Wait for ACK_B from JIG
        ack_flag = False
        while not ack_flag:
            #print("ACK Not Recieved")
            ack_byte = serial_com.ser_read()
            #print(ack_byte)
            
            if ack_byte == ACK_B:
                print("ACK Recieved")
                ack_flag = True
        
        if ack_flag:   
            #Append Barcode, Date, Time to Upload List
            upload_list.append(barcode_num)
            upload_list.append(str(today))
            upload_list.append(str(current_time))
            
            
            #print("UP LIST",upload_list)
            #Get the Data from Serial Port
            ret_data = serial_com.load_data() # Get the data from JIG
            for i in range(0,len(ret_data)):
                upload_list.append(str(ret_data[i]))
            #print("Final PACKET",upload_list)

            
            #lcd.sleep(2)
            
            # Upload to Local File
            try:
                txt_upload.local_upload(upload_list)
            except:
                txt_upload.local_uploadtxt(upload_list)
            
            #lcd.lcd_putdata("DONE DONE")
            #lcd.sleep(1)
            len_list = len(upload_list)
            if upload_list[len_list-1] == PASS_B:
                print(Back.GREEN+" ====   ====    ====    ====   ")
                print(Back.GREEN+"||   | ||   || ((      ((     ")
                print(Back.GREEN+" ====   ====    ====    ==== ")
                print(Back.GREEN+"||     ||   ||  ___))   ___))")
            else:
                if upload_list[len_list-1]== FAIL_B:
                    print(Back.LIGHTRED_EX+" ===    ===     ||   ||   ")
                    print(Back.LIGHTRED_EX+"||     ||  ||   ||   ||   ")
                    print(Back.LIGHTRED_EX+" ===    ===     ||   ||   ")
                    print(Back.LIGHTRED_EX+"||     ||  ||   ||   ||___")
                else:
                    print(Fore.RED+"RESULT ERROR - RESCAN")
            print(Style.RESET_ALL)       
            #time.sleep(1)
                
        else:
            #lcd.lcd_putdata("ACK IMPROPER\n"+"RE-SCAN")
            #lcd.sleep(1)
            print("ACK IMPROPER RE-SCAN")
            #time.sleep(1)
            
            

