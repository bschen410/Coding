from math import ceil

def cal(book):
    for i in range(len(book)):
        if 1 <= book[i]['amount'] <= 10:
            book[i]['total'] = ceil(book[i]['prize'] * book[i]['amount'])
        elif 11 <= book[i]['amount'] <= 20:
            book[i]['total'] = ceil(book[i]['prize'] * book[i]['amount'] * book[i]['d1'] / 100)
        elif 21 <= book[i]['amount'] <= 30:
            book[i]['total'] = ceil(book[i]['prize'] * book[i]['amount'] * book[i]['d2'] / 100)
        elif 31 <= book[i]['amount']:
            book[i]['total'] = ceil(book[i]['prize'] * book[i]['amount'] * book[i]['d3'] / 100)
    return book

def main():
    book = list()
    prize_list = [380, 1200, 180]
    book_list = ['A', 'B', 'C']
    for i in range(3):
        str = input().split(',')
        temp = {'amount': int(str[0]), 'd1': int(str[1]), 'd2': int(str[2]), 'd3': int(str[3]),
                'prize': prize_list[i], 'product': book_list[i]}
        book.append(temp)
    #
    book = cal(book)
    book = sorted(book, key=lambda x: x['total'], reverse=True)
    for i in book:
        print(i['product'], i['total'], sep = ',')
    print(sum(i['total'] for i in book))

if __name__ == '__main__':
    main()
