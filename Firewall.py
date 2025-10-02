# Simple Firewall Simulation script following tutorial from faanross: https://www.youtube.com/watch?v=UfyF6CvL4Ts

# Import the random module to generate random IP addresses and numbers
import random

# Generates random IP addresses in the range 192.168.1.0 to 192.168.1.20
def generate_random_ip():
    return f"192.168.1.{random.randint(0, 20)}"

# Checks if the generated IP address is in the firewall rules and returns the corresponding action
def check_firewall_rules(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"


def main():
    firewall_rules = {
        # 6 arbitrary IP addresses to block
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block",
    }

    # This for loop will simulate network traffic, checking them against the rules and then printing the result.
    for _ in range(12):
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(0, 9999)
        print(f"IP Address: {ip_address}, Action: {action}, Random Number: {random_number}")

# Ensures the main function runs when the script is executed
if __name__ == "__main__":
    main()
