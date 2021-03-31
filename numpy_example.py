import numpy as np

# pip install numpy

tab = [ 2, 3, 14]

vec = np.array([ 2, 3, 14])

print(tab)
print(vec)
print(vec*vec)
print(vec.shape)
print(vec.ndim)
print(vec.transpose()*vec)
#iloczyn skalarny wektorów
print(vec.dot(vec))
#iloczyn wektorowy wektorów
print(np.cross(vec, vec))

# matrix = np.array([[2,3,4], [7,6,5]])
# print(matrix)
# print(matrix*matrix)
# print(matrix.shape)
# print(matrix.ndim)

# print(matrix.transpose())
# m_v2 =matrix.reshape(3,2)
# print(m_v2)
# m3 = matrix.reshape(1,3,2)
# print(m3)
# print(m_v2[0])
# print(m3[0])

# print (matrix[1,2])
# print (matrix[:,1:])
# print (matrix[:,-2:])

# m = [
#       [1,2,3,4,5],
#       [2,3,4,5,6],
#       [3,4,5,6,7]
#     ]
# print("======")
# print(m[1][0:5:2])  # od 0 do 5 co drugi

# print(matrix.dtype)
# #stara macierz
# matrix = np.array([[2,3,4], [7,6,5]])
# #ta sama ale inny typ
# matrix = np.array([[2,3,4], [7,6,5]], dtype=np.float32)
# print(matrix.dtype)
# print(matrix)

# matrix = np.array([[2,3,4], [7,6,5]], dtype=np.float32)
# print('max:',np.max(matrix))
# print('mean:',np.mean(matrix))
# print('std:',np.std(matrix))
# print('sum',np.sum(matrix))
# print('sum',np.sum(matrix, axis=0)) #suma w kolumnach
# print('sum',np.sum(matrix, axis=1)) #suma w wierszach
# print('max:',np.max(matrix, axis=0))
#
# m2 = matrix.copy().reshape(3,2) #kopia
# m3 = matrix.view().reshape(3,2) #widok
# matrix[0,0]=12
# print(m2)
# print(m3)
#
# for a in matrix:
#     for b in a:
#         print(b)

v1 = np.array([1,2,3])
v2 = np.array([4,5,6])
print(np.concatenate((v1,v2)))
print(np.stack((v1,v2)))
print(np.concatenate( (v1,[6]) ))
v3 = np.concatenate((v1,v2))
indeksy =np.where(v3%2==0)
print("indeksy parzystych",indeksy)
print('Wypisz parzyste', v3[indeksy])

miejscowosci = np.array(["Lodz","Berlin","Warta"])
mieszkancy = np.array([700000,3000000,5000])
indeksy = np.where(mieszkancy>10000)
print(miejscowosci[indeksy])