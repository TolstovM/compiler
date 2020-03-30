from machine import *

program = [
    ['PUSH', [3]],
    ['PUSH', [8]],
    ['MUL', []],
    ['PUSH', [10]],
    ['PUSH', [8]],
    ['PUSH', [2]],
    ['DIV', []],
    ['SUB', []],
    ['PUSH', [3]],
    ['MUL', []],
    ['ADD', []]
]
instruction_table = Machine.get_instruction_table()

builder = Builder(instruction_table)
for code in program:
    builder.put(code[0], code[1])

machine = Machine(builder.get_program(), instruction_table)
for i in range(11):
    machine.step()
print(machine.pop_operand())
