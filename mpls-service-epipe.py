with open("epipe_create.txt", "w") as f:
    for service_id in range(1001, 3001):
        # Start with an empty string for each service ID
        output = f"configure service epipe {service_id} customer 1 create\n"
        output += f"sap 2/x1/1/c2/1:{service_id}.{service_id} create\n"
        output += "ingress qos 30\n"
        output += "egress qos 30\n"
        output += "exit\n"
        output += f"spoke-sdp 101:{service_id} create\n"
        output += "exit\n"
        output += "no shutdown\n"
        output += "exit all\n"

        # Write the accumulated output to the file
        f.write(output)
