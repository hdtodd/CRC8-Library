''' tstcrc8.py

    Python program to test the crc8 library functions

    Check CRC results against
       https://www.autosar.org/fileadmin/user_upload/standards/classic/
              20-11/AUTOSAR_SWS_CRCLibrary.pdf
    tables 7.2.1.1 and 7.2.1.2.

    HD Todd, February, 2022
'''

import libcrc8 as crc

msg1 = bytearray([0x00, 0x00, 0x00, 0x00, 0x00])
msg2 = bytearray([0xf2, 0x01, 0x83, 0x00      ]);
msg3 = bytearray([0x0f, 0xaa, 0x00, 0x55, 0x00])
msg4 = bytearray([0x00, 0xff, 0x55, 0x11, 0x00])
msg5 = bytearray([0x33, 0x22, 0x55, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff, 0x00])
msg6 = bytearray([0x92, 0x6b, 0x55, 0x00])
msg7 = bytearray([0xff, 0xff, 0xff, 0xff, 0x00])

print("Program to test/demo CRC-8 library\n");

# check section 7.2.1.1
print("Check table XOR'd CRC with SWS_Crc_00052 in AutoSAR");
poly = 0x1d
crc.buildCRC8Table(poly)
#crc.dumpCRC8Table()
init = 0xff
print("\nWith poly = 0x{:02x}, init = 0x{:02x}".format(crc.getCRC8Poly(), init))

ms = len(msg1)-1
msg1[ms] = crc.crc8(msg1, ms, init)
print("Message+CRC:\t", end="")
for j in range(0,len(msg1)):
    print("0x{:02x} ".format(msg1[j]), end="")
print("\nChecksum of all bytes in msg incl CRC (should be 0x00) = 0x{:02x}".
	 format(crc.crc8(msg1,ms+1,init)));
print("Checksum of msg without CRC xor'd with 0xFF = 0x{:02x}\n".format( msg1[ms] ^ 0xFF) )

ms = len(msg2)-1
msg2[ms] = crc.crc8(msg2, ms, init)
print("Message+CRC:\t", end="")
for j in range(0,len(msg2)):
    print("0x{:02x} ".format(msg2[j]), end="")
print("\nChecksum of all bytes in msg incl CRC (should be 0x00) = 0x{:02x}".
	 format(crc.crc8(msg2,ms+1,init)));
print("Checksum of msg without CRC xor'd with 0xFF = 0x{:02x}\n".format( msg2[ms] ^ 0xFF) )

ms = len(msg3)-1
msg3[ms] = crc.crc8(msg3, ms, init)
print("Message+CRC:\t", end="")
for j in range(0,len(msg3)):
    print("0x{:02x} ".format(msg3[j]), end="")
print("\nChecksum of all bytes in msg incl CRC (should be 0x00) = 0x{:02x}".
	 format(crc.crc8(msg3,ms+1,init)));
print("Checksum of msg without CRC xor'd with 0xFF = 0x{:02x}\n".format( msg3[ms] ^ 0xFF) )

ms = len(msg4)-1
msg4[ms] = crc.crc8(msg4, ms, init)
print("Message+CRC:\t", end="")
for j in range(0,len(msg4)):
    print("0x{:02x} ".format(msg4[j]), end="")
print("\nChecksum of all bytes in msg incl CRC (should be 0x00) = 0x{:02x}".
	 format(crc.crc8(msg4,ms+1,init)));
print("Checksum of msg without CRC xor'd with 0xFF = 0x{:02x}\n".format( msg4[ms] ^ 0xFF) )

ms = len(msg5)-1
msg5[ms] = crc.crc8(msg5, ms, init)
print("Message+CRC:\t", end="")
for j in range(0,len(msg5)):
    print("0x{:02x} ".format(msg5[j]), end="")
print("\nChecksum of all bytes in msg incl CRC (should be 0x00) = 0x{:02x}".
	 format(crc.crc8(msg5,ms+1,init)));
print("Checksum of msg without CRC xor'd with 0xFF = 0x{:02x}\n".format( msg5[ms] ^ 0xFF) )

ms = len(msg6)-1
msg6[ms] = crc.crc8(msg6, ms, init)
print("Message+CRC:\t", end="")
for j in range(0,len(msg6)):
    print("0x{:02x} ".format(msg6[j]), end="")
print("\nChecksum of all bytes in msg incl CRC (should be 0x00) = 0x{:02x}".
	 format(crc.crc8(msg6,ms+1,init)));
print("Checksum of msg without CRC xor'd with 0xFF = 0x{:02x}\n".format( msg6[ms] ^ 0xFF) )

