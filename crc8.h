uint8_t crc8(uint8_t *msg, int sizeOfMsg, uint8_t init);
void buildCRC8Table(uint8_t poly);
uint8_t getCRC8Poly(void);
void dumpCRC8Table(void);
