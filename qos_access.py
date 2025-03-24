with open("access_qos_10K", "w") as f:
    output = f"configure qos\n"
    for i in range(10001, 20001):
        output += f"sap-ingress {i} create\n"
        output += f"queue 1 create\n"
        output += f"exit\n"
        output += f"exit\n"
    output += f"exit all\n"

    output += f"configure qos\n"
    for i in range(10001, 20001):
        output += f"sap-egress {i} create\n"
        output += f"queue 1 create\n"
        output += f"exit\n"
        output += f"exit\n"
    output += f"exit all\n"

        # Write the accumulated output to the file
    f.write(output)
