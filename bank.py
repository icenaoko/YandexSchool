import math
import numpy

def creditCalculator(age, gender, incomeSource, income, creditRating, requestedSum, duration, purpose):
    # age: not negative int
    if not isinstance(age, int):
        return 'Data validation fails'
    
    # gender: ['F', 'M']
    if gender not in list(['F', 'M']):
        return 'Data validation fails'

    # incomeSource: [пассивный доход, наёмный работник, собственный бизнес, безработный],
    if incomeSource not in list(['passive', 'employee', 'self-employed', 'unemployed']):
        return 'Data validation fails'

    # income: int,
    if not isinstance(income, int) or income <= 0:
        return 'Data validation fails'

    # creditRating: [-2, -1, 0, 1, 2],
    if creditRating not in range(-2, 3):
        return 'Data validation fails'

    # requestedSum: [0.1 .. 10],
    if not (isinstance(requestedSum, float) or isinstance(requestedSum, int)) or requestedSum < 0.1 or requestedSum > 10:
        return 'Data validation fails'

    # duration: [1 .. 20],
    if duration not in range(1, 21):
        return 'Data validation fails'

    # purpose: [ипотека, развитие бизнеса, автокредит, потребительский]
    if purpose not in list(['mortgage', 'business', 'car', 'consumer']):
        return 'Data validation fails'

    # 1. Если возраст превышает пенсионный возраст на момент возврата кредита. 60 лет для женщин и 65 лет для мужчин.
    ageFinal = age + duration
    if gender == 'F' and ageFinal > 60:
        return 'Credit application denied'
    elif gender == 'M' and ageFinal > 65:
        return 'Credit application denied'

    # 2. Если человек не совершеннолетний (младше 18 лет).
    if age < 18:
        return 'Credit application denied'

    # 3. Если результат деления запрошенной суммы на срок погашения в годах более трети годового дохода.
    payment = requestedSum / ( duration + 0.0 )
    incomeThird = income / 3.0
    if payment > incomeThird:
        return 'Credit application denied'

    # 4. Если кредитный рейтинг -2.
    if creditRating == -2:
        return 'Credit application denied'

    # 5. Если в источнике дохода указано "безработный".
    if incomeSource == 'unemployed':
        return 'Credit application denied'

    # Суммы кредита:
    # 1. Если работают несколько условий по сумме кредита — выбирается наименьшая. 
    # 2. Если человек просит сумму, большую возможной для выдачи, кредит не выдаётся.
    # 3. При пассивном доходе выдаётся кредит на сумму до 1 млн, наёмным работникам — до 5 млн, собственное дело — до 10 млн.
    # 4. При кредитном рейтинге -1 выдаётся кредит на сумму до 1 млн, при 0 — до 5 млн, при 1 или 2 — до 10 млн
    if incomeSource == 'passive':
        creaditLimitByIncomeSourse = 1
    elif incomeSource == 'employee':
        creaditLimitByIncomeSourse = 5
    elif incomeSource == 'self-employed':
        creaditLimitByIncomeSourse = 10
    
    if creditRating == -1:
        creaditLimitByCreditRating = 1
    elif creditRating == 0:
        creaditLimitByCreditRating = 5
    elif creditRating == 1 or creditRating == 2:
        creaditLimitByCreditRating = 10

    creditLimit = min(creaditLimitByIncomeSourse, creaditLimitByCreditRating)

    print(creditLimit)

    if requestedSum > creditLimit:
        return 'Credit application denied'

    # базовая ставка — 10%
    persentage = 10

    # 1. Все модификаторы процентной ставки суммируются, применяется итоговый модификатор
    # 2. -2% для ипотеки, -0.5% для развития бизнеса, +1.5% для потребительского кредита
    # 3. +1.5% для кредитного рейтинга -1, 0% для кредитного рейтинга 0, -0.25% для кредитного рейтинга 1,
    #    -0.75% для кредитного рейтинга 2
    # 4. Модификатор в зависимости от запрошенной суммы рассчитывается по формуле [-log(sum)];
    #    например, для 0.1 млн изменение ставки составит +1%, для 1 млн - 0%, для 10 млн изменение ставки составит -1%
    # 5. Для пассивного дохода ставка повышается на 0.5%, для наемных работников ставка снижается на 0.25%,
    #    для заёмщиков с собственным бизнесом ставка повышается на 0.25%

    if purpose == 'mortgage':
        persentage = persentage - 2
    elif purpose == 'business':
        persentage = persentage - 0.5
    elif purpose == 'consumer':
        persentage = persentage + 1.5

    if creditRating == -1:
        persentage = persentage + 1.5
    elif creditRating == 1:
        persentage = persentage - 0.25
    elif creditRating == 2:
        persentage = persentage - 0.75

    persentage = persentage - math.log(requestedSum, 10)

    if incomeSource == 'passive':
        persentage = persentage + 0.5
    elif incomeSource == 'employee':
        persentage = persentage - 0.25
    elif incomeSource == 'self-employed':
        persentage = persentage + 0.25
    
    # Годовой платеж по кредиту определяется по следующей формуле: 
    # (<сумма кредита> * (1 + <срок погашения> * (<базовая ставка> + <модификаторы>)/100)) / <срок погашения>

    yearPayment = requestedSum * (1 + duration * persentage / ( 100 + 0.0) ) / ( duration + 0.0 )
    yearPayment = round(yearPayment, 4)

    # 6. Если годовой платёж (включая проценты) больше половины дохода.
    if yearPayment > ( income * 0.5 ):
        return 'Credit application denied'

    return list(['Approved', yearPayment])

if __name__ == "__main__":
    print('Approved', creaditCalculator(18, 'F', 'self-employed', 2, -1, 1, 20, 'mortgage'))

