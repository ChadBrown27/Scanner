import socket
import sys

#Checks if a command-line argument was provided
if len(sys.argv) == 2:
    #if yes that is the target
    target = socket.gethostbyname(sys.argv[1]) #translates the host name to IPv4
else:
    print("Invalid amount of arguments")
    print("Syntax: python3 scanner.py <ip_address_or_hostname>")
    sys.exit()

#Scanning logic
print("-" * 50)
print(f"Scanning Target {target}")
print("-" * 50)

try:
    #Scans ports 1 through 50
    for port in range (1,101):
        #Create the socket object for each connection attempt
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5) #A half second timeout window for better scanning

        #Try to connect and store the result
        result = s.connect_ex((target,port))

        #If the port is open, the result is 0
        if result == 0:
            #Try to receive a small amount of data (the banner)
            try:
                #1024 is the buffer size - how much data to receive at once
                banner = s.recv(1024).decode('utf-8').strip()
                print(f"Port {port}: OPEN | Banner: {banner}")
            except:
                #if we cant get a banner, just say it's open
                print(f"Port {port}: OPEN")

        #close the connection
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror:
    print("Hostname count not be resolved. Exiting.")
    sys.exit()
except socket.error:
    print("Couldn't connect to server. Exiting")
    sys.exit()

print ("-" * 50)
print ("Scan complete.")