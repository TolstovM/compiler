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
    
Полученный результат

    True