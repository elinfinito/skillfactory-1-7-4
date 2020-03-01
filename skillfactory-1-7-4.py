if __name__ == "__main__":
    
    text = 'Название языка питон произошло вовсе не от вида пресмыкающихся. Автор назвал язык в честь популярного британского комедийного телешоу 1970-х Летающий цирк Монти Пайтона'
    text = text.split()
    print(text)
    print("")
    words_to_find = ['питон', 'Монти', 'проверка', 'честь', 'шоу', 'драма']
    print(words_to_find)

    print("")

    result1 = set() #преображаем в Множество. result - это контейнер, у него есть метод add, который кладет значение
    #множество это как массив уникальных значений
    #на каждом шаге туда будет добавляться элемент, если условие истинно
    #потом принтом мы выводим все что там накопилось
    #программы = алгоритмы + структуры данных

    for i in text:
        if i in words_to_find:
            result1.add(i) #result - это контейнер, у него есть метод add, который кладет значение
        else:
            continue
    result1 = sorted(result1)  # чтоб потом отсортироватб/упорядочить по алфавиту
    print('Следующие слова содержатся в списке: "{}"' .format(result1))

    print("")
    # или проще в рамках пройденного материала
    for i in text:
        if i in words_to_find:
            print('Слово содержится в списке:  "{}" '.format(i))

    print("")

    text = 'Название языка питон произошло вовсе не от вида пресмыкающихся. Автор назвал язык в честь популярного британского комедийного телешоу 1970-х Летающий цирк Монти Пайтона'
    words_to_find = ['питон', 'Монти', 'проверка', 'честь', 'шоу', 'драма']

    result1 = set() #сделали множество
    for i in words_to_find:
        if text.find(i) >= 0: #при .find
            result1.add(i)

    print('Следующие слова содержатся в списке: "{}"'.format(result1))

    result1 = set()

    for i in words_to_find:
        l = text.find(i)
        if l >= 0:
            result1.add(i)
    result1 = list(result1)

    print('Следующие слова содержатся в списке: "{}"' .format(', '.join(result1)))

    print("")

def is_word_present_in_text_fuzzy_search(word, text):
    return text.find(word) >= 0


def main():
    text = 'Название языка питон произошло вовсе не от вида пресмыкающихся. Автор назвал язык в честь популярного британского комедийного телешоу 1970-х Летающий цирк Монти Пайтона'
    words_to_find = ['питон', 'Монти', 'проверка', 'честь', 'шоу', 'драма']
    print("")

    result1 = set()

    for i in words_to_find:
        if is_word_present_in_text_fuzzy_search(i, text):
            result1.add(i)

    result1 = sorted(result1)
    print('Следующие слова содержатся в списке: "{}"'.format(result1))


if __name__ == '__main__':
    main()