ms = len(msg7)-1
msg7[ms] = crc.crc8(msg7, ms, init)
print("Message+CRC:\t", end="")
for j in range(0,len(msg7)):
    print("0x{:02x} ".format(msg7[j]), end="")
print("\nChecksum of all bytes in msg incl CRC (should be 0x00) = 0x{:02x}".
	 format(crc.crc8(msg7,ms+1,init)));
print("Checksum of msg without CRC xor'd with 0xFF = 0x{:02x}\n\n".format( msg7[ms] ^ 0xFF) )

# check section 7.2.1.2
print("Check table XOR'd CRC with SWS_Crc_00053 in AutoSAR");
poly = 0x2f
crc.buildCRC8Table(poly)
#crc.dumpCRC8Table()
init = 0xff
print("\nWith poly = 0x{:02x}, init = 0x{:02x}".format(crc.getCRC8Poly(), init))

ms = len(msg1)-1
msg1[ms] = crc.crc8(msg1, ms, init)
print("Message+CRC:\t", end="")
for j in range(0,len(msg1)):
    print("0x{:02x} ".format(msg1[j]), end="")
print("\nChecksum of all bytes in msg incl CRC (should be 0x00) = 0x{:02x}".
	 format(crc.crc8(msg1,ms+1,init)));
print("Checksum of msg without CRC xor'd with 0xFF = 0x{:02x}\n".format( msg1[ms] ^ 0xFF) )

ms = len(msg2)-1
msg2[ms] = crc.crc8(msg2, ms, init)
print("Message+CRC:\t", end="")
for j in range(0,len(msg2)):
    print("0x{:02x} ".format(msg2[j]), end="")
print("\nChecksum of all bytes in msg incl CRC (should be 0x00) = 0x{:02x}".
	 format(crc.crc8(msg2,ms+1,init)));
print("Checksum of msg without CRC xor'd with 0xFF = 0x{:02x}\n".format( msg2[ms] ^ 0xFF) )

ms = len(msg3)-1
msg3[ms] = crc.crc8(msg3, ms, init)
print("Message+CRC:\t", end="")
for j in range(0,len(msg3)):
    print("0x{:02x} ".format(msg3[j]), end="")
print("\nChecksum of all bytes in msg incl CRC (should be 0x00) = 0x{:02x}".
	 format(crc.crc8(msg3,ms+1,init)));
print("Checksum of msg without CRC xor'd with 0xFF = 0x{:02x}\n".format( msg3[ms] ^ 0xFF) )

ms = len(msg4)-1
msg4[ms] = crc.crc8(msg4, ms, init)
print("Message+CRC:\t", end="")
for j in range(0,len(msg4)):
    print("0x{:02x} ".format(msg4[j]), end="")
print("\nChecksum of all bytes in msg incl CRC (should be 0x00) = 0x{:02x}".
	 format(crc.crc8(msg4,ms+1,init)));
print("Checksum of msg without CRC xor'd with 0xFF = 0x{:02x}\n".format( msg4[ms] ^ 0xFF) )

ms = len(msg5)-1
msg5[ms] = crc.crc8(msg5, ms, init)
print("Message+CRC:\t", end="")
for j in range(0,len(msg5)):
    print("0x{:02x} ".format(msg5[j]), end="")
print("\nChecksum of all bytes in msg incl CRC (should be 0x00) = 0x{:02x}".
	 format(crc.crc8(msg5,ms+1,init)));
print("Checksum of msg without CRC xor'd with 0xFF = 0x{:02x}\n".format( msg5[ms] ^ 0xFF) )

ms = len(msg6)-1
msg6[ms] = crc.crc8(msg6, ms, init)
print("Message+CRC:\t", end="")
for j in range(0,len(msg6)):
    print("0x{:02x} ".format(msg6[j]), end="")
print("\nChecksum of all bytes in msg incl CRC (should be 0x00) = 0x{:02x}".
	 format(crc.crc8(msg6,ms+1,init)));
print("Checksum of msg without CRC xor'd with 0xFF = 0x{:02x}\n".format( msg6[ms] ^ 0xFF) )

ms = len(msg7)-1
msg7[ms] = crc.crc8(msg7, ms, init)
print("Message+CRC:\t", end="")
for j in range(0,len(msg7)):
    print("0x{:02x} ".format(msg7[j]), end="")
print("\nChecksum of all bytes in msg incl CRC (should be 0x00) = 0x{:02x}".
	 format(crc.crc8(msg7,ms+1,init)));
print("Checksum of msg without CRC xor'd with 0xFF = 0x{:02x}\n\n".format( msg7[ms] ^ 0xFF) )
