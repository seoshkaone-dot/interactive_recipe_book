while True:
    print('Какой рецепт вы хотите посчитать?')
    print('1 - люля-кебаб', '2 - котлеты куринные', '3 - шницель', '4 - рыбные котлеты', '5 - тефтели', '6 - льезон', sep='\n')
    index_recipe = int(input('Введите индекс рецепта - '))
    total_weight = 0
    if index_recipe == 1:
        kebab = {'филе куринное':10000, 'сало':3000, 'соль':100, 'лук':3000, 'хлеб':350}
        print(*kebab.keys(), sep='\n')
        s = input('По какому ингредиенту нужно посчитать - ')
        n = float(input('Введите на сколько кг расчитать - ')) / (kebab[s] / 1000)
        for i in kebab:
            weight_i = int(kebab[i] * n)
            total_weight += weight_i
            print(i, '-', str(weight_i) + 'г')
    elif index_recipe == 2:
        chicken_cutlet = {'филе куриное':10000, 'сало':3000, 'соль':100, 'лук':1500, 'хлеб':1400, 'вода':1200}
        print(*chicken_cutlet.keys(), sep='\n')
        s = input('По какому ингредиенту нужно посчитать - ')
        n = float(input('Введите на сколько кг расчитать - ')) / (chicken_cutlet[s] / 1000)
        for i in chicken_cutlet:
            weight_i = int(chicken_cutlet[i] * n)
            total_weight += weight_i
            print(i, '-', str(int(weight_i)) + 'г')
    elif index_recipe == 3:
        schnitzel = {'свинина':3000, 'филе куриное':7000, 'сало':3000, 'соль':100, 'чеснок':50, 'лук':1500, 'хлеб':1400, 'вода':700}
        print(*schnitzel.keys(), sep='\n')
        s = input('По какому ингредиенту нужно посчитать - ')
        n = float(input('Введите на сколько кг расчитать - ')) / (schnitzel[s] / 1000)
        for i in schnitzel:
            weight_i = int(schnitzel[i] * n)
            total_weight += weight_i
            print(i, '-', str(int(weight_i)) + 'г')
    elif index_recipe == 4:
        fish_cutlet = {'рыба':5000, 'филе куринное':5000, 'сало':2500, 'соль':100, 'лук':2500, 'хлеб':1050}
        print(*fish_cutlet.keys(), sep='\n')
        s = input('По какому ингредиенту нужно посчитать - ')
        n = float(input('Введите на сколько кг расчитать - ')) / (fish_cutlet[s] / 1000)
        for i in fish_cutlet:
            weight_i = int(fish_cutlet[i] * n)
            total_weight += weight_i
            print(i, '-', str(int(weight_i)) + 'г')
    elif index_recipe == 5:
        meatballs = {'филе куринное':3000, 'сало':800, 'соль':30, 'лук':800, 'рис':900}
        print(*meatballs.keys(), sep='\n')
        s = input('По какому ингредиенту нужно посчитать - ')
        n = float(input('Введите на сколько кг расчитать - ')) / (meatballs[s] / 1000)
        for i in meatballs:
            weight_i = int(meatballs[i] * n)
            total_weight += weight_i
            print(i, '-', str(int(weight_i)) + 'г')
    elif index_recipe == 6:
        liezon = {'соль':35, 'вода':3800, 'мука':2340}
        n = float(input('Введите сколько отбивных у вас в наличии - ')) / 150
        total_weight = 0
        for i in liezon:
            weight_i = int(liezon[i] * n)
            total_weight += weight_i
            if i == 'вода':
                print('молоко - 800г')
                print(i, '-', str(weight_i - 800) + 'г')
            else:
                print(i, '-', str(weight_i) + 'г')
    else:
        print()
        print('По-моему вы что-то перепутали, проверьте индекс.')
        print()
        continue
    print('Общий вес - ', str(total_weight) + 'г')
    print()
