import numpy as np

arr = np.arange(24).reshape(2, 3, 4)
# print(arr)


swapped_arr = arr.swapaxes(0, 1)
print(swapped_arr)


# 1-usul
# arr = np.array([1, 2, 3, 4])
# print(arr)
# print(type(arr))

# 2-usul
# lst = [1, 2, 3, 4]
# arr1 = np.array(lst)
# print(arr1)
# print(type(arr1))

# 3-usul
# arr2 = np.arange(10)
# print(arr2)
# print(type(arr2))

# 4-usul
# arr3 = np.arange(1, 21, 3)
# print(arr3)
# print(type(arr3))

# ".ndim" --> arraylarning o'lchamini aniqlab beradi
# N1
# arr4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(arr4.ndim)

# N2
# arr5 = np.array([
#     [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
#     [[9, 10, 11], [12, 13, 14], [16, 17, 18]],
#     [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
# ])
# print(arr5)
# print(arr5.ndim)

# ".shape" --> arrayning qatorlar va ustunlar sonini tuple ko'rinishida qaytaradi (qator, ustun)
# arr6 = np.arange(1, 10).reshape(3, 3)
# print(arr6.size)
# print(arr6.shape)

# N2
# arr7 = np.arange(11, 23).reshape(4, 3)
# print(arr7.size) # elementlar sonini ko'rsatadi
# print(arr7.shape) # arrayning o'lchamini ko'rsatadi


# N3
# arr8 = np.random.rand(2, 4) # ustun , qator
# print(arr8)
# print(arr8.size) # elementlar soni
# print(arr8.shape) # ustun va qatorlar sonini


# "np.zeros()" barcha elementi 0 bo'lgan massiv yasab beradi
# arr9 = np.zeros((3, 4))
# print(arr9)
# print(arr9.size)
# print(arr9.shape)
# print(arr9.ndim)

# N2
# arr10 = np.zeros((4, 4), dtype='int16')
# print(arr10)
# print(arr10.ndim)
# print(arr10.size)
# print(arr10.shape)

# "np.ones()" barcha elementlari 1 bo'lgan massiv yaratb beradi
# arr11 = np.ones((4, 3), dtype='int16')
# print(arr11.ndim)
# print(arr11.size)
# print(arr11.shape)


# "arange" default
# arr12 = np.arange(12)
# print(arr12)
# print(arr12.ndim)
# print(arr12.size)
# print(arr12.shape)


# Ma'lumot turlari -> Boolean - true , false 
# arr13 = np.array([1, 2, 3, 4], dtype=np.float16)
# print(arr13.dtype)

# arr14 = np.arange(12, dtype=np.int16).reshape(3, 4)
# print(arr14)
# print(arr14.dtype)
# arr_re = arr14.astype(np.float16)
# print(arr_re)
# print(arr_re.dtype)
# print(arr14.dtype)



# create an array N1
# arr = np.array([1, 2, 3, 4])
# print(arr)
# print(type(arr))
# print(arr.ndim)
# print(arr.size)
# print(arr.shape)


# arr1 = [1, 2, 3, 4]
# arr_n = np.array(arr1)
# print(type(arr_n))
# print(arr_n)


# arr2 = np.arange(2, 21, 2).reshape(5, 2)
# print(arr2)
# print(type(arr2))
# print(arr2.size)
# print(arr2.ndim)
# print(arr2.shape)


# arr3 = np.random.rand(2, 4, 5) vaqt bo'lganda rand ni o'rganish
# print(arr3)
# print(arr3.ndim)
# print(arr3.size)
# print(arr3.shape)


# arr4 = np.random.randint(10, 20, 6).reshape(2, 3) 
# print(arr4)
# print(arr4.ndim)
# print(arr4.size)
# print(arr4.shape)

# arr = np.zeros(shape=(3, 4))
# print(arr)
# print(arr.ndim)
# print(arr.size)
# print(arr.shape)

# arr = np.ones((3, 4))
# print(arr)
# print(arr.ndim)
# print(arr.size)
# print(arr.shape)


# arr = np.array([1, 2, 3, 4, 5], dtype=np.int16)
# print(arr)
# print(arr.dtype)


# arr = np.random.rand(3, 4).astype(np.float16)
# print(arr)
# print(arr.dtype)


# arr = np.arange(10).reshape(2, 5).astype(np.float16)
# print(arr)
# print(arr.dtype)


# arr = np.arange(10, dtype=np.int16)
# print(arr.dtype)


