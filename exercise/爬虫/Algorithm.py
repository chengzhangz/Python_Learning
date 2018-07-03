import random

# 实现冒泡排序
class Bubble(object):
    # 初始化一个list
    def __init__(self):
        self.unsort_list = []
        for i in range(10):
            item_list = 50 * random.random()
            self.unsort_list.append(int(item_list))
        print("排序初始化：")
        print(self.unsort_list)

    def process_sort(self):
        for i in range(len(self.unsort_list)):
            for j in range(len(self.unsort_list) - i - 1):
                if self.unsort_list[j] > self.unsort_list[j + 1]:
                    self.unsort_list[j + 1], self.unsort_list[j] = self.unsort_list[j], self.unsort_list[j + 1]
        print("排序结束：")
        print(self.unsort_list)


def main():
    # 冒泡排序
    my_list = Bubble()
    my_list.process_sort()


if __name__ == "__main__":
    main()