from .instructionTable import InstructionTable
from .instruction import Instruction


class Machine:

    def __init__(self, program: list, instruction_table: InstructionTable):
        self.program = program
        self.instruction_table = instruction_table
        self.instruction_pointer = 0
        self.operand_stack = []
        self._is_halted = False

    def push_operand(self, operand):
        self.operand_stack.insert(0, operand)

    def pop_operand(self):
        return self.operand_stack.pop(0)

    def get_next_code(self):
        code = self.program[self.instruction_pointer]
        self.instruction_pointer += 1
        return code

    def run(self):
        while not self._is_halted:
            self.step()

    def step(self):
        op_name = self.get_next_code()
        instruction = self.instruction_table.get(op_name)
        if not instruction:
            raise Exception('Instruction ' + op_name + 'does not supported')

        args = []
        for i in range(instruction.arity):
            args.append(self.get_next_code())
        instruction.func(self, args)

    @classmethod
    def get_instruction_table(cls) -> InstructionTable:
        instruction_table = InstructionTable()
        instruction_table.insert(Instruction('PUSH', 1, cls.push))
        instruction_table.insert(Instruction('POP', 0, cls.pop))
        instruction_table.insert(Instruction('DUP', 0, cls.dup))
        instruction_table.insert(Instruction('ADD', 0, cls.add))
        instruction_table.insert(Instruction('SUB', 0, cls.sub))
        instruction_table.insert(Instruction('MUL', 0, cls.mul))
        instruction_table.insert(Instruction('DIV', 0, cls.div))
        instruction_table.insert(Instruction('AND', 0, cls.and_op))
        instruction_table.insert(Instruction('OR', 0, cls.or_op))
        instruction_table.insert(Instruction('NOT', 0, cls.not_op))
        instruction_table.insert(Instruction('ISEQ', 0, cls.is_equal))
        instruction_table.insert(Instruction('ISGT', 0, cls.is_greater))
        instruction_table.insert(Instruction('ISGE', 0, cls.is_greater_equal))
        return instruction_table

    def push(self, args):
        arg = args[0]
        self.push_operand(arg)

    def pop(self, args):
        self.pop_operand()

    def dup(self, args):
        op = self.pop_operand()
        self.push_operand(op)
        self.push_operand(op)

    def add(self, add):
        rh = self.pop_operand()
        lh = self.pop_operand()
        self.push_operand(lh + rh)

    def sub(self, args):
        rh = self.pop_operand()
        lh = self.pop_operand()
        self.push_operand(lh - rh)

    def mul(self, args):
        rh = self.pop_operand()
        lh = self.pop_operand()
        self.push_operand(lh * rh)

    def div(self, args):
        rh = self.pop_operand()
        lh = self.pop_operand()
        self.push_operand(lh / rh)

    def and_op(self, args):
        rh = self.pop_operand()
        lh = self.pop_operand()
        self.push_operand(lh and rh)

    def or_op(self, args):
        rh = self.pop_operand()
        lh = self.pop_operand()
        self.push_operand(lh or rh)

    def not_op(self, args):
        op = self.pop_operand()
        self.push_operand(not op)

    def is_equal(self, args):
        rh = self.pop_operand()
        lh = self.pop_operand()
        self.push_operand(lh == rh)

    def is_greater(self, args):
        rh = self.pop_operand()
        lh = self.pop_operand()
        self.push_operand(lh > rh)

    def is_greater_equal(self, args):
        rh = self.pop_operand()
        lh = self.pop_operand()
        self.push_operand(lh >= rh)
