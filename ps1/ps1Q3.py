def first_method(tot, por, ann_sal, rr, sem):
    # a massage variable
    msg = ""
    # a boolean initialized to false that determine if we found an answer on not
    first = True
    # defining the accuracy
    acc = 10000

    for i in range(0, acc + 1):
        # initializing current savings for every percentile value
        current_savings = 0.0
        # Calculates the monthly salary
        monthly_salary = ann_sal / 12
        # iterate over all 36 months
        for month in range(36):
            # adds the annual rate from the investment
            current_savings += current_savings * rr / 12
            # this if statement make sure to check if the payment is possible within the annual salary before trying to
            # find the percentage
            if first:
                # rate of 100% of the salary
                current_savings += monthly_salary * 1
            else:
                # changing rate of 0.0001, 0.0002, 0.0003, ...
                current_savings += monthly_salary * (i / acc)
            # raise the monthly salary every 6 months
            if month % 6 == 0:
                monthly_salary += monthly_salary * sem

        # if this is the first iteration that means we checked if 100% is enough
        if first:
            first = False
            # if it is not enough save the message and throw us out of the loop
            if current_savings < (tot * por) - 100:
                msg = "It is not possible to pay the down payment in three years"
                break
            # if it is possible, save the rate for the case that exactly 100% of the salary is needed to succeed within
            # 3 years
            else:
                msg = "Best saving rate: 1.0000" + "\nnumber of iterations: 10000"
        # if this is not the first time then it is possible to buy the house, maybe with lower percentage per month
        else:
            # if the checked rate was successful save the parameters and throw us out of the loop
            if current_savings >= (tot * por) - 100:
                msg = "Best saving rate: " + str(i / acc) + "\nnumber of iterations: " + str(i)
                break
    # print the saved message
    print(msg)

def second_method(tot, por, ann_sal, rr, sem):
    # a massage variable
    msg = ""
    # a boolean that declares whether the percentage found or not
    found = False
    # iteration counter
    i = 1
    # top percentage limit
    p_t = 1.0000
    # lower percentage limit
    p_l = 0.0000
    # the percentage limit. initialized to 1 in order to check on the first iteration if it is possible to buy the house
    # with the given salary
    p = p_t
    # keeps iterating until a break occurs
    while not found:
        #
        if i == 1 or abs(p - p_t) > 0.0001:
            # initialize my current savings and monthly salary before checking a new percentage rate
            current_savings = 0.0
            monthly_salary = ann_sal/12
            # iterating over 3 years period
            for months in range(36):
                # adds the annual rate from the investment
                current_savings += current_savings * rr/12
                # adds the agreed percentage to my current savings. the percentage is changing according to
                # lion in the desert
                current_savings += monthly_salary * p
                # raise the monthly salary every 6 months
                if months % 6 == 0:
                    monthly_salary += monthly_salary * sem
            # if this is the first iteration that means we checked if 100% is enough
            if i == 1:
                # if it is not enough save the message and throw us out of the loop
                if current_savings < (tot * por) - 100:
                    msg = "It is not possible to pay the down payment in three years"
                    break
                # if it is possible, save the rate for the case that exactly 100% of the salary is needed to succeed within
                # 3 years
                else:
                    msg = "Best saving rate: " + str(round(p, 4)) + "\nnumber of iterations: " + str(i)
            # if this is not the first time then it is possible to buy the house, maybe with lower percentage per month
            else:
                # if the checked rate was unsuccessful, set the lower limit to the current p value
                if current_savings < (tot * por) - 100:
                    p_l = p
                # if the checked rate was successful, save the parameters and set the top limit to the current p value
                elif current_savings >= (tot * por) - 100:
                    p_t = p
                    msg = "Best saving rate: " + str(round(p, 4)) + "\nnumber of iterations: " + str(i)
            # set the percentage value to the average of the lower and upper limit
            p = (p_t + p_l) / 2
            # increase counter by 1
            i += 1
        else:
            break
    # print the saved message
    print(msg)


# The portion that I have to pay as part of the installment agreement
portion_down_payment = 0.25
# An annual investment rate
r = 0.04
# The total cost of a house
total_cost = 1000000.0
# The raise percentage that occur every 6 months
semi_annual_raise = 0.07
# The annual salary I make
annual_salary = float(input("Enter your annual salary: "))

first_method(total_cost, portion_down_payment, annual_salary, r, semi_annual_raise)
second_method(total_cost, portion_down_payment, annual_salary, r, semi_annual_raise)
