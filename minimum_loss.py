pn = int(input().strip())
ps = [(int(x), idx) for idx, x in enumerate(input().strip().split(' '))]
ps.sort(reverse=True)
# print("ps: {0}".format(ps))
# chcemy znalesc pierwszy wiekszy i puzniejszy
best_loss = None
for i in range(0, pn - 1):
    (buy_price, buy_time) = ps[i]
    for ii in range(i + 1, pn):
        (sell_price, sell_time) = ps[ii]
        if sell_time > buy_time and buy_price > sell_price:
            if best_loss == None:
                best_loss = sell_price - buy_price
            else:
                best_loss = max(best_loss, sell_price - buy_price)
            break
print("{0}".format(-best_loss))
