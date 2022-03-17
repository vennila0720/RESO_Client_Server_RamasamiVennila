import socket,os

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("", 5005))
k = ' '
size = 1024


fname = input("Enter file name of the image with extentsion (example: filename.jpg,filename.png \n")

#client_socket.send(fname)
#fname = 'images/'+fname

fp = open(fname,'w')
while True:
            strng = client_socket.recv(512)
            if not strng:
                break
            fp.write(strng)
fp.close()
print ("Data Received successfully")
exit()
        #data = 'viewnior '+fname
        #os.system(data)
        
