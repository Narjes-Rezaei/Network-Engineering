
from netmiko import ConnectHandler

cisco_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.122.200',
    'username': 'admin',
    'password': 'cisco123',
    # الگوریتم‌های قدیمی‌تر برای پشتیبانی از IOS 12.4
    'ssh_strict': False,
}

config_commands = [
    'interface Loopback0',
    'description Configured by Netmik Python Script',
    'ip address 1.1.1.1 255.255.255.255',
    'no shutdown'
]



print("Connecting to router...")
try:
    net_connect = ConnectHandler(**cisco_router)

    print("Sending configuration commands...")
    output = net_connect.send_config_set(config_commands)
    print(output)

    print("\n--- Verifying Loopback0 Status ---")
    verification = net_connect.send_command('show ip interface brief')
    print(verification)


    # output = net_connect.send_command('show ip interface brief')
    # print("\n--- Output from R1 ---")
    # print(output)
    net_connect.disconnect()
except Exception as e:
    print(f"Error: {e}")