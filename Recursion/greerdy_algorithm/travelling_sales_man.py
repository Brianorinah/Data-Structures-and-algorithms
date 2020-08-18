# def basic_small_change(denom, total_amount):
#     sorted_denom = sorted(denom , reverse= True)
#     print(sorted_denom)

#     returned_change = []
#     for cash in sorted_denom:
#         div = total_amount // cash        
#         if div > 0:
#             total_amount = total_amount % cash
#             returned_change.append((cash , div))

#     return returned_change

# print(basic_small_change([5,1,8], 20))

#More optimal solution
#O(n) most likely loglinear O(nlogn) research!!

def optimal_small_change(denom, total_amount):
    sorted_denominations = sorted(denom, reverse=True)
    possible_comb_list = []

    for j in range(len(sorted_denominations)):
        term_list = sorted_denominations[j:]
        number_of_denoms = []
        local_total = total_amount
        coins = 0

        for i in term_list:
            div = local_total // i            
            if div > 0:
                local_total = local_total % i
                coins = coins + div
                number_of_denoms.append((i, div))
        number_of_denoms.append(coins)
        possible_comb_list.append(number_of_denoms)

    no_of_coins_list = sorted([x[-1] for x in possible_comb_list])

    return no_of_coins_list[0]

print(optimal_small_change([5,1,8], 68))
