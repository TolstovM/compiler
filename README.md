# compiler
Компилятор python на python + виртуальная машина на python

<b>Исполнители:</b>
<p>Компилятор</p>
<uL>
    <li>Кубленко Павел, группа 4.1, email: kublenko_p_v@sc.vsu.ru;</li>
    <li>Григорьев Владимир, группа 4.1;</li>
</uL>
<p>Виртуальная машина</p>
<ul>
    <li>Толстов Максим, группа 4.1, email: maksfox0@gmail.com;</li>
</ul>

#stack-based virtual machine
Список инструкций, поддерживаемых виртуальной машиной.

| Instruction | Argument | Description |
| --- | --- | --- |
| HALT | - | Сигнал завершения программы |
| PUSH | + | Добавляет аргумент в стек |
| POP | - | Извлекает значение из стека |
| DUP | - | Дублирует верхний элемент в стеке |
| ADD | - | Извлекает из стека 2 элемента, складывает и возвращает результат в стек |
| SUB | - | Вычетает первый элемент в стеке из второго, извлекая их, возвращает результат в стек |
| MUL | - | Извлекакет из стека 2 элемента, умножает, возвращает результат в стек |
| DIV | - | Делит второй элемент в стеке на первый, извлекая их, возвращает результат в стек |
| AND | - | Извлекает из стека 2 элемента, возвращает результат логического и в стек  |
| OR | - | Извлекакет из стека 2 элемента, возвращает логическое или в стек |
| NOT | - | Извлекает из стека элемент, возвращает лочическое не |
| ISEQ | - | a == b |
| ISGT | - | a > b |
| ISGE | - | a >= b |
| JUMP | + | Сдвигает указатель на указанное число инструкций |
| JUMP_IF | + | Сдвигает указатель на указанное число инструкций, если предыдущее значение в стеке true, извлекает его |
| LOAD | + | Загружает переменную из контекста |
| STORE | + | Сохраняет переменную в контекст |
| FUNC | + | Вызов встроенной функции. Например, print, input, int, str и тд. Принимает 2 аргумента: имя функции и количество аргументов, принимаемых функцией | 
| CALL | + | Вызов функции |
| RET | - | Возвращение из функции |
| NEW_LIST | - | Создает список |
| NEW_DICT | - | Создает словарь |
| *** | *** | Инструкции для работы со списками и словарями |
