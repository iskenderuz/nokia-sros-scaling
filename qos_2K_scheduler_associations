service_id_range = range(1001, 3001)
vlan1_start = 1001
vlan1_end = 2001
vlan2_start = 1
vlan2_end = 16
vlan3_start = 2001
vlan3_end = 3001
vlan4_start = 1
vlan4_end = 16


total_vlan2_values = vlan2_end - vlan2_start + 1
total_vlan4_values = vlan4_end - vlan4_start + 1

with open("scheduler_local_all.txt", "w") as f:

    output = f"configure qos\n"
    for i in range(1001, 3001):
            output += f"scheduler-policy sched-{i} create\n"
            output += f"tier 1\n"
            output += f"scheduler top create\n"
            output += f"rate 10000\n"
            output += f"exit\n"
            output += f"exit\n"
            output += f"exit \n"

    output += f"exit all \n"
    output += f"configure qos sap-egress 101 create\n"
    output += f"exit all \n"
    output += f"configure service sdp 101 mpls create\n"
    output += f"far-end 10.245.151.132\n"
    output += f"exit all \n"

    for index, service_id in enumerate(service_id_range):
        # Calculate vlan1 and vlan2 based on the current index
        vlan1 = vlan1_start + (index // total_vlan2_values)
        vlan2 = vlan2_start + (index % total_vlan2_values)
        vlan3 = vlan3_start + (index // total_vlan4_values)
        vlan4 = vlan4_start + (index % total_vlan4_values)

        # Stop if vlan1 exceeds the desired end value
        if vlan1 > vlan1_end:
            break

        output += f"configure service epipe {service_id} customer 1 create\n"
        output += f"sap 2/x1/1/c2/1:{vlan1}.{vlan2} create\n"
        output += f"egress qos 101\n"
        output += f"egress scheduler-policy sched-{service_id}\n"
        output += f"exit\n"
        output += f"sap 2/x1/1/c2/1:{vlan3}.{vlan4} create\n"
        output += f"exit\n"
        output += f"no shutdown\n"
        output += f"exit all\n"

    output += "exit all\n"

    f.write(output)

