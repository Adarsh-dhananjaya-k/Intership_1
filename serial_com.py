import serial
#import lcd
try:
    ser = serial.Serial('/dev/ttyUSB0',9600)
except:
    print("----------USB ERROR-------------")
    print("----------USB ERROR-------------")
    print("----------USB ERROR-------------")

DATA_SB = '$'
END_B = '#'
PASS_B = '!'
FAIL_B = '@'


end_flag = False



def ser_read():
    c = ser.read().decode('ascii')
    #print(c)
    return(c)
    
def ser_write(sb):
    ser.write(sb)
    
def load_data():
    packet_data = []
    end_flag = False
    testr_flag = False
    temp_byte = ''
    temp =''
    str_data =''
    
    
    while not testr_flag:
        temp = ser.read().decode('ascii')
        #print("Inside TEST")
        if temp == DATA_SB:
            #print("Inside DATA_SB")
            #print("START BYTE:",temp)
            while not end_flag:
                #print("Inside Start Read")
                temp = ser.read().decode('ascii')
                #print("IN LOOP:",temp)
                if temp == END_B:
                    #print("END FLAG")
                    end_flag = True
                    #print("END BYTE",temp)
                else:
                    temp_byte = temp_byte+str(temp) 
                    
                    
            packet_data.append(temp_byte)
            #print(packet_data)
            temp_byte = ''
            temp =''
            end_flag = False
            #temp = ser.read().decode('ascii')
        else:
            if temp == PASS_B:
                #print("Inside OASS B")
                packet_data.append(temp)
                testr_flag = True
                #lcd.lcd_putdata("      PASS")
                print("TEST RESULT: PASS")
                return(packet_data)
            else:
                if temp == FAIL_B:
                    #print("InsideFAIL B")
                    packet_data.append(temp)
                    testr_flag = True
                    #lcd.lcd_putdata("     FAIL")
                    print("TEST RESULT: FAIL")
                    return(packet_data)
                else:
                    if temp == "\n":
                        if str_data != '':
                            #print(str_data)
                            #lcd.lcd_putdata(str_data)
                            print(str_data)
                            #print("\n")
                            str_data =''
                            temp = ser.read().decode('ascii')
                    else:
                        str_data = str_data +str(temp)
                        #temp = ser.read().decode('ascii')
                        #print("TEMP",temp)
                    
                    
                    
                
            
            
            
                
    
            
            
    
        
                
    #return(packet_data)
            
             
