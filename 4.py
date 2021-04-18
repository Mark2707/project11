numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
text_first = 'Пожалуйста, введите первые 4 циры номера карты:'


card_num = input(text_first)
A = input()

def card(card_num, A):
    if A == 'Yes':
        return
    else:
        for i in range(10 ** 12):
            if len(card_num) > 4:
                return cardq(str(int(card_num)+1), A)
            z = card_num
            i = str(i)
            n = '0' * 12
            if len(i) < 12:
                i = n[len(i)::] + i
                card_num += i
            else:
                card_num += i

            card_num_invers = card_num[::-1]
            even = int(card_num_invers[::-2])
            odd = int(card_num[::-2])
            sum_odd = 0
            sum_even = 0
            for j in str(odd):
                sum_odd += int(j)
            for w in str(even):
                a = int(w) * 2
                if a > 9:
                    a = a // 10 + a % 10
                    sum_even += a
                else:
                    sum_even += int(a)
                full_sum = sum_even + sum_odd
            if full_sum % 10 != 0:
                card_num = z
            else:
                print(card_num)
                return card(card_num, A)


def cardq(card_num, A):
    if A == 'Y':
        return
    else:
        card_num_invers = card_num[::-1]
        even = int(card_num_invers[::-2])
        odd = int(card_num[::-2])
        sum_odd = 0
        sum_even = 0
        for j in str(odd):
            sum_odd += int(j)
        for w in str(even):
            a = int(w) * 2
            if a > 9:
                a = a // 10 + a % 10
                sum_even += a
            else:
                sum_even += int(a)
            full_sum = sum_even + sum_odd
        if full_sum % 10 != 0:
            return cardq(str(int(card_num)+1), A)
        else:
            print(card_num)
            return cardq(str(int(card_num)+1), A=input())


z = card(card_num, A)