def position_size(balance, entry, stop, leverage, loss):
    risk = (1 - stop / entry) * 100
    potential_loss = balance / 100 * loss
    result = (potential_loss * 100) / (risk * leverage)
    return str(result) + " $"


def price_distance(open_p, percent, l_or_s: bool):
    if l_or_s:
        return str(open_p - (open_p/100*percent)) + " $"
    else:
        return str(open_p + (open_p/100*percent)) + " $"


# if __name__ == '__main__':
#     print(position_size(130000, 20000, 19000, 7, 15))