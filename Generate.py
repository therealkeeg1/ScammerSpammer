import random
import names


class Functions:
    def __init__(self):
        pass

    def expM(self):
        m = random.randint(1,12)
        if m < 10:
            m = "0" + str(m)
        return str(m)

    def email(self):
        return names.get_first_name().lower() + names.get_last_name().lower() + str(random.randint(0,999)) + "@gmail.com"

    def luhn(self, first_6):
        card_no = [int(i) for i in str(first_6)]  # To find the checksum digit on
        card_num = [int(i) for i in str(first_6)]  # Actual account number
        seventh_15 = random.sample(range(9), 9)  # Acc no (9 digits)
        for i in seventh_15:
            card_no.append(i)
            card_num.append(i)
        for t in range(0, 15, 2):  # odd position digits
            card_no[t] = card_no[t] * 2
        for i in range(len(card_no)):
            if card_no[i] > 9:  # deduct 9 from numbers greater than 9
                card_no[i] -= 9
        s = sum(card_no)
        mod = s % 10
        check_sum = 0 if mod == 0 else (10 - mod)
        card_num.append(check_sum)
        card_num = [str(i) for i in card_num]
        card_num.insert(4,"%20")
        card_num.insert(9,"%20")
        card_num.insert(14,"%20")
        return ''.join(card_num)