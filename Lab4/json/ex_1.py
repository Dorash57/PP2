import json

print("Interface status")
print("============================================================================================")
print("DN                                                   Description        Speed     MTU")
print("--------------------------------------------------  -------------      --------  -----")


with open("sample-data.json", "r") as file:
    data=json.load(file)

    
for i in range(len(data)):
    request_from_server = data["imdata"][i]["l1PhysIf"]["attributes"]["dn"]
    speed = data["imdata"][i]["l1PhysIf"]["attributes"]["fecMode"]
    mtu = data["imdata"][i]["l1PhysIf"]["attributes"]["mtu"]
    print(request_from_server, "                            ", speed," ", mtu )
    print(request_from_server, "                            ", speed," ", mtu )
    print(request_from_server, "                            ", speed," ", mtu )