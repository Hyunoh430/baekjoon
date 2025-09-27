# ======== 배열 회전 =========
def clock_wise(arr):
    return list(zip(*arr[::-1]))
def not_clock_wise(arr):
    return list(zip(*arr))[::-1]


# ========== 순열 (Permutation) ==========
def permutation(arr, r):
    result = []
    used = [False] * len(arr)
    def backtrack(current, used):
        if len(current) == r:
            result.append(current[:])
            return
        for i in range(len(arr)):
            if not used[i]:
                used[i] = True
                current.append(arr[i])
                backtrack(current, used)
                current.pop()
                used[i] = False
    backtrack([], used)
    return result


# ========== 조합 (Combination) ==========
def combination(arr, r):
    result = []

    def backtrack(start, current):
        if len(current) == r:
            result.append(current[:])
        for i in range(start,len(arr)):
            current.append(arr[i])
            backtrack(start + 1, current)
            current.pop()
    backtrack(0,[])
    return result


# ========== 테스트 ==========
if __name__ == "__main__":
    arr = [1, 2, 3, 4]

    print("배열:", arr)
    print()

    print("=== 순열 P(4,2) ===")
    perm_result = permutation(arr, 2)
    print(f"결과: {perm_result}")
    print(f"개수: {len(perm_result)}개")
    print()

    print("=== 조합 C(4,2) ===")
    comb_result = combination(arr, 2)
    print(f"결과: {comb_result}")
    print(f"개수: {len(comb_result)}개")
    print()

    print("=== 차이점 확인 ===")
    print("순열에는 [1,2]와 [2,1]이 둘 다 있음")
    print("조합에는 [1,2]만 있음 (순서 상관없어서)")