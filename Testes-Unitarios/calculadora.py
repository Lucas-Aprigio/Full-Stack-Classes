from unittest import TestCase, main

valor=0
def calculator(num1,num2,operator):
    if operator == '+':
        valor=num1 + num2
    elif operator == '-':
        valor=num1 - num2
    elif operator == '*':
        valor=num1 * num2
    elif operator == '/':
        valor=num1 / num2
    return valor

class Testes(TestCase):
    def test_soma(self):
        self.assertEqual(calculator(3,5,'+'), 8)
        self.assertEqual(calculator(0,0,'+'), 0)
        self.assertEqual(calculator(1,1,'+'), 2)
        self.assertEqual(calculator(9,6,'+'),15)   
    def test_sub(self):
        self.assertEqual(calculator(6,5,'-'), 1)
        self.assertEqual(calculator(0,3,'-'), -3)
        self.assertEqual(calculator(1,1,'-'), 0)
        self.assertEqual(calculator(9,6,'-'), 3)
    def test_mult(self):
        self.assertEqual(calculator(3,5,'*'), 15)
        self.assertEqual(calculator(0,0,'*'), 0)
        self.assertEqual(calculator(1,1,'*'), 1)
        self.assertEqual(calculator(9,6,'*'), 54)
    def test_div(self):
        self.assertEqual(calculator(36,6,'/'), 6)
        self.assertEqual(calculator(100,10,'/'), 10)
        self.assertEqual(calculator(1,1,'/'), 1)
        self.assertEqual(calculator(9,3,'/'), 3)

if __name__ == '__main__':
    main()
