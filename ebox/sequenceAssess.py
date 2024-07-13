set1 = set(map(int, input().split(',')))
set2 = set(map(int, input().split(',')))

# print(set1)
# print(set2)

print(set1.issubset(set2))
print(set2.issubset(set1))
print(set1.issuperset(set2))
print(set2.issuperset(set1))


########################

# Initialize an empty dictionary to store client details
clients = {}

# Read the number of clients
num_clients = int(input("Enter the number of clients\n"))

# Collect details for each client
for i in range(1, num_clients + 1):
    print(f"Enter the details of the client {i}")
    name = input().strip()
    email = input().strip()
    passport_number = input().strip()
    
    # Store client details in the dictionary with passport number as the key
    clients[passport_number] = f"{name}--{email}--{passport_number}"

# Read the passport number to be searched
search_passport_number = input("Enter the passport number of the client to be searched\n").strip()

# Retrieve and print client details if found, else print "Client not found"
if search_passport_number in clients:
    print("Client Details")
    print(clients[search_passport_number])
else:
    print("Client not found")