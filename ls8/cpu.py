"""CPU functionality."""

import sys

instructions = {
    0b00000000: '???',
    0b00000001: 'HLT',
    0b00000010: 'LDI',
    0b00000111: 'PRN',
    0b00100010: 'MUL'
}


class CPU:
    """Main CPU class."""
    
    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 0xFF  # x is a list of 25 zeroes
        self.registers = [0] * 0x0F
        self.pc = 0     # Program Counter, address of the currently executing instruction
        self.ir = 0     # Instruction Register, contains a copy of the currently executing instruction
        self.mar = 0    # Memory Address Register, holds the memory address we're reading or writing
        self.mdr = 0    # Memory Data Register, holds the value to write or the value just read
        self.fl = 0     # Flags, see below

    # Register getter methods
    @property
    def r0(self):
        return self.registers[0]
    @property
    def r1(self):
        return self.registers[1]
    @property
    def r2(self):
        return self.registers[2]
    @property
    def r3(self):
        return self.registers[3]
    @property
    def r4(self):
        return self.registers[4]
    @property
    def r5(self):
        return self.registers[5]
    @property
    def r6(self):
        return self.registers[6]
    @property
    def r7(self):
        return self.registers[7]

    # Register setter methods
    @r0.setter
    def r0(self, value):
        self.registers[0] = value
    @r1.setter
    def r1(self, value):
        self.registers[1] = value
    @r2.setter
    def r2(self, value):
        self.registers[2] = value
    @r3.setter
    def r3(self, value):
        self.registers[3] = value
    @r4.setter
    def r4(self, value):
        self.registers[4] = value
    @r5.setter
    def r5(self, value):
        self.registers[5] = value
    @r6.setter
    def r6(self, value):
        self.registers[6] = value
    @r7.setter
    def r7(self, value):
        self.registers[7] = value

    def ram_read(self, mar):
        return self.ram[mar]
    
    def ram_write(self, mar, mdr):
        self.ram[mar] = mdr

    def load(self):
        """Load a program into memory."""

        address = 0

        # Load the program from file
        file = None # If open fails, compiler will complain "local variable 'file' referenced before assignment"
        filename = None # And if second argument is missing
        program = []

        try:
            filename = sys.argv[1] # This will throw if there is no second argument
            # filename = "examples/mult.ls8"

            file = open(filename, "r")
            for line in file:
                line = line.split("#", 1) # Find comments
                line = line[0].strip() # Take non-comment portion and trim spaces
                if len(line) == 0: # If there is nothing left...
                    continue 

                byte = int(line, 2)
                program.append(byte)

            if len(program) == 0:
                raise EOFError

        except EOFError:
            print(f"{filename} did not contain a program")
            sys.exit()
        except:
            if len(filename) == 0:
                print("Second argument must be filename: python3 ls8.py examples/print.ls8")
            else:
                print(f"Unable to open filename {filename}")
            sys.exit()

        finally:
            if file is not None:
                file.close()

        # Load the program into RAM
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
        while True:
            # Read the memory address that's stored in register PC, and store that result in the Instruction Register.
            self.ir = self.pc

            cmd = instructions[self.ram_read(self.pc) & 0x3F]

            if cmd == 'HLT':
                return 
            elif cmd == 'LDI':
                self.ldi()
            elif cmd == 'PRN':
                self.prn()
            elif cmd == 'MUL':
                self.mul()
            else:
                print(f"Unsupported instruction: {cmd}")
                return 

            # Advance PC by the highest two order bits
            self.pc = self.pc + (self.ram_read(self.pc) >> 6) + 1

    def ldi(self):
        self.registers[self.ram_read(self.pc + 1) & 0x07] = self.ram_read(self.pc + 2)
        return

    def prn(self):
        print(self.registers[self.ram_read(self.pc + 1) & 0x07])
        return 
        
    def mul(self):
        self.r0 = self.r0 * self.r1
        return

