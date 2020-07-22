"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""
    
    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 0xFF  # x is a list of 25 zeroes
        self.pc = 0     # Program Counter, address of the currently executing instruction
        self.ir = 0     # Instruction Register, contains a copy of the currently executing instruction
        self.mar = 0    # Memory Address Register, holds the memory address we're reading or writing
        self.mdr = 0    # Memory Data Register, holds the value to write or the value just read
        self.fl = 0     # Flags, see below

        print(self.r7)
        self.r7 = 0xF4
        print(self.r7)

    # Register getter methods
    @property
    def r0(self):
        return self.ram[0]
    @property
    def r1(self):
        return self.ram[1]
    @property
    def r2(self):
        return self.ram[2]
    @property
    def r3(self):
        return self.ram[3]
    @property
    def r4(self):
        return self.ram[4]
    @property
    def r5(self):
        return self.ram[5]
    @property
    def r6(self):
        return self.ram[6]
    @property
    def r7(self):
        return self.ram[7]

    # Register setter methods
    @r0.setter
    def r0(self, value):
        self.ram[0] = value
    @r1.setter
    def r1(self, value):
        self.ram[1] = value
    @r2.setter
    def r2(self, value):
        self.ram[2] = value
    @r3.setter
    def r3(self, value):
        self.ram[3] = value
    @r4.setter
    def r4(self, value):
        self.ram[4] = value
    @r5.setter
    def r5(self, value):
        self.ram[5] = value
    @r6.setter
    def r6(self, value):
        self.ram[6] = value
    @r7.setter
    def r7(self, value):
        self.ram[7] = value

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        pass
