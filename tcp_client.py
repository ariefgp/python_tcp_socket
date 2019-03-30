# import library socket karena akan menggunakan IPC socket
import socket

# definisikan tujuan IP server
HOST = '127.0.0.1' 

# definisikan port dari server yang akan terhubung
PORT = 65432 

# definisikan ukuran buffer untuk mengirimkan pesan
buffer = 7

# definisikan pesan yang akan disampaikan
pesan = "Contoh Pesan"

# buat socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

# lakukan koneksi ke server dengan parameter IP dan Port yang telah didefinisikan
	s.bind((HOST, PORT))
	s.listen(buffer)

# kirim pesan ke server
	conn, addr = s.accept()
    with conn:

# terima pesan dari server
		print('Connected by', addr)

# tampilkan pesan/reply dari server
		while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

# tutup koneksi
	conn.close()
    print 'client disconnected'
