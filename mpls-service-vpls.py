with open("vpls_create.txt", "w") as f:
    for service_id in range(1001, 1011):
        # Start with an empty string for each service ID
        output = f"configure service vpls {service_id} customer 1 create\n"
        
        for vlan_x in range(1001, 1011):
            output += f"sap 2/x1/1/c2/1:{service_id}.{vlan_x} create\n"
            output += "ingress qos 30\n"
            output += "egress qos 30\n"
            output += "exit\n"
        output += f"spoke-sdp 101:{service_id} create\n"
        output += "exit\n"
        output += "no shutdown\n"
        output += "exit all\n"

        # Write the accumulated output to the file
        f.write(output)
