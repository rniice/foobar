def answer(total_lambs):
    def pay_henchman(stingy, avail_lambs, n_1_pay, n_2_pay):
        max_pay = 2 * n_1_pay
        min_pay = n_1_pay + n_2_pay
        if stingy and avail_lambs >= min_pay: return min_pay
        elif not stingy and avail_lambs >= max_pay: return max_pay
        elif not stingy and avail_lambs >= min_pay: return avail_lambs
        else: return 0

    def generatePayouts(payouts, stinginess, total_lambs):
        next_rank = 3
        rem_lambs = total_lambs - 2 if stinginess else total_lambs -3
        while(True):
            next_pay = pay_henchman(stinginess, rem_lambs, payouts[next_rank - 1], payouts[next_rank - 2])
            if next_pay == 0: break
            payouts[next_rank] = next_pay
            rem_lambs -= next_pay
            next_rank += 1
        return payouts

    if total_lambs == 1: return 1 #handle the exception condition
    pay_stingy   = generatePayouts({1:1, 2:1}, True, total_lambs)
    pay_generous = generatePayouts({1:1, 2:2}, False, total_lambs)
    diff         = len(pay_stingy) - len(pay_generous)
    return diff

print(answer(143))