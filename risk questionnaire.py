import csv

def get_credentials():
    username = input("Please key in your username: ")
    password = input("Please key in your password: ")

    return username, password

    print(user_account)

def risk_questionnaire():
    response = []

    # question 1 - investment objective
    objective = """
    Which of the following do you think 
    best describes your investment objectives?

    A. Your primary focus is on capital growth. You are prepared to
    accept a high level of short term volatility and possible capital
    losses in order to generate potentially higher levels of capital
    growth over the long term. You are well placed to recover
    from unforeseen market downturns either because you have
    time on your side or access to capital reserves. 

    B. You require your investments to be a balance between
    capital growth and income generating assets. Calculated
    risks will be acceptable as you are prepared to accept short
    term levels of volatility in order to outperform inflation.

    C. Generating a regular income stream is a priority over capital
    growth. You are prepared to sacrifice higher returns in favour
    of preservation of capital

    """

    score = 0
    count = 0

    investment_objective = str(input(objective))
    investment_objective = investment_objective.upper()

    while count <= 0:
        if investment_objective == "A":
            score += 1
            count += 1
            response.append(investment_objective)
        elif investment_objective == "B":
            score += 3
            count += 1
            response.append(investment_objective)
        elif investment_objective == "C":
            score += 5
            count += 1
            response.append(investment_objective)
        else:
            investment_objective = str(input(objective))

    print(score)
    print(count)
    print(response)

    # question 2 - investible capital
    capital = """
    What percentage of your risk capital are you comfortable 
    will you be investing?

    ** Risk capital means funds and assets which if lost would not
    materially change your lifestyle or your family's lifestyle.

    A. Greater than 70%

    B. 35% to 70%

    C. Less than 35%

    """

    risk_capital = str(input(capital))
    risk_capital = risk_capital.upper()

    while count <= 1:
        if risk_capital == "A":
            score += 1
            count += 1
            response.append(risk_capital)
        elif risk_capital == "B":
            score += 3
            count += 1
            response.append(risk_capital)
        elif risk_capital == "C":
            score += 5
            count += 1
            response.append(risk_capital)
        else:
            risk_capital = str(input(capital))

    print(score)
    print(count)
    print(response)

    # question 3 - draw down period
    draw_down = """
    Once investments have been placed, how long would it be 
    before you would need to access your capital?

    A. > 2 Years

    B. Between 6 Months and 2 Years

    C. Less than 6 Months

    """

    draw_down_period = str(input(draw_down))
    draw_down_period = draw_down_period.upper()

    while count <= 2:
        if draw_down_period == "A":
            score += 1
            count += 1
            response.append(draw_down_period)
        elif draw_down_period == "B":
            score += 3
            count += 1
            response.append(draw_down_period)
        elif draw_down_period == "C":
            score += 5
            count += 1
            response.append(draw_down_period)
        else:
            draw_down_period = str(input(draw_down))

    print(score)
    print(count)
    print(response)

    # question 4 - risk appetite
    risk = """
    Inflation can reduce your spending power. 
    How much risk are you prepared to take to counteract
    the effects of inflation?

    A. I am comfortable with short to medium term losses
    in order to beat inflation over the long term.

    B. I am conscious of the effects of inflation, and 
    am prepared to take moderate risks in order to stay 
    ahead of inflation.

    C. Inflation may erode my savings over the long-term,
    but I am only willing to take limited risks to attempt 
    to counter the effects of inflation.

    """

    risk_appetite = str(input(risk))
    risk_appetite = risk_appetite.upper()

    while count <= 3:
        if risk_appetite == "A":
            score += 1
            count += 1
            response.append(risk_appetite)
        elif risk_appetite == "B":
            score += 3
            count += 1
            response.append(risk_appetite)
        elif risk_appetite == "C":
            score += 5
            count += 1
            response.append(risk_appetite)
        else:
            risk_appetite = str(input(risk))

    print(score)
    print(count)
    print(response)

    # question 5 - emergency funds
    emergency = """
    How much money have you set aside
    (outside of your pension / Central Provident Fund
    savings) to handle emergencies? 

    A. More than six(6) months of living expenses.

    B. Between one(1) and six(6) months of living expenses.

    C. Less than one(1) month of living expenses.

    """

    emergency_funds = str(input(emergency))
    emergency_funds = emergency_funds.upper()

    while count <= 4:
        if emergency_funds == "A":
            score += 1
            count += 1
            response.append(emergency_funds)
        elif emergency_funds == "B":
            score += 3
            count += 1
            response.append(emergency_funds)
        elif emergency_funds == "C":
            score += 5
            count += 1
            response.append(emergency_funds)
        else:
            emergency_funds = str(input(emergency))

    print(score)
    print(count)
    print(response)

    # question 6 - asset mix

    asset = """
    You possess $100,000 and wish to invest the
    funds for the future. Which of the asset mixes would you
    choose to invest in?

    Investment A has a potential return of 30% but the
    possibility of losing up to 40% in any year.

    Investment B has a potential return of 3% with the 
    possibility of losing up to 5% in any year.

    A. 80% in Investment A and 20% in Investment B

    B. 50% in Investment A and 50% in Investment B

    C. 20% in Investment A and 80% in Investment B

    """

    asset_mix = str(input(asset))
    asset_mix = asset_mix.upper()

    while count <= 5:
        if asset_mix == "A":
            score += 1
            count += 1
            response.append(asset_mix)
        elif asset_mix == "B":
            score += 3
            count += 1
            response.append(asset_mix)
        elif asset_mix == "C":
            score += 5
            count += 1
            response.append(asset_mix)
        else:
            asset_mix = str(input(asset))

    # question 7 - expected returns

    expectation = """
    Over the long term, what returns do you reasonably 
    expect to achieve from your portfolio.?

    A. More than 9% per annum above the fixed deposit rate.

    B. 3% - 9% per annum above the fixed deposit rate.

    C. Less than 3% per annum above the fixed deposit rate.

    """

    expected_returns = str(input(expectation))
    expected_returns = expected_returns.upper()

    while count <= 6:
        if expected_returns == "A":
            score += 1
            count += 1
            response.append(expected_returns)
        elif expected_returns == "B":
            score += 3
            count += 1
            response.append(expected_returns)
        elif expected_returns == "C":
            score += 5
            count += 1
            response.append(expected_returns)
        else:
            expected_returns = str(input(expectation))

    # question 8 - downside risk tolerance

    downside = """
    Most investments can fluctuate both up and down 
    (i.e volatility). 
    How much could your investment fall in value over 
    a 12 months period before you begin to feel 
    concerned and anxious?

    A. More than 25%.

    B. Up to 25%.

    C. Up to 5%.

    """

    downside_risk_tolerance = str(input(downside))
    downside_risk_tolerance = downside_risk_tolerance.upper()

    while count <= 7:
        if downside_risk_tolerance == "A":
            score += 1
            count += 1
            response.append(downside_risk_tolerance)
        elif downside_risk_tolerance == "B":
            score += 3
            count += 1
            response.append(downside_risk_tolerance)
        elif downside_risk_tolerance == "C":
            score += 5
            count += 1
            response.append(downside_risk_tolerance)
        else:
            downside_risk_tolerance = str(input(downside))

    # question 9 - loss tolerance

    loss = """
    What would your reaction be if six months 
    after placing your investment you discover that your
    portfolio had decreased in value by 20%?

    A. I would invest more funds to lower my average 
    investment price, expecting future growth.

    B. This was a calculated risk and I would leave
    the investment in place, expecting future growth.

    C. I would cut my losses.

    """

    loss_tolerance = str(input(loss))
    loss_tolerance = loss_tolerance.upper()

    while count <= 8:
        if loss_tolerance == "A":
            score += 1
            count += 1
            response.append(loss_tolerance)
        elif loss_tolerance == "B":
            score += 3
            count += 1
            response.append(loss_tolerance)
        elif loss_tolerance == "C":
            score += 5
            count += 1
            response.append(loss_tolerance)
        else:
            loss_tolerance = str(input(loss))

    # question 10 - capital preservation

    capital = """
    To what extent are you concerned about preservation 
    of your capital?

    A. A high degree of risk would be acceptable given
    long term capital growth objectives.

    B. A moderate degree of risk would be acceptable given
    the potential for increased returns.

    C. A minimal degree of risk would be acceptable for 
    a slight increase in potential returns.

    """

    capital_presevation = str(input(capital))
    capital_presevation = capital_presevation.upper()

    while count <= 9:
        if capital_presevation == "A":
            score += 1
            count += 1
            response.append(capital_presevation)
        elif capital_presevation == "B":
            score += 3
            count += 1
            response.append(capital_presevation)
        elif capital_presevation == "C":
            score += 5
            count += 1
            response.append(capital_presevation)
        else:
            capital_presevation = str(input(capital))

    # question 11 - income requirements

    income = """What are your current income requirements
    from your investments?

    A. I require a small amount of investment income 
    as I am mainly focused on capital growth.

    B. I require an equal combination of investment 
    income and capital growth.

    C. I require substantial investment income with only
    some capital growth. 

    """

    income_requirement = str(input(income))
    income_requirement = income_requirement.upper()

    while count <= 10:
        if income_requirement == "A":
            score += 1
            count += 1
            response.append(income_requirement)
        elif income_requirement == "B":
            score += 3
            count += 1
            response.append(income_requirement)
        elif income_requirement == "C":
            score += 5
            count += 1
            response.append(income_requirement)
        else:
            income_requirement = str(input(income))


    aggressive = """ 
    You are categorised as an Aggressive investor.
    An Aggressive investor is prepared to accept higher 
    risk in order to obtain greater investment returns
    with a potential to lose all or more of his capital.
    An Aggressive investor is comfortable with investments
    that are more volatile and bear a higher risk of loss
    of capital. An Aggresive investor has a high appetite 
    for speculative trading.
    """

    balanced = """
    A Balanced investor seeks a mixture of capital growth 
    and regular income from his investments. A Balanced 
    investor is therefore prepared to accept moderate amounts 
    of risks to earn moderate potential returns. A Balanced
    investor accepts that there ois a real potential to lose
    at least part of his capital in seeking moderate returns.
    A  Balanced investor appreciates that there will be, 
    even in times of stability, occasional periods of volatility
    and risk of loss of capital. A Balanced investor may engage 
    in speculative trading from time to time and particularly
    accepts that when times are uncertain, trading is more
    likely to be regarded as more inherently speculative.
    """

    conservative = """
    A Conservative investor seeks primarily capital preservation.
    A Conservative Investor seeks principally a safe and regular 
    income as a priority over capital growth. A Conservative 
    investor should seriously consider whether he should be putting
    his money in investments other than in fixed deposit.
    """
    if score <= 30:
        print(aggressive)
    elif score >30 and score <= 47:
        print(balanced)
    elif score > 48:
        print(conservative)

    return response


