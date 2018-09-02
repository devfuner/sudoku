from random import randrange
from random import sample

"""
이 프로그램을 스도쿠를 만들기전 기본 개념을 파악하기 위한 용도이다.

  1 | 2 | 3
  - + - + -
  2 | 3 | 1
  - + - + -
  3 | 1 | 2
  
  위의 보드형식을 기준으로 한다.
  각각의 행과 열은 1,2,3의 숫자를 하나씩만 가져야한다.
  
"""
board = []


def new_board():
    """
    새로운 보드를 생성한다.
    :return: board
    """
    return sample(range(1, 4), 3) + sample(range(1, 4), 3) + sample(range(1, 4), 3)


def validation(*index):
    """
    선택된 행열이 1,2,3의 값을 하나씩만 가지고 있는지 체크
    :param index: 행열의 인덱스 리스트
    :return: 추출한 set과 valid_set의 비교 값
    """
    valid_set = {1, 2, 3}
    letter = set()
    for x in index:
        letter.add(board[x])

    return letter == valid_set


def validate():
    """
    각각의 행열을 확인
    :return:
    """

    if not validation(0, 1, 2):
        return False

    if not validation(3, 4, 5):
        return False

    if not validation(6, 7, 8):
        return False

    if not validation(0, 3, 6):
        return False

    if not validation(1, 4, 7):
        return False

    if not validation(2, 5, 8):
        return False

    return True


def set_3_empty():
    """
    빈칸 생성
    :return:
    """
    for i in sample(range(0, 9), 3):
        board[i] = " "


def answer():
    """
    빈칸에 들어갈 값을 찾는 함수
    :return:
    """
    emptys = [i for i, x in enumerate(board) if x == " "]
    print(emptys)

    while True:
        for i in emptys:
            board[i] = randrange(1, 4)

        if validate():
            break


def game_start():
    global board

    board = new_board()

    while not validate():
        board = new_board()

    print("답 >", board)

    set_3_empty()
    print("문제 >", board)

    answer()
    print("정답 >", board)


if __name__ == '__main__':
    game_start()
