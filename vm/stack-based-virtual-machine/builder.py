from .instructionTable import InstructionTable


class Builder:

    def __init__(self, instruction_table: InstructionTable):
        self.instruction_table = instruction_table
        self.instructions = []

    def put(self, name, args: list):
        instruction = self.instruction_table.get(name)

        if not instruction:
            raise Exception('Instruction ' + name + 'does not support')
        if instruction.arity != len(args):
            raise Exception('Instruction ' + name + " requires " + instruction.arity + ' arguments, but provided ' + len(args))

        self.instructions.append(name)
        for arg in args:
            self.instructions.append(arg)

    def get_program(self):
        return self.instructions
