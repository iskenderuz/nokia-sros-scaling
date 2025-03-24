with open("vprn_create.txt", "w") as f:
    for service_id in range(100, 200):
        # Start with an empty string for each service ID
        output = f"configure service vprn {service_id} customer 1 create\n"
        
        for vlan_x in range(1, 10):
            output += f"interface int_{service_id}{vlan_x} create\n"
            output += f"address 10.{service_id}.{vlan_x}.1/30\n"
            output += f"sap 1/1/c2/1:{service_id}{vlan_x} create\n"
            output += "ingress qos 30\n"
            output += "egress qos 30\n"
            output += "exit\n"
            output += "exit\n"
        
        output += "auto-bind-tunnel resolution any\n"
        output += f"route-distinguisher {service_id}:{service_id}\n"
        output += f"vrf-target target:{service_id}{service_id}\n"
        output += "no shutdown\n"
        
        output += "exit all\n"
        
        # Write the accumulated output to the file
        f.write(output)
