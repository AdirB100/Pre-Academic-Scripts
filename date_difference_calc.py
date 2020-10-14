def calc_def_date():
    print('Date Calculator')
    date1 = input('From: ')
    date2 = input('Till: ')
    # input clearance
    date1 = date1.replace('.', '/')
    date2 = date2.replace('.', '/')
    if date1[1] == '/':
        date1 = '0' + date1
    if date2[1] == '/':
        date2 = '0' + date2
    if date1[4] == '/':
        date1 = date1[:3] + '0' + date1[3:]
    if date2[4] == '/':
        date2 = date2[:3] + '0' + date2[3:]
    try:
        date1[7]
    except IndexError:
        date1 = date1[:6] + '0' + date1[6:]
    try:
        date2[7]
    except IndexError:
        date2 = date2[:6] + '0' + date2[6:]
    if len(date1) == 8:
        if int(date1[6] + date1[7]) < 30:
            date1 = date1[:6] + '20' + date1[6:]
        else:
            date1 = date1[:6] + '19' + date1[6:]
    if len(date2) == 8:
        if int(date2[6] + date2[7]) < 30:
            date2 = date2[:6] + '20' + date2[6:]
        else:
            date1 = date2[:6] + '19' + date2[6:]
    # basic constants
    month_days_regular = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    month_days_leap = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    day1 = int(date1[0] + date1[1])
    day2 = int(date2[0] + date2[1])
    mo1 = int(date1[3] + date1[4])
    mo2 = int(date2[3] + date2[4])
    ye1 = int(date1[6] + date1[7] + date1[8] + date1[9])
    ye2 = int(date2[6] + date2[7] + date2[8] + date2[9])
    if (ye1 % 4 == 0 and ye1 % 100 != 0) or (ye1 % 400 == 0):
        ye1_leap = 1
    else:
        ye1_leap = 0
    if (ye2 % 4 == 0 and ye2 % 100 != 0) or (ye2 % 400 == 0):
        ye2_leap = 1
    else:
        ye2_leap = 0
    def_ye = ye2 - ye1
    def_days = 0
    if def_ye != 0:
        def_mo = ((def_ye + 1) - 2) * 12 + (12 - mo1) + mo2 - 1
        cnt = 0  # counts the number of leap years
        for year in range(ye1 + 1, ye2):
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                cnt += 1
        if def_ye >= 2:
            def_days += 366 * cnt + 365 * ((def_ye + 1) - 2 - cnt)
        if ye1_leap == 1:
            for month in range(mo1 + 1, 13):
                def_days += month_days_leap[month]
            def_days += month_days_leap[mo1] - day1
        else:
            for month in range(mo1 + 1, 13):
                def_days += month_days_regular[month]
            def_days += month_days_regular[mo1] - day1
        if ye2_leap == 1:
            for month in range(1, mo2):
                def_days += month_days_leap[month]
        else:
            for month in range(1, mo2):
                def_days += month_days_regular[month]
        def_days += day2
    else:
        def_mo = mo2 - mo1
        if def_mo == 0:
            def_days = day2 - day1
        else:
            cnt2 = 0
            cnt3 = 0
            if ye1_leap == 1:
                for month in range(1, mo2):
                    cnt2 += month_days_leap[month]
                for month in range(1, mo1):
                    cnt3 += month_days_leap[month]
                def_days += cnt2 - cnt3 + day2 - day1
            else:
                for month in range(1, mo2):
                    cnt2 += month_days_regular[month]
                for month in range(1, mo1):
                    cnt3 += month_days_regular[month]
                def_days += cnt2 - cnt3 + day2 - day1
    def_weeks = def_days // 7
    ld = len(str(def_days))
    lw = len(str(def_weeks))
    lm = len(str(def_mo))
    ly = len(str(def_ye))
    print('''
''' + (10 + ld + 4) * '*' + f'''
   {def_days}  days
   {def_days // 7}''' + (ld - lw + 2) * ' ' + f'''weeks
   {def_mo}''' + (ld - lm + 2) * ' ' + f'''months
   {def_ye}''' + (ld - ly + 2) * ' ' + '''years
''' + (10 + ld + 4) * '*')


calc_def_date()