with open("sr-te-lsp_16K.txt", "w") as f:
    output = f"configure router mpls\n"
    for i in range(1, 16001):
            output += f"path t3_3-path-{i}\n"
            output += f"hop 1 sid-label 20033\n"
            output += f"no shutdown\n"
            output += f"exit\n"

    for i in range(1, 16001):
            output += f"lsp t3_1-to-t3_3-lsp-{i} sr-te\n"
            output += f"to 10.245.151.132\n"
            output += f"primary t3_3-path-{i}\n"
            output += f"exit\n"           
            output += f"no shutdown\n"
            output += f"exit\n"
    output += "exit all\n"
    
    for i in range(1, 16001):
            output += f"configure service sdp {i} mpls create\n"
            output += f"far-end 10.245.151.132\n"
            output += f"sr-te-lsp t3_1-to-t3_3-lsp-{i}\n"           
            output += f"no shutdown\n"
            output += f"exit\n"

    output += "exit all\n"
        
        # Write the accumulated output to the file
    f.write(output)
