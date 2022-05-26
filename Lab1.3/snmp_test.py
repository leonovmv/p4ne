from pysnmp.hlapi import *

snmp_engine = SnmpEngine()
community_data = CommunityData("public", mpModel=0)
transport = UdpTransportTarget(("10.31.70.107", 161))
context_data = ContextData()

snmp_system = ObjectIdentity("SNMPv2-MIB", "sysDescr", 0)
snmp_interfaces = ObjectIdentity("1.3.6.1.2.1.2.2.1.2")

result = getCmd(snmp_engine, community_data, transport, context_data, ObjectType(snmp_system))
result2 = nextCmd(snmp_engine, community_data, transport, context_data, ObjectType(snmp_interfaces), lexicographicMode=False)

print("snmp_system")
for e in result:
    for a in e[3]:
        print(a)

print("snmp_interfaces")
for e in result2:
    for a in e[3]:
        print(a)