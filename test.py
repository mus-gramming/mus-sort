from random import shuffle
import time
from mus_sort import mus_sort

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