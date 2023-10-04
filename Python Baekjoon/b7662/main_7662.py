## 이중 우선순위 큐
import sys
import heapq

def isEmpty(nums) :
    for i in nums :
        if (i[1] > 0) : ## 비어 있지 않음; dict()에 값이 존재
            return False
    return True         ## 비어 있음; dict()에 값이 없음


def main() :
    t = int(sys.stdin.readline().strip())

    for i in range(t) :
        min_heap = []
        max_heap = []
        nums = dict()

        k = int(sys.stdin.readline())

        for j in range(k) :
            chk, n = sys.stdin.readline().split()
            n = int(n)

            if (chk == 'I') :   ## 값 삽입
                if (n in nums) :    ## 중복
                    nums[n] += 1
                else :              ## 신규
                    nums[n] = 1

                    heapq.heappush(min_heap, n)
                    heapq.heappush(max_heap, -n)
            elif (chk == 'D') :   ## 값 삭제
                if not (isEmpty(nums.items())) :  ## dict()가 비어 있지 않음
                    if (n == 1) : ## 최대값 삭제
                        while (-max_heap[0] not in nums or nums[-max_heap[0]] < 1) :    ## 중복되는 값 삭제
                            temp = -heapq.heappop(max_heap) ## temp = 중복된 값

                            if (temp in nums) : ## 중복된 값(temp)가 dict()에 있는지 검사
                                del (nums[temp])    ## dict()에서 해당 값(중복된 값) 삭제

                        nums[-max_heap[0]] -= 1 ## 값 카운트 업데이트
                    else :  # 최소값 삭제
                        while (min_heap[0] not in nums or nums[min_heap[0]] < 1) :  ## 중복되는 값 삭제
                            temp = heapq.heappop(min_heap)  ## temp = 중복된 값
                            if (temp in nums) : ## 중복된 값(temp)가 dict()에 있는지 검사
                                del (nums[temp])    ## dict()에서 해당 값(중복된 값) 삭제

                        nums[min_heap[0]] -= 1  ## 값 카운트 업데이트

        # 결과 출력
        if (isEmpty(nums.items())) :
            print("EMPTY")
        else :
            while (min_heap[0] not in nums or nums[min_heap[0]] < 1) :
                heapq.heappop(min_heap)

            while (-max_heap[0] not in nums or nums[-max_heap[0]] < 1) :
                heapq.heappop(max_heap)

            print(-max_heap[0], min_heap[0])



if (__name__ == "__main__") :
    main()