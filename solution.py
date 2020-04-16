import xml.etree.ElementTree as et

id = {}
isbn = {}
year = {}
avcost = {}

tree = et.parse('books.xml')
root = tree.getroot()

for child in root:
    id[str(child.attrib.get('id'))] = []
    isbn[child[1].text] = []
    isbn[child[1].text].append('id')
    isbn[child[1].text].append(child.attrib.get('id'))

    for char in range(len(child)):
        id[str(child.attrib.get('id'))].append(child[char].tag)
        id[str(child.attrib.get('id'))].append(child[char].text)
        if char!=1:
            isbn[child[1].text].append(child[char].tag)
            isbn[child[1].text].append(child[char].text)
    if child[6].text not in year.keys():
        year[child[6].text] = 1
    elif child[6].text in year.keys():
        year[child[6].text] += 1

    if child[4].text not in avcost.keys():
        avcost[child[4].text] = [float(child[8].text)]
    elif child[4].text in avcost.keys():
        avcost[child[4].text].append(float(child[8].text))

def vyvodisbn(isbn):
    strisbn = input('Введите ISBN: ')
    sp = isbn.get(strisbn)
    for i in range(int(len(sp) / 2)):
        print(sp[2 * i], '-', sp[2 * i + 1])

def vyvodid(id,i):
    if i==0:
        strid = input('Введите id книги: ')
        sp = id.get(strid)
        for i in range(int(len(sp)/2)):
            print(sp[2*i], '-', sp[2*i+1])
    else:
        strid = str(i)
        sp = id.get(strid)
        for i in range(int(len(sp) / 2)):
            print(sp[2 * i], '-', sp[2 * i + 1])

def vyvodyear(year):
    stryear = input('Введите год: ')
    print(year.get(stryear))

def vyvodavcost(avcost):
    keys = list(avcost.keys())
    for i in range(len(keys)):
        av = sum(avcost.get(keys[i])) / len(avcost.get(keys[i]))
        print(keys[i], '-', int(av))

def maxcost(root,id):
    year = input('Введите год издания: ')
    pub = input('Введите издательство: ')
    ma = 0
    newid = []
    for child in root:
        if child[6].text == year and child[4].text == pub:
            if float(child[8].text) > ma:
                newid = [str(child.attrib.get('id'))]
                ma = float(child[8].text)
            elif float(child[8].text) == ma:
                newid.append(str(child.attrib.get('id')))
    for i in newid:
        vyvodid(id, i)

def main():
    while True:
        choice = int(input('\n1. Вывести полную информацию по id книги.\n'
                           '2. Вывести полную информацию о книге по ISBN.\n'
                           '3. Подсчитать количество книг по заданному году издания.\n'
                           '4. Подсчитать среднюю стоимость книг по каждому издательству.\n'
                           '5. Вывести информацию о самой дорогой книге(ах) по заданным издательству и году издания. '))
        if choice == 1:
            vyvodid(id, 0)
        elif choice == 2:
            vyvodisbn(isbn)
        elif choice == 3:
            vyvodyear(year)
        elif choice == 4:
            vyvodavcost(avcost)
        elif choice == 5:
            maxcost(root,id)

main()

