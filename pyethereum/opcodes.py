opcodes = {
    0x00: ['STOP', 0, 0],
    0x01: ['ADD', 2, 1],
    0x02: ['SUB', 2, 1],
    0x03: ['MUL', 2, 1],
    0x04: ['DIV', 2, 1],
    0x05: ['SDIV', 2, 1],
    0x06: ['MOD', 2, 1],
    0x07: ['SMOD', 2, 1],
    0x08: ['EXP', 2, 1],
    0x09: ['NEG', 2, 1],
    0x0a: ['LT', 2, 1],
    0x0b: ['GT', 2, 1],
    0x0c: ['EQ', 2, 1],
    0x0d: ['NOT', 1, 1],
    0x10: ['AND', 2, 1],
    0x11: ['OR', 2, 1],
    0x12: ['XOR', 2, 1],
    0x13: ['BYTE', 2, 1],
    0x20: ['SHA3', 2, 1],
    0x30: ['ADDRESS', 0, 1],
    0x31: ['BALANCE', 0, 1],
    0x32: ['ORIGIN', 0, 1],
    0x33: ['CALLER', 0, 1],
    0x34: ['CALLVALUE', 0, 1],
    0x35: ['CALLDATALOAD', 1, 1],
    0x36: ['CALLDATASIZE', 0, 1],
    0x37: ['GASPRICE', 0, 1],
    0x40: ['PREVHASH', 0, 1],
    0x41: ['COINBASE', 0, 1],
    0x42: ['TIMESTAMP', 0, 1],
    0x43: ['NUMBER', 0, 1],
    0x44: ['DIFFICULTY', 0, 1],
    0x45: ['GASLIMIT', 0, 1],
    0x51: ['POP', 1, 0],
    0x52: ['DUP', 1, 2],
    0x53: ['SWAP', 2, 2],
    0x54: ['MLOAD', 1, 1],
    0x55: ['MSTORE', 2, 0],
    0x56: ['MSTORE8', 2, 0],
    0x57: ['SLOAD', 1, 1],
    0x58: ['SSTORE', 2, 0],
    0x59: ['JUMP', 1, 0],
    0x5a: ['JUMPI', 2, 0],
    0x5b: ['PC', 0, 1],
    0x5c: ['MSIZE', 0, 1],
    0x5d: ['GAS', 0, 1],
    0x60: ['PUSH', 0, 1], #encompasses 96...127
    0xf0: ['CREATE', 4, 1],
    0xf1: ['CALL', 7, 1],
    0xf2: ['RETURN', 2, 1],
    0xff: ['SUICIDE', 1, 1],
}
reverse_opcodes = {}
for o in opcodes:
    reverse_opcodes[opcodes[o][0]] = o
