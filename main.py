from scipy.integrate import quad
from math import exp, sqrt, pi

data = [8378, 8373, 8385, 8376, 8394, 8385, 8375, 8373, 8374, 8373, 8374, 8393, 8366, 8462, 8366, 8377,
        8375, 8364, 8385, 8381, 8381, 8386, 8381, 8376, 8373, 8370, 8376, 8381, 8390, 8369, 8367, 8390, 8366,
        8400, 8375, 8385, 8373, 8377, 8389, 8374]

N = len(data)
print(f"N = {N} (число измерений)")

x_average = sum(data) / len(data)
print(f"<X> = {x_average} (среднее значение X)")

sigma = sqrt(sum((x - x_average) ** 2 for x in data) / (len(data) - 1))
print(f"СКО = {sigma} (среднеквадратическое отклонение)")


def f(x):
    return exp((-1 / 2) * ((x - x_average) / sigma) ** 2) / (sigma * sqrt(2 * pi))


def Prob(a, b):
    return quad(f, a, b)[0]


n = 4
print(f"n = {n} (число число интервалов)")

interval_1 = [x for x in data if x < x_average - sigma]
interval_2 = [x for x in data if x_average - sigma < x < x_average]
interval_3 = [x for x in data if x_average < x < x_average + sigma]
interval_4 = [x for x in data if x_average + sigma < x]

ok = [len(interval_1), len(interval_2), len(interval_3), len(interval_4)]

print(f"""
Распределение по интервалам (оk):
x < <X> - sigma :         о1 = {ok[0]}
<X> - sigma < x < <X> :   о2 = {ok[1]}
<X> < x < <X> + sigma :   о3 = {ok[2]}
<X> + sigma < x :         о4 = {ok[3]}
""")

print("Гистограмма:")
for i in ok: print('#' * i)

prob1 = Prob(-float('inf'), x_average - sigma)
prob2 = Prob(x_average - sigma, x_average)
prob3 = Prob(x_average, x_average + sigma)
prob4 = Prob(x_average + sigma, float('inf'))

print(f"""
Значение интеграла (Probk):
предел интегрирования
от -oo до <X> - sigma :   Prob1 = {prob1}
от <X> - sigma до <X> :   Prob2 = {prob2}
от <X> до <X> + sigma :   Prob3 = {prob3}
от <X> + sigma до x :     Prob4 = {prob4}
""")

ek = [prob1 * N, prob2 * N, prob3 * N, prob4 * N]

print(f"""
Значение ожидаемого числа попаданий Ek = N * Probk:
E1 = {ek[0]}
E2 = {ek[1]}
E3 = {ek[2]}
E4 = {ek[3]}
""")

k = n - 1
print(f"k = n(число интервалов) - 1 = {k} (число степеней свободы)\n")

X2 = sum((ok[i] - ek[i]) ** 2 / ek[i] for i in range(n))
print(f"X^2 = {X2} (хи-квадрат)")

print("""
Смотрим в таблицу \"Критических точек распределения хи-квадрат\" и ищем табличное значение на пересечении уровня значимости
и числа степеней свободы k. Если полученное значение X^2 <= <табличное значение>, то данные соответствуют нормальному распределению.
В ином случае не соответствуют.
""")
print("====== Для k = 3 и уровня значимости 5% <табличное значение> = 7,8 ======")
