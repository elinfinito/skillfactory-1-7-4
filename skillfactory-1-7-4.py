text = 'Название языка питон произошло вовсе не от вида пресмыкающихся. Автор назвал язык в честь популярного британского комедийного телешоу 1970-х Летающий цирк Монти Пайтона'
    text = text.split()
    words_to_find = ['питон', 'Монти', 'проверка', 'честь', 'шоу', 'драма']
    print("")

    result = set() 

    for i in text:
        if i in words_to_find:
            result.add(i)
        else:
            continue
    result = sorted(result)  
    print('Следующие слова содержатся в списке: "{}"' .format(result))
