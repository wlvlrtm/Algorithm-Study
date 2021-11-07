def hanoi_move(n, x, y) :
    """ n: 이동 원반 수
        x: 시작 기둥
        y: 목표 기둥
    """

    if (n > 1) :
        hanoi_move(n-1, x, 6-x-y)

    print(f"원반 [{n}]을(를) {x} 기둥에서 {y} 기둥으로 옮겼습니다.")

    if (n > 1) :
        hanoi_move(n-1, 6-x-y, y)

hanoi_move(3, 1, 3)