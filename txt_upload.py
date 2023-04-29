from csv import writer

u_list=[]
def local_uploadtxt(u_list): 
    with open('/home/pi/Desktop/IPCB_ROUV/IPCB_Data.txt','a') as f:
        f.write(u_list)
        f.write("\n")
        
def local_upload(u_list):
    with open('/home/pi/Desktop/IPCB_ROUV/IPCB_Data.csv','a') as f_csv:
        writer_obj = writer(f_csv)
        writer_obj.writerow(u_list)
    
