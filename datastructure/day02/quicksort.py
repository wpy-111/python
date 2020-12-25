"""
    快速排序
"""
def quick_sort(li,first,last):
    if first >= last:
        return
    pos = part(first,last,li)
    quick_sort(li,first,pos-1)
    quick_sort(li,pos+1,last)

def part(first, last, li):
    lcursor = first + 1
    rcursor = last
    while True:
        while lcursor <= rcursor and li[lcursor] <= li[first]:
            lcursor += 1
        while lcursor <= rcursor and li[rcursor] >= li[first]:
            rcursor -= 1
        if lcursor > rcursor:
            li[first],li[rcursor] = li[rcursor],li[first]
            break
        else:
            li[lcursor],li[rcursor] = li[rcursor],li[lcursor]
    return rcursor
if __name__ == '__main__':
    li = [12, 8, 3, 5, 4, 6, 7, 2, 88]
    quick_sort(li,0,len(li)-1)
    print(li)

