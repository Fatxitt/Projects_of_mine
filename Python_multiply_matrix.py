import numpy as np
# Cách nhân ma trận thông thường 
def Multiply_matrix_normally(x, y):
    if len(arr2) != len(list(zip(*arr1))):
        return  "Ma trận không nhân được "
    rows=len(x)
    cols=len(y[0])
    result= [[0] * cols for _ in range(rows)]# Đây là các tạo list với kích thước đã biết 
                                                #nhờ cách này ta cũng biết nếu muốn thêm phần tử trong ma trận dạng list mà y chang  thì:
                                                # [[A ]* só phần tử như tập hợp A]=>> [[A,A]]
                                                
    for i in range(len(x)):# len(x) là số cột chứ không phải số hàng 
        for j in range(len(y[0])): #có thể dùng len(zip(*arr2) hoặc dùng len(y[0]) để biểu thị số cột 
            for k in range (len(y)):
                result[i][j]+=x[i][k]*y[k][j]  
    return result         

       
# Cách nhân 2 ma trận sử dụng list comprehension ( ở đây lưu ý cái cách zip(*arr2) là nó giống như ma trận chuyển vị vì * để giải nén khỏi list
# sau đó thì zip lại , hàm zip thì nó zip song song nên mới có chuyện như vậy)
def Multiply_2D_array_using_list_comprehension(arr1,arr2):
    if len(arr2) != len(list(zip(*arr1))):
        return  "Ma trận không nhân được "
    arr_result=[]
    arr_result=[[sum(a*b for a,b in zip(arr1_row,arr2_col)) for arr2_col in zip(*arr2) ] for arr1_row in arr1 ] 
    return arr_result


# cách nhân ma trận sử dụng numpy:
# Cách chuyển đổi từ list sang numpy array thì chỉ cần np.array , còn từ numoy chiển về list thì chỉ cần .tolist 
if __name__=='__main__':
    arr1=[[1,2,3],
          [5,6,7],
          [8,9,10]]
    arr2=[[1,2,3,9],
        [4,5,6,9],
        [7,8,9,9]]
    
    #Cách 1:
    print(Multiply_2D_array_using_list_comprehension(arr1, arr2))
    #Cách 2:
    print(Multiply_matrix_normally(arr1, arr2))
    #Cách 3:
    arr1=np.array(arr1)
    arr2=np.array(arr2)
    print(arr1.dot(arr2))
#  cách tạo một 2D list tổng quát với kích thước cho trước là 
 #cách tạo một 2d list tổng quát
    #lst=[[0]*cols]*rows
    #vd:
    lst=[[0]*10]*2
    print (lst)
    # có thể dùng comprehension luôn nha
    #matrix = [[0 for _ in range(5)] for _ in range(5)]  nếu thay thế _ bằng một biến j cũng không thay đổi gì
    
    
# ý nghĩa của dấu _ là một biến không quan trọng (nhưng lại rất hay và hữu ích) 
#vd 1: Dùng _trong vòng lặp thì  vòng lặp sẽ chạy theo số lần mà không cần biết biến đếm 
    #matrix = [[0 for _ in range(5)] for _ in range(5)]  nếu thay thế _ bằng một biến j cũng không thay đổi gì
    
    print (list(['1','2','3'] for j in range (10)) )
#vd 2: khi một hàm trả về nhiều biến nhưng ta chỉ cần có 1 thì nó sẽ tự bỏ qua (_ cũng là một biến đó nha)
    #result, _ = some_function()  # Giá trị thứ hai không được sử dụng
    
    a,_=(9,0)
    print (_)
#chaining comparison
 
 
    print (1<2<3)
 # có thể sử dụng switch trong python nhưng phải có kĩ thuật cao và nó có thể tích hợp với lambda để tạo nên một hàm mạnh
    a,b,c=str(input("nhap so ma bạn muón")).split()
    print (a, b,c,sep=" ")
    dict_func={
        '+':lambda a,b : a+b,
        '-':lambda a,b:a-b,
        '*':lambda a,b:a*b,
        '/':lambda a,b:a/b,
    }
    print(dict_func['+'](10,9))