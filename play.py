from getpass import getpass
import telnetlib

HOST = "localhost"
PORT = 4212

tn = telnetlib.Telnet(HOST, PORT, 5)
print tn.read_until("\n")
print tn.read_until("Password: ")
print "promptet for password - getting pass"
password = getpass()
print password
tn.write(password.encode("utf-8"))
tn.write("\n".encode("utf-8"))

tn.write("add Video1.WMV\n".encode("utf-8"))