# arr = np.arange(3, 35, 2)
# sliced_arr = arr[3:5].copy()
# sliced_arr[0] = -22
# sliced_arr[1] = -33
# print(arr)
# print(sliced_arr)


# 2D arrayda keslib olish 
# arr = np.arange(10).reshape(2, 5)
# print(arr)
# print(arr[:, 2]) # birinchi indexga qatorni (axis=1) 2-ga ustunni (axis=0)


# arr = np.arange(9, 18).reshape(3, 3)
# print(arr)
# print(arr[1:, 1:])


# Create a 1D array with 24 elements (4x3x2)
# arr = np.arange(24)
# arr_3d = arr.reshape(4, 3, 2)
# print(arr_3d[1, 1:, 1])


# Boolean indexing -> array elementlari true va falselardan tashkil topgan boladi
# names = ['Hasan', 'Husan', 'Elyor', 'Hasan', 'Mirasil', 'Elyor', "Og'abek"]
# data = np.random.rand(7, 4) # ismlarga tegishli ma'lumotlar
# # Hasanga tegishli ma'lumotlarni olish
# print(data[names == 'Hasan'])
# print(names)
# print(data)

# Yuqoridagi booleanni uyda collabda yozib tekshirish


# Array o'qlarini almashtirish  -- ustunni qator ko'rinishida qilish
# Array pozitsiyasini ko'chirish
# arr = np.arange(12).reshape(3, 4)
# print(arr.T)

# Array o'qlarini almashtirish -- ustunni qator ko'rinishida qilib beradi
# print("Array :\n", arr)
# print("Transpose :\n", arr.T)
# print("O'qlarini almashtirish :\n", arr.swapaxes(0, 1))


# arr = np.arange(16).reshape(4, 4)
# print(arr)
# print(arr.swapaxes(1, 0))


# Transposeni matematikada qo'llanishi 
# arr = np.arange(8).reshape(2, 4)
# print(arr)
# print("Transpose:\n", arr.T)
# print("Transpose matematika:\n", np.dot(arr, arr.T)) # dot arrayni ikkinchi arrayga ko'paytirib beradi
# mana shu kodda arraylar qanday ko'paytirilganini skreshot olib mohirdevga tashash


# universal funksiyalar mavzusi -> 2taga bo'linadi 1) Unary (bitta argument oladi)
# 2) Binary (2 ta argument qabul qiladi)
# arr = np.array([np.NaN, 2, 3, 4, 5]) 
# print(np.sqrt(arr)) # har bir elementdan kvadrat ildiz qaytaradi 
# print(np.square(arr)) # har bir elementni kvadratga ko'taradi
# print(np.exp(arr)) # har bir elementni (a ni "e"-darajaga oshiradi)
# print(np.log(arr)) # loge ga nisbatan hisoblaydi 
# print(np.modf(arr)) # float sonlarni 2 ta arrayga butun qismli va qoldiq qismlilarga ajratadi
#   yuqoridagi modf metodini ham netdan o'rganib kodni collabda tekshirish
# print(np.sign(arr)) # elementlar + bo'lsa (1) ni , - bo'lsa (-1) ni qaytaradi
# print(np.isnan(arr)) # nan bo'lsa true qaytaradi , yo'q bo'lsa false

# arr1 = np.arange(1, 6)
# arr2 = np.array([-6, 7, -8, 9, -10])
# print(arr1) 
# print(arr2)
# print(np.add(arr1, arr2))
# print(np.subtract(arr2, arr1))
# print(np.power(arr1, arr2)) # birinchi array elementlarini , 2-array elementlariga kopaytiradi
# print(np.copysign(arr1, arr2)) # 2-array ishoralarini 1-array mos elementlariga copy qiladi

# mantiqiy shart operatori (where)
# arr = np.arange(1, 6)
# print(arr)
# arr2 = np.array([0, 3, 2, 5, 1])
# print(arr2)
# print(np.where(arr>arr2, arr, '-'))


# Matematik va statik amallar
# arr = np.arange(1, 16).reshape(3, 5)
# print(arr)
# print(np.sum(arr, axis=1))

# arr = np.arange(1, 11)
# print(np.mean(arr)) # o'rta arifmetik

# arr = np.arange(1, 6)
# print(np.cumsum(arr))

# Sorting 
# arr = np.random.rand(10).reshape(2, 5)
# print(arr)
# # print(np.sort(arr))
# arr.sort()
# print(arr)
# print("teskarisi: \n")
# rev_arr = -np.sort(-arr)
# print(rev_arr)
# # print(np.sort(arr, axis=0))
# # print(np.sort(arr, axis=1))

