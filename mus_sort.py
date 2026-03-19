import gc 
import math 
from functools import lru_cache


@lru_cache(maxsize=128)
def get_dynamic_threshold(length):
    return (1 + math.sqrt(5)) / 2 - (1 / (length + 1))


def delete_arr(arr):
    if not arr: 
        return [], []
    
    current = arr[0]
    kept = [current]
    deleted = []

    for i in range(1, len(arr)):
        val = arr[i]
        if val >= current:
            kept.append(val)
            current = val
        else:
            deleted.append(val)
    
    return kept, deleted


def delete_arr_unclockwise(arr):
    if not arr: 
        return [], []
    
    current = arr[-1]
    kept = [current]
    deleted = []

    for i in range(len(arr) - 2, -1, -1):
        val = arr[i]
        if val >= current:
            kept.append(val)
            current = val
        else:
            deleted.append(val)
    
    return kept, deleted


def choosing_inner_arr(arr):
    PHI = get_dynamic_threshold(len(arr))

    # Thử chiều xuôi
    k_cw, d_cw = delete_arr(arr)
    if not d_cw: 
        return k_cw, d_cw
    ratio_cw = len(k_cw) / len(d_cw)
    if ratio_cw >= PHI - 1e-4:
        return k_cw, d_cw

    # Thử chiều ngược
    k_ucw, d_ucw = delete_arr_unclockwise(arr)
    if not d_ucw: 
        return k_ucw, d_ucw
    
    ratio_ucw = len(k_ucw) / len(d_ucw)
    if ratio_ucw >= PHI - 1e-4:
        return k_ucw, d_ucw
    
    if ratio_cw >= ratio_ucw:
        return k_cw, d_cw
    else:
        return k_ucw, d_ucw


def splitting(arr):
    if len(arr) == 1:
        return arr 
    kept, deleted = choosing_inner_arr(arr)
    result = [kept]
    while deleted:
        inner_kept, inner_deleted = choosing_inner_arr(deleted)
        result.append(inner_kept)
        deleted = inner_deleted

    if deleted:
        result.append(deleted)
    return result
    

import heapq

def mus_sort(arr):
    runs = splitting(arr)
    return list(heapq.merge(*runs))



# ============================================ TEST ============================================
from random import shuffle
import time

POPULATION = [*range(-50000, 50000)]
shuffle(POPULATION)
arr = POPULATION
start_time = time.time()
sorted_arr = mus_sort(arr)
end_time = time.time()

print(f"Thời gian xử lý 100,000 dòng: {end_time - start_time:.4f} giây")



def verify_sorting(original_arr, mus_sorted_arr):
    assert len(original_arr) == len(mus_sorted_arr), "Lỗi: Mất dữ liệu!"
    assert mus_sorted_arr == sorted(original_arr), "Lỗi: Sắp xếp sai thứ tự!"
    
    print("✅ Chúc mừng Mus: Thuật toán chuẩn xác 100%!")

# Sử dụng trong code của Mus:
verify_sorting(arr, sorted_arr)