def confirm():
    confirmation = input("Do you think that the description accurately describes you? Yes/No")

    while confirmation == "No":
        risk()




#y = risk()
#print(y)


""" for creating new accounts/login
x = get_credentials()
print(x[0])
user_account = {'123':'456'}

for creating new account, check username
if x[0] not in user_account.keys():
    user_account[x[0]] = x[1]
elif x[0] in user_account.keys():
    print('The username is taken ')



def response_dict():
    #tag response to user account with dictionary
    user_response = {}
    user_response['123'] = risk()
    print(user_response)

    #create CSV file to store user responses
    #problem: all responses stored in 1 cell

    with open("data.csv", "w", newline="") as data:
        writer = csv.writer(data)
        for key, response in user_response.items():
            writer.writerows(key, [response])
"""

def response_list():
    #store user input using list
    #benefits: each response stored in different column
    #to do: add user data into list before adding in csv

    response = risk_questionnaire()

    with open("data.csv", "a", newline="") as data:
        writer = csv.writer(data)
        writer.writerows([response])

"""
def change_response(): #WIP figure out if its possible to edit specific row
    marked_item = "B" #get user id from login
    with open("data.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')

        lines = []
        for line in reader:
            if line[1] == marked_item:
                lines = risk()

    with open("data.csv", "w", newline='') as data:
        writer = csv.writer(data, delimiter=",")
        writer.writerows([lines])


a = change_response()
"""




change dict to dataframe



#tag to user
#dictionary to change response if they want to
