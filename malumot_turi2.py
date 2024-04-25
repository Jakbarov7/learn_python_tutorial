import numpy as np
# Array yaratayotganimizda , uning malumot turini aniq qilib berish
# arr = np.array([1, 2, 3, 4], dtype=np.float64)
.dtype - arrayimiz qaysi ma'lumot turida ekanligini aniqlab beradi
print(arr.dtype)
print(arr)

# Bir ma'lumot turidan boshqasiga o'tish
arr = np.array([1, 2, 3, 4]) # dtype = int64
float_arr = arr.astype(np.float64)
print(float_arr.dtype)

