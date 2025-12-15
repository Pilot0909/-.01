"""
Задание 7. Калькулятор

Преобразование выражения из инфиксной формы в обратную польскую нотацию (ОПН)
и вычисление результата.
"""


class Calculator:
    """
    Калькулятор, использующий обратную польскую нотацию.
    """
    
    def __init__(self):
        self.precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3,
            '(': 0,
            ')': 0
        }
    
    def infix_to_rpn(self, expression: str) -> list:
        """
        Преобразование выражения из инфиксной формы в ОПН (обратную польскую нотацию).
        
        Алгоритм Дейкстры (алгоритм сортировочной станции).
        
        Временная сложность: O(n), где n - длина выражения
        
        Args:
            expression: Выражение в инфиксной форме (например, "3 + 4 * 2")
            
        Returns:
            Список токенов в ОПН (например, ['3', '4', '2', '*', '+'])
        """
        output = []
        stack = []
        
        tokens = self._tokenize(expression)
        
        for token in tokens:
            if self._is_number(token):
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            elif token in self.precedence:
                while (stack and 
                       stack[-1] != '(' and
                       self.precedence[stack[-1]] >= self.precedence[token]):
                    output.append(stack.pop())
                stack.append(token)
        
        while stack:
            output.append(stack.pop())
        
        return output
    
    def _tokenize(self, expression: str) -> list:
        """
        Разбиение выражения на токены.
        
        Поддерживает числа и операторы: +, -, *, /, ^, (, )
        """
        tokens = []
        i = 0
        while i < len(expression):
            if expression[i].isspace():
                i += 1
                continue
            
            if expression[i].isdigit() or expression[i] == '.':
                num = ""
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num += expression[i]
                    i += 1
                tokens.append(num)
            elif expression[i] in '+-*/^()':
                tokens.append(expression[i])
                i += 1
            else:
                raise ValueError(f"Неизвестный символ: {expression[i]}")
        
        return tokens
    
    def _is_number(self, token: str) -> bool:
        """Проверка, является ли токен числом."""
        try:
            float(token)
            return True
        except ValueError:
            return False
    
    def evaluate_rpn(self, rpn: list) -> float:
        """
        Вычисление выражения в ОПН.
        
        Временная сложность: O(n), где n - количество токенов
        
        Args:
            rpn: Список токенов в ОПН
            
        Returns:
            Результат вычисления
        """
        stack = []
        
        for token in rpn:
            if self._is_number(token):
                stack.append(float(token))
            else:
                if len(stack) < 2:
                    raise ValueError("Недостаточно операндов для операции")
                
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    if b == 0:
                        raise ValueError("Деление на ноль")
                    result = a / b
                elif token == '^':
                    result = a ** b
                else:
                    raise ValueError(f"Неизвестная операция: {token}")
                
                stack.append(result)
        
        if len(stack) != 1:
            raise ValueError("Некорректное выражение")
        
        return stack[0]
    
    def calculate(self, expression: str) -> float:
        """
        Вычисление выражения в инфиксной форме.
        
        Args:
            expression: Выражение в инфиксной форме
            
        Returns:
            Результат вычисления
        """
        rpn = self.infix_to_rpn(expression)
        return self.evaluate_rpn(rpn)


if __name__ == "__main__":
    calc = Calculator()
    
    print("=== Тестирование калькулятора ===")
    
    test_expressions = [
        "3 + 4",
        "3 + 4 * 2",
        "(3 + 4) * 2",
        "10 / 2 - 3",
        "2 ^ 3",
        "2 + 3 * 4 - 5",
        "(1 + 2) * (3 + 4)"
    ]
    
    for expr in test_expressions:
        rpn = calc.infix_to_rpn(expr)
        result = calc.evaluate_rpn(rpn)
        print(f"\nВыражение: {expr}")
        print(f"ОПН: {' '.join(rpn)}")
        print(f"Результат: {result}")


