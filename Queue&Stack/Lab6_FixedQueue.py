# 고정 길이 큐 클래스

from typing import Any

class Lab6_FixedQueue:

    def __init__(self, capacity: int) -> None:
        """ Queue Reset """
        self.num = 0                    ## 현재 데이터 개수
        self.front = 0                  ## 맨 앞 원소 인덱스
        self.rear = 0                   ## 다음 Enque 위치
        self.capacity = capacity        ## 구역 크기
        self.queue = [None] * capacity  ## 큐 객체


    def __len__(self) -> int :
        """ 큐에 있는 모든 데이터 개수 반환 """
        return self.num


    def is_Empty(self) -> bool :
        """ 큐가 공백 상태인지 점검 """
        return self.num <= 0


    def is_Full(self) -> bool :
        """ 큐가 포화 상태인지 점검 """
        return self.num >= self.capacity


    def enque(self, x: Any) -> None :
        """ 데이터 x를 인큐 """
        if (self.is_Full()) :   ## 큐가 포화 상태라면,
            raise FixedQueue.Full()

        self.queue[self.rear] = x
        self.rear += 1
        self.num += 1

        if (self.rear == self.capacity) :
            self.rear = 0


    def deque(self) -> Any :
        """ 데이터 디큐 """
        if (self.is_Empty()) :  ## 큐가 공백 상태라면,
            raise FixedQueue.Empty()

        x = self.queue[self.front]
        self.front += 1
        self.num -= 1

        if (self.front == self.capacity) :
            self.front = 0

        return x


    def pick(self) -> Any :
        """ 큐에서 데이터 피크(맨 앞 데이터를 반환) """
        if (self.is_Empty()) :
            raise FixedQueue.Empty()

        return self.queue[self.front]


    def find(self, value: Any) -> Any :
        """ 큐에서 value를 찾아 인덱스를 반환(없으면 -1) """
        for i in range(self.num) :
            idx = (i + self.front) % self.capacity
            if (self.queue[idx] == value) :
                return idx
        return -1


    def count(self, value: Any) -> bool :
        """ 큐에 있는 value 개수 반환 """
        c = 0
        for i in range(self.num) :
            idx = (i + self.front) % self.capacity

            if (self.queue[idx] == value) :
                c += 1

        return c


    def __contains__(self, value: Any) -> bool :
        """ 큐에 value가 있는지 검사 """
        return self.count(value)


    def clear(self) -> None :
        """ 큐 초기화 """
        self.num = self.front = self.rear = 0


    def dump(self) -> None :
        """ 모든 데이터를 맨 앞부터 맨 끝 순으로 출력 """
        if (self.is_Empty()) :
            print("큐가 비었습니다.")
        else :
            for i in range(self.num) :
                print(self.queue[(i + self.front) % self.capacity], end="")
            print()


    class Empty(Exception) :
        """ 공백 FixedQueue에서 Dequeue() 또는 Pick()를 호출할 때 내보내는 예외 처리 """
        pass


    class Full(Exception) :
        """ 포화 FixedQueue에서 Inqueue()를 호출할 때 내보내는 예외 처리 """
        pass