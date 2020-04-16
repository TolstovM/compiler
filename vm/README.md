# Описание тестов


##test1
Выполнение арефметических операций 
    
    3*8+(10-8/2)*3
    
Набор команд для выполнения

    PUSH 3
    PUSH 8
    MUL
    PUSH 10
    PUSH 8
    PUSH 2
    DIV
    SUB
    PUSH 3
    MUL
    ADD
    FUNC' 'print' 1
    HALT
    
Полученный результат 

    42.0
    
    
##test2
Выполнение логических операций и сравнения

    3*8+(10-8/2)*3 == 42 and True
    
Набор команд 

    PUSH 3
    PUSH 8
    MUL
    PUSH 10
    PUSH 8
    PUSH 2
    DIV
    SUB
    PUSH 3
    MUL
    ADD
    PUSH 42
    ISEQ
    PUSH True
    AND
    FUNC' 'print' 1
    HALT
    
Полученный результат

    True
    
    
##test3

Условный переход
        
    a = 100
    b = 30
    if a > b:
        c = a
    else:
        c = b
    print(c)
    
Набор команд

    PUSH 100
    STORE 'a'
    PUSH 30
    SRORE 'b'
    LOAD 'a'
    LOAD 'b'
    ISGT 
    JUMP_IF
    LOAD 'b'
    STORE 'c'
    JUMP
    LOAD 'a'
    STORE 'c'
    LOAD 'c'
    FUNC' 'print' 1
    HALT
    
Результат 

    100
    
Цикл while

    a = 16
    b = 10
    while a > b:
        a -= 1
        print(a)
        
Набор команд

    PUSH 16
    STORE 'a'
    PUSH 10
    STORE 'b'
    LOAD 'a'
    LOAD 'b'
    ISGT
    NOT
    JUMP_IF 30
    LOAD 'a'
    PUSH 1
    SUB
    STORE 'a'
    LOAD 'a'
    FUNC 'print' 1
    JUMP 8
    HALT
    
Результат

    15
    14
    13
    12
    11
    10
    
    
##test5

Собственные функции

    print(pow(2, 8))
    
    def pow(a, b):
        result = 1
        i = 0
        while b > i:
            result *= a
            i += 1
        return result
        
Набор команд

    PUSH' 2
    PUSH' 8
    CALL' 10
    FUNC' 'print' 1
    HALT'
    STORE' 'b'
    STORE' 'a'
    PUSH' 1
    STORE' 'result'
    PUSH' 0
    STORE' 'i'
    LOAD' 'b'
    LOAD' 'i'
    ISGT'
    NOT'
    JUMP_IF' 46
    LOAD' 'a'
    LOAD' 'result'
    MUL'
    STORE 'result'
    LOAD 'i'
    PUSH 1
    ADD
    STORE i
    JUMP 22
    LOAD result
    RET
    
Результат 

    256