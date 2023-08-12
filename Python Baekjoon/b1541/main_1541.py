## 잃어버린 괄호
import sys

def main() :
    exp = sys.stdin.readline().split('-')
    nums = list()

    for i in exp :
        temp = i.split('+')
        temp_sum = 0

        for j in temp :
            temp_sum += int(j)

        nums.append(temp_sum)

    r = nums[0]

    for k in range(1, len(nums)) :
        r -= nums[k]

    print(r)



if (__name__ == "__main__") :
    main()