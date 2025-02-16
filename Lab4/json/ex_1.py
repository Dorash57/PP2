import json


with open("sample-data.json", "r") as file:
    data=json.load(file)
    

print(len(data["imdata"]))
cnt=1


print("Interface status")
print("============================================================================================")
print("DN                                                   Description        Speed     MTU")
print("--------------------------------------------------  -------------      --------  -----")


for i in range(len(data["imdata"])):
    print(cnt)
    request_from_server = data["imdata"][i]["l1PhysIf"]["attributes"]["dn"]
    speed = data["imdata"][i]["l1PhysIf"]["attributes"]["fecMode"]
    mtu = data["imdata"][i]["l1PhysIf"]["attributes"]["mtu"]
    print(request_from_server, "                            ", speed," ", mtu )
    print(request_from_server, "                            ", speed," ", mtu )
    print(request_from_server, "                            ", speed," ", mtu )
    cnt+=1