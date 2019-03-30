# import library socket karena akan menggunakan IPC socket
import socket

# definisikan alamat IP binding  yang akan digunakan 
HOST = '127.0.0.1' 

# definisikan port number binding  yang akan digunakan 
PORT = 65432 

# definisikan ukuran buffer untuk mengirimkan pesan
buffer = 7

# buat socket bertipe TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

# lakukan bind
	s.bind((HOST, PORT))

# server akan listen menunggu hingga ada koneksi dari client
	s.listen(buffer)

# lakukan loop forever
	while True:
		# menerima koneksi
	    conn, addr = s.accept()
		
		# menampilkan koneksi berupa IP dan port client yang terhubung menggunakan print
	    print('Connected by', addr)

		# menerima data berdasarkan ukuran buffer
	    from_client = ''
		
		# menampilkan pesan yang diterima oleh server menggunakan print
	    while True:
	        data = conn.recv(4096)
	        if not data: break
	        from_client += data
	        print(from_client)
		
		# mengirim kembali data yang diterima dari client kepada client
	    conn.send("I am SERVER\n")

# tutup koneksi	
	conn.close()
