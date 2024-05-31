import sympy as sp
import random

def generate_questions(num_questions):
    """Funcao para gerar questoes dos temas propostos de calculo"""
    if isinstance(num_questions,int):
        questions = []
        x, y = sp.symbols('x y')
        
        num_each = num_questions // 3
        remainder = num_questions % 3
        
        # Partial Derivatives
        for _ in range(num_each):
            a, b = random.randint(1, 99), random.randint(1, 99)
            f = a*x**b + b*y**a
            question = f"Encontre a derivada parcial de f(x, y) = {f} em relação a x."
            answer = sp.diff(f, x)
            questions.append({"question": question, "answer": answer})

        # Optimization
        for _ in range(num_each):
            a, b, c = random.randint(-50,50 ), random.randint(-50, 50), random.randint(-50, 50)
            f = -a*x**2 + b*x + c
            critical_points = sp.solve(sp.diff(f, x), x)
            critical_point = critical_points[0] if critical_points else None
            max_value = f.subs(x, critical_point) if critical_point is not None else None
            question = f"Encontre o ponto máximo de f(x) = {f}."
            answer = max_value
            questions.append({"question": question, "answer": answer})

        # Double Integrals
        for _ in range(num_each + remainder):
            a, b, c, d = random.randint(0, 99), random.randint(1, 99), random.randint(0, 99), random.randint(1, 99)
            f = random.randint(1, 99)
            question = f"Avalie a integral dupla de {f} sobre a região {a} <= x <= {a + random.randint(1,9)} e {c} <= y <= {c + random.randint(1,9)}."
            integral = sp.integrate(sp.integrate(f, (x, a, a + 1)), (y, c, c + 1))
            answer = integral
            questions.append({"question": question, "answer": answer})

        random.shuffle(questions)  # Randomize the order of questions
        return questions
    else: 
        raise ValueError('Por favor use um numero inteiro')
        

