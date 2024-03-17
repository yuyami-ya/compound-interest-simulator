import datetime
from typing import List, Tuple
from dateutil.relativedelta import relativedelta
from common import const

def calculate(
) -> Tuple[List]:
    # 元金
    initial_savings = 0
    # 初期費用
    first_installment = 0
    # 年率
    annual_increase_percent = 7
    # 月の積立金額
    installment_per_month = 30
    # 積立期間
    installment_term = 30
    # スタート年月
    begin_month = datetime.datetime.now()
    # 欲しい年の期間 (〇ヵ月入力)
    output_period_month = 50

    # 出力予定の年月
    year_month_list = []
    for i in range(output_period_month):
        # dt1 + 〇ヵ月
        this_month = begin_month + relativedelta(months=i)
        # 2024/1 の形式で出力
        this_month_output = f"{this_month.year}/{this_month.month}"
        year_month_list.append(this_month_output)


    # 元金
    pay_list = []
    for elem in range(output_period_month):
        # install
        if elem < installment_term:
            # 今月までの元金(=前月までの元金 + 今月の掛け金)
            if pay_list == []:
                pay_list.append(installment_per_month)
            else:
                pay_list.append(pay_list[-1] + installment_per_month)
        # not install anymore
        else:
            pay_list.append(pay_list[-1])

    # 評価額
    amount_appraised_list = []
    # 毎月の増加率 7% の場合, 毎月 1.005833333 % 増加する
    increase_rate = annual_increase_percent/100/12 + 1
    for index in range(output_period_month):
        pay_this_month = pay_list[index] 
        if amount_appraised_list == []:
            amount_appraised_list.append(pay_this_month)
        else:
            appraised_this_month = (amount_appraised_list[index-1] * increase_rate) + installment_per_month
            amount_appraised_list.append(
                appraised_this_month
            )

    # 増加額
    increase_amount_list = []
    for num in range(output_period_month):
        if increase_amount_list == []:
            increase_amount_list.append(amount_appraised_list[num])
        else:
            increase_amount_list.append(amount_appraised_list[num] - increase_amount_list[num-1])

    return (
        year_month_list,
        pay_list,
        amount_appraised_list,
        increase_amount_list
    )
