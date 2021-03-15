import subprocess
import re
import optparse

# Get Options For Program For Interface And The New MAC Address
# Change the MAC Address
# check MAC Address With New MAC Address


def get_options():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Enter an interface")
    parser.add_option("-m", "--mac", dest="new_mac",
                      help="Enter New MAC address")
    (options, args) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please Enter an interface to work with!!!!")
    elif not options.new_mac:
        parser.error("[-] Pleas Enter a MAC address! ")
    return options


def mac_spoof(interface, mac_add):
    print("[+] Disconnecting " + interface)
    subprocess.run(["iconfig", interface, "down"])
    print("[+] Spoofing MAC address...")
    subprocess.run(["ifconfig", interface, "hw", "hw", "ether", "mac_add"])
    print("[+] Reconnecting" + interface)
    subprocess.run(["ifconfig", interface, "up"])


def mac_check(interface):
    # checking ifconfig interface for validity (like lo interface etc.....)
    ifconfig = subprocess.check_output(["ifconfig", options.interface])
    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    if current_mac.group(0):
        return current_mac.group(0)
    else:
        print("[-] Error Reading MAC Address.")


options = get_options()

print("[+] " + options.interface+"MAC Address :" +
      str(mac_check(options.interface)))

mac.spoof(options.interface, options.new_mac)

if mac_check(options.interface) == options.new_mac:
    print("[+] " + options.interface +
          "MAC Address Has Been Spoofed Successfully!!!")
else:
    print("[-] " + options.interface + "MAC Address Spoofing Has FAILED!!!!")
