/*  tstcrc8.c

    Test the crc8 library functions

    Check CRC results against
       https://www.autosar.org/fileadmin/user_upload/standards/classic/
              20-11/AUTOSAR_SWS_CRCLibrary.pdf
    tables 7.2.1.1 and 7.2.1.2.

    HD Todd, February, 2022
*/

#include <stdio.h>
#include <stdint.h>
#include "crc8.h"

void main(void) {
  uint8_t poly, init;
  int ms;
  
  uint8_t  msg1[5] = {0x00, 0x00, 0x00, 0x00, 0x00};
  uint8_t  msg2[4] = {0xf2, 0x01, 0x83, 0x00      };
  uint8_t  msg3[5] = {0x0f, 0xaa, 0x00, 0x55, 0x00};
  uint8_t  msg4[5] = {0x00, 0xff, 0x55, 0x11, 0x00};
  uint8_t  msg5[10]= {0x33, 0x22, 0x55, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff, 0x00};
  uint8_t  msg6[4] = {0x92, 0x6b, 0x55, 0x00};
  uint8_t  msg7[5] = {0xff, 0xff, 0xff, 0xff, 0x00};

  printf("Program to test/demo CRC-8 library\n");

  /* check section 7.2.1.1 */

  printf("Check table XOR'd CRC with SWS_Crc_00053 in AutoSAR\n");
  poly = 0x1d;
  buildCRC8Table(poly);
//dumpCRC8Table();
  init = 0xff;
  printf("\nWith poly = 0x%02x, init = 0x%02x\n", getCRC8Poly(), init);
  
  ms = sizeof(msg1)-1;
  msg1[ms] = crc8(msg1, ms, init);
  printf("Message+CRC:\t");
  for (int j=0; j<sizeof(msg1); j++) printf("0x%02x ", msg1[j]);
  printf("\nChecksum xor'd with 0xFF = 0x%02x\n\n", msg1[ms] ^ 0xFF);

  ms = sizeof(msg2)-1;
  msg2[ms] = crc8(msg2, ms, init);
  printf("Message+CRC:\t");
  for (int j=0; j<sizeof(msg2); j++) printf("0x%02x ", msg2[j]);
  printf("\nChecksum xor'd with 0xFF = 0x%02x\n\n", msg2[ms] ^ 0xFF);

  ms = sizeof(msg3)-1;
  msg3[ms] = crc8(msg3, ms, init);
  printf("Message+CRC:\t");
  for (int j=0; j<sizeof(msg3); j++) printf("0x%02x ", msg3[j]);
  printf("\nChecksum xor'd with 0xFF = 0x%02x\n\n", msg3[ms] ^ 0xFF);

  ms = sizeof(msg4)-1;
  msg4[ms] = crc8(msg4, ms, init);
  printf("Message+CRC:\t");
  for (int j=0; j<sizeof(msg4); j++) printf("0x%02x ", msg4[j]);
  printf("\nChecksum xor'd with 0xFF = 0x%02x\n\n", msg4[ms] ^ 0xFF);

  ms = sizeof(msg5)-1;
  msg5[ms] = crc8(msg5, ms, init);
  printf("Message+CRC:\t");
  for (int j=0; j<sizeof(msg5); j++) printf("0x%02x ", msg5[j]);
  printf("\nChecksum xor'd with 0xFF = 0x%02x\n\n", msg5[ms] ^ 0xFF);

  ms = sizeof(msg6)-1;
  msg6[ms] = crc8(msg6, ms, init);
  printf("Message+CRC:\t");
  for (int j=0; j<sizeof(msg6); j++) printf("0x%02x ", msg6[j]);
  printf("\nChecksum xor'd with 0xFF = 0x%02x\n\n", msg6[ms] ^ 0xFF);

  ms = sizeof(msg7)-1;
  msg7[ms] = crc8(msg7, ms, init);
  printf("Message+CRC:\t");
  for (int j=0; j<sizeof(msg7); j++) printf("0x%02x ", msg7[j]);
  printf("\nChecksum xor'd with 0xFF = 0x%02x\n\n", msg7[ms] ^ 0xFF);

  /* check section 7.2.1.2 */
  
  printf("Check table XOR'd CRC with SWS_Crc_00053 in AutoSAR\n");
  poly = 0x2f;
  buildCRC8Table(poly);
//dumpCRC8Table();
  init = 0xff;
  printf("\nWith poly = 0x%02x, init = 0x%02x\n", getCRC8Poly(), init);
  
  ms = sizeof(msg1)-1;
  msg1[ms] = crc8(msg1, ms, init);
  printf("Message+CRC:\t");
  for (int j=0; j<sizeof(msg1); j++) printf("0x%02x ", msg1[j]);
  printf("\nChecksum xor'd with 0xFF = 0x%02x\n\n", msg1[ms] ^ 0xFF);

  ms = sizeof(msg2)-1;
  msg2[ms] = crc8(msg2, ms, init);
  printf("Message+CRC:\t");
  for (int j=0; j<sizeof(msg2); j++) printf("0x%02x ", msg2[j]);
  printf("\nChecksum xor'd with 0xFF = 0x%02x\n\n", msg2[ms] ^ 0xFF);

  ms = sizeof(msg3)-1;
  msg3[ms] = crc8(msg3, ms, init);
  printf("Message+CRC:\t");
  for (int j=0; j<sizeof(msg3); j++) printf("0x%02x ", msg3[j]);
  printf("\nChecksum xor'd with 0xFF = 0x%02x\n\n", msg3[ms] ^ 0xFF);

  ms = sizeof(msg4)-1;
  msg4[ms] = crc8(msg4, ms, init);
  printf("Message+CRC:\t");
  for (int j=0; j<sizeof(msg4); j++) printf("0x%02x ", msg4[j]);
  printf("\nChecksum xor'd with 0xFF = 0x%02x\n\n", msg4[ms] ^ 0xFF);

  ms = sizeof(msg5)-1;
  msg5[ms] = crc8(msg5, ms, init);
  printf("Message+CRC:\t");
  for (int j=0; j<sizeof(msg5); j++) printf("0x%02x ", msg5[j]);
  printf("\nChecksum xor'd with 0xFF = 0x%02x\n\n", msg5[ms] ^ 0xFF);

  ms = sizeof(msg6)-1;
  msg6[ms] = crc8(msg6, ms, init);
  printf("Message+CRC:\t");
  for (int j=0; j<sizeof(msg6); j++) printf("0x%02x ", msg6[j]);
  printf("\nChecksum xor'd with 0xFF = 0x%02x\n\n", msg6[ms] ^ 0xFF);

  ms = sizeof(msg7)-1;
  msg7[ms] = crc8(msg7, ms, init);
  printf("Message+CRC:\t");
  for (int j=0; j<sizeof(msg7); j++) printf("0x%02x ", msg7[j]);
  printf("\nChecksum xor'd with 0xFF = 0x%02x\n\n", msg7[ms] ^ 0xFF);

}
