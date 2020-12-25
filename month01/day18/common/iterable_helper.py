class IterableHelper:
    @staticmethod
    def accumulate(iterator,func_accumulate):
        """
        在可迭代对象中搜索满足条件的元素
        :param iterator: 需要搜索可迭代对象
        :param func_accumulate: 搜索类型，搜索条件
        :return: 生成器，可以推算出满足条件的数据
        """
        count = 0
        for item in iterator:
            count+=func_accumulate(item)
        return count
    @staticmethod
    def find_all(iterable, func_condition):
        """
        在可迭代对象中搜索满足条件的元素
        :param iterable: 需要搜索可迭代对象
        :param func_condition: 搜索类型，搜索条件
        :return: 生成器，可以推算出满足条件的数据
        """
        for item in iterable:
            yield func_condition(item)
    @staticmethod
    def remove_all(iterable,fun_condition):
        count=0
        for item in iterable[::-1]:
            if fun_condition(item):
                iterable.remove(item)
                count+=1
        return count
    @staticmethod
    def find_most(iterable,fun_condition):
        most_big=iterable[0]
        for i in range(1,len(iterable)):
            if fun_condition(most_big) < fun_condition(iterable[i]):
                most_big=iterable[i]
        return most_big
    @staticmethod
    def ascending(iterable,fun_condition):
        for i in range(len(iterable)-1):
            for c in range(i+1,len(iterable)):
                if fun_condition(iterable[i])>fun_condition(iterable[c]):
                    iterable[i],iterable[c]=iterable[c],iterable[i]

