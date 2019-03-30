# import library socket karena akan menggunakan IPC socket
import socket

# definisikan tujuan IP server
HOST = '127.0.0.1'

# definisikan port dari server yang akan terhubung
PORT = 65432 

# definisikan ukuran buffer untuk mengirimkan pesan
buffer = 7

# definisikan pesan yang akan disampaikan
pesan = "received pesan"

# buat socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan koneksi ke server dengan parameter IP dan Port yang telah didefinisikan
s.connect((HOST, PORT))

# kirim pesan ke server
s.send("I am CLIENT\n")

# terima pesan dari server
from_server = s.recv(4096)

# tampilkan pesan/reply dari server
print from_server

# tutup koneksi
s.close()

