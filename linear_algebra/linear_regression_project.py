
# coding: utf-8

# # 欢迎来到线性回归项目
# 
# 若项目中的题目有困难没完成也没关系，我们鼓励你带着问题提交项目，评审人会给予你诸多帮助。
# 
# 所有选做题都可以不做，不影响项目通过。如果你做了，那么项目评审会帮你批改，也会因为选做部分做错而判定为不通过。
# 
# 其中非代码题可以提交手写后扫描的 pdf 文件，或使用 Latex 在文档中直接回答。

# # 1 矩阵运算
# 
# ## 1.1 创建一个 4*4 的单位矩阵

# In[1]:


# 这个项目设计来帮你熟悉 python list 和线性代数
# 你不能调用任何NumPy以及相关的科学计算库来完成作业


# 本项目要求矩阵统一使用二维列表表示，如下：
A = [[1,2,3], 
     [2,3,3], 
     [1,2,5]]

B = [[1,2,3,5], 
     [2,3,3,5], 
     [1,2,5,1]]

#TODO 创建一个 4*4 单位矩阵
I = [[1,2,3,4],
     [5,6,8,9],
     [9,8,8,4],
     [6,4,2,4]]


# ## 1.2 返回矩阵的行数和列数

# In[2]:


# TODO 返回矩阵的行数和列数
def shape(M):
    c = len(M[0])
    r = len(M)
    return r,c


# In[3]:


# 运行以下代码测试你的 shape 函数
get_ipython().magic(u'run -i -e test.py LinearRegressionTestCase.test_shape')


# ## 1.3 每个元素四舍五入到特定小数数位

# In[4]:


# TODO 每个元素四舍五入到特定小数数位
# 直接修改参数矩阵，无返回值
from decimal import *
def matxRound(M, decPts=4):
    [[round(num,decPts) for num in row] for row in M]


# In[5]:


# 运行以下代码测试你的 matxRound 函数
get_ipython().magic(u'run -i -e test.py LinearRegressionTestCase.test_matxRound')


# ## 1.4 计算矩阵的转置

# In[6]:


# TODO 计算矩阵的转置
def transpose(M):
    return [[row[col] for row in M] for col in range(len(M[0]))]


# In[7]:


# 运行以下代码测试你的 transpose 函数
get_ipython().magic(u'run -i -e test.py LinearRegressionTestCase.test_transpose')


# ## 1.5 计算矩阵乘法 AB

# In[25]:


# TODO 计算矩阵乘法 AB，如果无法相乘则raise ValueError
def matxMultiply(A, B):
    A_C = len(A[0])
    B_R = len(B)
        
    if A_C == B_R:
        #A * B
        return [[sum(a * b for a, b in zip(a, b)) for b in zip(*B)] for a in A]
    else:
        raise ValueError()


# In[29]:


# 运行以下代码测试你的 matxMultiply 函数
get_ipython().magic(u'run -i -e test.py LinearRegressionTestCase.test_matxMultiply')


# ---
# 
# # 2 Gaussign Jordan 消元法
# 
# ## 2.1 构造增广矩阵
# 
# $ A = \begin{bmatrix}
#     a_{11}    & a_{12} & ... & a_{1n}\\
#     a_{21}    & a_{22} & ... & a_{2n}\\
#     a_{31}    & a_{22} & ... & a_{3n}\\
#     ...    & ... & ... & ...\\
#     a_{n1}    & a_{n2} & ... & a_{nn}\\
# \end{bmatrix} , b = \begin{bmatrix}
#     b_{1}  \\
#     b_{2}  \\
#     b_{3}  \\
#     ...    \\
#     b_{n}  \\
# \end{bmatrix}$
# 
# 返回 $ Ab = \begin{bmatrix}
#     a_{11}    & a_{12} & ... & a_{1n} & b_{1}\\
#     a_{21}    & a_{22} & ... & a_{2n} & b_{2}\\
#     a_{31}    & a_{22} & ... & a_{3n} & b_{3}\\
#     ...    & ... & ... & ...& ...\\
#     a_{n1}    & a_{n2} & ... & a_{nn} & b_{n} \end{bmatrix}$

# In[35]:


# TODO 构造增广矩阵，假设A，b行数相同
def augmentMatrix(A, b):
    B =[[A[j][i] for i in range(len(A[0]))] for j in range(len(A))]
    for item ,x in enumerate(B):
        x.append(b[item][0])
    return B


# In[31]:


# 运行以下代码测试你的 augmentMatrix 函数
get_ipython().magic(u'run -i -e test.py LinearRegressionTestCase.test_augmentMatrix')


# ## 2.2 初等行变换
# - 交换两行
# - 把某行乘以一个非零常数
# - 把某行加上另一行的若干倍：

# In[42]:


# TODO r1 <---> r2
# 直接修改参数矩阵，无返回值
def swapRows(M, r1, r2):
    M[r1],M[r2] = M[r2],M[r1]


# In[33]:


# 运行以下代码测试你的 swapRows 函数
get_ipython().magic(u'run -i -e test.py LinearRegressionTestCase.test_swapRows')


# In[43]:


# TODO r1 <--- r1 * scale
# scale为0是非法输入，要求 raise ValueError
# 直接修改参数矩阵，无返回值
def scaleRow(M, r, scale):
    if scale != 0:
        M[r] = [scale * x for x in M[r]]
    else:
        raise ValueError("scale is zero")


# In[37]:


# 运行以下代码测试你的 scaleRow 函数
get_ipython().magic(u'run -i -e test.py LinearRegressionTestCase.test_scaleRow')


# In[38]:


# TODO r1 <--- r1 + r2*scale
# 直接修改参数矩阵，无返回值
def addScaledRow(M, r1, r2, scale):
    M[r1] = [x + (y *scale) for x,y in zip(M[r1],M[r2])]


# In[39]:


# 运行以下代码测试你的 addScaledRow 函数
get_ipython().magic(u'run -i -e test.py LinearRegressionTestCase.test_addScaledRow')


# ## 2.3  Gaussian Jordan 消元法求解 Ax = b

# ### 2.3.1 算法
# 
# 步骤1 检查A，b是否行数相同
# 
# 步骤2 构造增广矩阵Ab
# 
# 步骤3 逐列转换Ab为化简行阶梯形矩阵 [中文维基链接](https://zh.wikipedia.org/wiki/%E9%98%B6%E6%A2%AF%E5%BD%A2%E7%9F%A9%E9%98%B5#.E5.8C.96.E7.AE.80.E5.90.8E.E7.9A.84-.7Bzh-hans:.E8.A1.8C.3B_zh-hant:.E5.88.97.3B.7D-.E9.98.B6.E6.A2.AF.E5.BD.A2.E7.9F.A9.E9.98.B5)
#     
#     对于Ab的每一列（最后一列除外）
#         当前列为列c
#         寻找列c中 对角线以及对角线以下所有元素（行 c~N）的绝对值的最大值
#         如果绝对值最大值为0
#             那么A为奇异矩阵，返回None (你可以在选做问题2.4中证明为什么这里A一定是奇异矩阵)
#         否则
#             使用第一个行变换，将绝对值最大值所在行交换到对角线元素所在行（行c） 
#             使用第二个行变换，将列c的对角线元素缩放为1
#             多次使用第三个行变换，将列c的其他元素消为0
#             
# 步骤4 返回Ab的最后一列
# 
# **注：** 我们并没有按照常规方法先把矩阵转化为行阶梯形矩阵，再转换为化简行阶梯形矩阵，而是一步到位。如果你熟悉常规方法的话，可以思考一下两者的等价性。

# ### 2.3.2 算法推演
# 
# 为了充分了解Gaussian Jordan消元法的计算流程，请根据Gaussian Jordan消元法，分别手动推演矩阵A为奇异矩阵，矩阵A为非奇异矩阵两种情况。

# In[139]:


# 不要修改这里！
from helper import generateMatrix,printInMatrixFormat
    
rank = 4
A = generateMatrix(rank,singular=False)
b = np.ones(shape=(rank,1)) # it doesn't matter
printInMatrixFormat(rank,A,b)


# 请按照算法的步骤3，逐步推演增广矩阵的变换。
# 
# 在下面列出每一次循环体执行之后的增广矩阵
# 
# 增广矩阵
# $ Ab = \begin{bmatrix}
#     1 & 1.2 & -1.6 & -1.6 & -0.2\\
#     0 & -4.4 & 7.2 & 12.2 & 1.4\\
#     0 & -15.2 & 1.6 & 11.6 & 2.2\\
#     0 & -4.4 & -5.8 & -3.8 & 0.4\end{bmatrix}$
# 
# $ --> \begin{bmatrix}
#     1 & 0 & -1.473 & -0.681 & -0.026\\
#     0 & 1 & -1.634 & -2.769 & -0.318\\
#     0 & 0 & 6.7336 & 7.83 & 0.762\\
#     0 & 0 & -6.266 & -7.17 & -0.238\end{bmatrix}$
#     
# $ --> \begin{bmatrix}
#     1 & 0 & 0 & 1.038 & 0.142\\
#     0 & 1 & 0 & -0.642 & -0.133\\
#     0 & 0 & 1 & 1.167 & 0.114\\
#     0 & 0 & 0 & 0.144 & 0.476\end{bmatrix}$
# 
# $ --> \begin{bmatrix}
#     1 & 0 & 0 & 0 & 0.058\\
#     0 & 1 & 0 & 0 & -0.095\\
#     0 & 0 & 1 & 0 & 0.029\\
#     0 & 0 & 0 & 1 & 0.061\end{bmatrix}$
#     
# 

# ### 2.3.3 实现 Gaussian Jordan 消元法

# In[1]:


# TODO 实现 Gaussain Jordan 方法求解 Ax = b

""" Gaussian Jordan 方法求解 Ax = b.
    参数
        A: 方阵 
        b: 列向量
        decPts: 四舍五入位数，默认为4
        epsilon: 判读是否为0的阈值，默认 1.0e-16
        
    返回列向量 x 使得 Ax = b 
    返回None，如果 A，b 高度不同
    返回None，如果 A 为奇异矩阵
"""
from copy import deepcopy
def gj_Solve(A, b, decPts=4, epsilon = 1.0e-16):
    #1.1检查A，b的行数是否相等
    num_equations = len(A)#这里的A是方阵，所以不用去判断维度相等不相等
    num_variables = len(b)

    augmented_matrix = augmentMatrix(A,b)
    copy_augmented_matrix = deepcopy(augmented_matrix)
    #1.2 构造增广矩阵Ab  不影响原来的方阵A
    for i in range(num_equations):
        max_values_in_row = gets_the_maximum_value_of_the_diagonal_element(A,i,num_equations,epsilon)
        if i > -1 and max_values_in_row > -1:
            swapRows(copy_augmented_matrix,i,max_values_in_row)
        scale_row_to_make_coefficient_equal_one(copy_augmented_matrix,i,decPts)
        clear_coeffients_below(copy_augmented_matrix,i,decPts)
        if i > 0:#第一次不必清除上面的元素
            clear_coeffients_above(copy_augmented_matrix,i,decPts)
    a = create_two_dimens_array(copy_augmented_matrix)
    return a

#获取最大值所在的行
def gets_the_maximum_value_of_the_diagonal_element(matrix,row,num_row,epsilon):
    all_dict = {}
    
    for x in range(row,num_row):
        y = x
        while y < num_row :
            all_dict[matrix[y][x]] = y
            y += 1
            
    max_elements_index = -1
    max_elements = 0
    all_elements = all_dict.keys()
    
    for i,p in enumerate(all_elements):
        if abs(p) > max_elements:
            max_elements_index = i
            max_elements = abs(p)
    
    if max_elements < epsilon:
        return None
    else:
        return all_dict[all_elements[max_elements_index]]

def swap_row(matrix,row,be_changed_row):
    matrix[row],matrix[be_changed_row] = matrix[be_changed_row],matrix[row],matrix[be_changed_row]


def scale_row_to_make_coefficient_equal_one(matrix,row,decPts):
    if Decimal(matrix[row][row]) != 0:
        coefficient = Decimal('1') / Decimal(matrix[row][row])
        matrix[row] = [round(Decimal(i) * coefficient,decPts) for i in matrix[row]]
    
def clear_coeffients_below(matrix,row,decPts):
        num_equations = len(matrix)
        
        for k in range(row+1,num_equations):
            if Decimal(matrix[k][row]) != 0:
                beta = -Decimal('1') / Decimal(matrix[k][row])
                matrix[k] = [round(Decimal(i) * beta,decPts) for i in matrix[k]]
                matrix[k] = [x + y for x,y in zip(matrix[k],matrix[row])]
            
def clear_coeffients_above(matrix,col,decPts):
    for i in range(col)[::-1]:
        matrix[i] = [round(x + (-(y * matrix[i][col])),decPts)
                     for x,y in zip(matrix[i],matrix[col])]
    
            
def create_two_dimens_array(matrix):
    #创建一个默认的数组
    two_dimens_array = []
    for i in range(len(matrix)):
        two_dimens_array.append([0])
      
    x = 0
    for j in matrix:
        two_dimens_array[x][0] = j[len(matrix)]
        x += 1
    return two_dimens_array


# In[154]:


# 运行以下代码测试你的 gj_Solve 函数
get_ipython().magic(u'run -i -e test.py LinearRegressionTestCase.test_gj_Solve')


# ## (选做) 2.4 算法正确判断了奇异矩阵：
# 
# 在算法的步骤3 中，如果发现某一列对角线和对角线以下所有元素都为0，那么则断定这个矩阵为奇异矩阵。
# 
# 我们用正式的语言描述这个命题，并证明为真。
# 
# 证明下面的命题：
# 
# **如果方阵 A 可以被分为4个部分: ** 
# 
# $ A = \begin{bmatrix}
#     I    & X \\
#     Z    & Y \\
# \end{bmatrix} , \text{其中 I 为单位矩阵，Z 为全0矩阵，Y 的第一列全0}$，
# 
# **那么A为奇异矩阵。**
# 
# 提示：从多种角度都可以完成证明
# - 考虑矩阵 Y 和 矩阵 A 的秩
# - 考虑矩阵 Y 和 矩阵 A 的行列式
# - 考虑矩阵 A 的某一列是其他列的线性组合

# TODO 证明：
# 
# A是方阵，假设A是nxn的方阵，又因为I是单位矩阵 Z是零矩阵 Y的第一列是零 X是任意的矩阵
#     所以可以认为当A是非奇异方阵的时候的秩是n 
# 
#     此时的r(A) = r(I) + r(Y) 等于上下分块矩阵的秩的和，上面的矩阵是I和X I是单位阵所以上边的秩可以
#     认为就是单位矩阵的秩r(I)   下部分中Z是零矩阵 Y的第一列是零向量所以下边的秩可以认为是r(Y)
# 
#     此时假设r(I) = m ,那么Y中就有n - m那么多列，因为Y中最后一列是零向量，====》r(Y) < n - m
#     所以此时的总的分块矩阵的秩r(I) + r(Y) < n，也就是r(A) < n,所以A是奇异矩阵，此时的A的秩不是满秩

# # 3  线性回归

# ## 3.1 随机生成样本点

# In[62]:


# 不要修改这里！
from helper import generatePoints
from matplotlib import pyplot as plt

X,Y = generatePoints(num=100)
## 可视化
plt.xlim((-5,5))
plt.xlabel('x',fontsize=18)
plt.ylabel('y',fontsize=18)
plt.scatter(X,Y,c='b')
plt.show()


# ## 3.2 拟合一条直线
# 
# ### 3.2.1 猜测一条直线

# In[83]:


#TODO 请选择最适合的直线 y = kx + b
k = 2.8

b = 8



# 不要修改这里！
plt.xlim((-5,5))
x_vals = plt.axes().get_xlim()
y_vals = [k*x+b for x in x_vals]
plt.plot(x_vals, y_vals, 'r-')

plt.xlabel('x',fontsize=18)
plt.ylabel('y',fontsize=18)
plt.scatter(X,Y,c='b')

plt.show()


# ### 3.2.2 计算平均平方误差 (MSE)

# 我们要编程计算所选直线的平均平方误差(MSE), 即数据集中每个点到直线的Y方向距离的平方的平均数，表达式如下：
# $$
# MSE = \frac{1}{n}\sum_{i=1}^{n}{(y_i - mx_i - b)^2}
# $$

# In[84]:


# TODO 实现以下函数并输出所选直线的MSE

def calculateMSE(X,Y,m,b):
    #求所有点到直线y方向上的距离的平方的平均值（y1-mx1 - b）^2+.....+(yn-mxn - b)^2/n
    all_sum = sum([(y - (m * x) - b)**2 for x,y in zip(X,Y)])/len(X)
    return  all_sum

print(calculateMSE(X,Y,k,b))


# ### 3.2.3 调整参数 $m, b$ 来获得最小的平方平均误差
# 
# 你可以调整3.2.1中的参数 $m,b$ 让蓝点均匀覆盖在红线周围，然后微调 $m, b$ 让MSE最小。

# ## 3.3 (选做) 找到参数 $m, b$ 使得平方平均误差最小
# 
# **这一部分需要简单的微积分知识(  $ (x^2)' = 2x $ )。因为这是一个线性代数项目，所以设为选做。**
# 
# 刚刚我们手动调节参数，尝试找到最小的平方平均误差。下面我们要精确得求解 $m, b$ 使得平方平均误差最小。
# 
# 定义目标函数 $E$ 为
# $$
# E = \frac{1}{2}\sum_{i=1}^{n}{(y_i - mx_i - b)^2}
# $$
# 
# 因为 $E = \frac{n}{2}MSE$, 所以 $E$ 取到最小值时，$MSE$ 也取到最小值。要找到 $E$ 的最小值，即要找到 $m, b$ 使得 $E$ 相对于 $m$, $E$ 相对于 $b$ 的偏导数等于0. 
# 
# 因此我们要解下面的方程组。
# 
# $$
# \begin{cases}
# \displaystyle
# \frac{\partial E}{\partial m} =0 \\
# \\
# \displaystyle
# \frac{\partial E}{\partial b} =0 \\
# \end{cases}
# $$
# 
# ### 3.3.1 计算目标函数相对于参数的导数
# 首先我们计算两个式子左边的值
# 
# 证明/计算：
# $$
# \frac{\partial E}{\partial m} = \sum_{i=1}^{n}{-x_i(y_i - mx_i - b)}
# $$
# 
# $$
# \frac{\partial E}{\partial b} = \sum_{i=1}^{n}{-(y_i - mx_i - b)}
# $$

# TODO 证明:
# 
# $$
# E = \frac{1}{2}\\((y_1 - mx_1 - b)^2 + (y_1 - mx_1 - b)^2 + ... + (y_n - mx_n - b)^2 )
# $$
# 
# $$
# \frac{\partial E}{\partial m} = \frac{1}{2}\\(-2x_1(y_1 - mx_1 - b) -2x_2(y_2 - mx_2 - b) + .... -2x_n(y_n - mx_n - b))
# $$
# 
# $$
# \frac{\partial E}{\partial m} = -x_1(y_1 - mx_1 - b) -x_2(y_2 - mx_2 - b) + .... -x_n(y_n - mx_n - b) = \sum_{i=1}^{n}{-x_i(y_i - mx_i - b)}
# $$
# 
# 
# $$
# \frac{\partial E}{\partial b} = \frac{1}{2}\\(-2(y_1 - mx_1 - b) -2(y_2 - mx_2 - b) + .... -2(y_n - mx_n - b))
# $$
# 
# $$
# \frac{\partial E}{\partial b} = -(y_1 - mx_1 - b) -(y_2 - mx_2 - b) + .... -(y_n - mx_n - b) = \sum_{i=1}^{n}{-(y_i - mx_i - b)}
# $$

# ### 3.3.2 实例推演
# 
# 现在我们有了一个二元二次方程组
# 
# $$
# \begin{cases}
# \displaystyle
# \sum_{i=1}^{n}{-x_i(y_i - mx_i - b)} =0 \\
# \\
# \displaystyle
# \sum_{i=1}^{n}{-(y_i - mx_i - b)} =0 \\
# \end{cases}
# $$
# 
# 为了加强理解，我们用一个实际例子演练。
# 
# 我们要用三个点 $(1,1), (2,2), (3,2)$ 来拟合一条直线 y = m*x + b, 请写出
# 
# - 目标函数 $E$, 
# - 二元二次方程组，
# - 并求解最优参数 $m, b$

# TODO 写出目标函数，方程组和最优参数
# 
# 
# $$
# E = \frac{1}{2}\sum_{i=1}^{n}{(y_i - mx_i - b)^2}
# $$
# 
# 根据
# 
# $$
# \begin{cases}
# \displaystyle
# \sum_{i=1}^{n}{-x_i(y_i - mx_i - b)} =0 \\
# \\
# \displaystyle
# \sum_{i=1}^{n}{-(y_i - mx_i - b)} =0 \\
# \end{cases}
# $$可以求出m和b
# 
# 已知点$(1,1), (2,2), (3,2)$，第三个点带入到两个方程可以求出$m$和$b$
# 
# $$
# \begin{cases}
# \displaystyle
# \\14m + 6b =11 \\
# \\
# \displaystyle
# \\6m + 3b =5 \\
# \end{cases}
# $$
# 
# 所以最优参数$m = 0.5$,$b = 0.67$

# ### 3.3.3 将方程组写成矩阵形式
# 
# 我们的二元二次方程组可以用更简洁的矩阵形式表达，将方程组写成矩阵形式更有利于我们使用 Gaussian Jordan 消元法求解。
# 
# 请证明 
# $$
# \begin{bmatrix}
#     \frac{\partial E}{\partial m} \\
#     \frac{\partial E}{\partial b} 
# \end{bmatrix} = X^TXh - X^TY
# $$
# 
# 其中向量 $Y$, 矩阵 $X$ 和 向量 $h$ 分别为 :
# $$
# Y =  \begin{bmatrix}
#     y_1 \\
#     y_2 \\
#     ... \\
#     y_n
# \end{bmatrix}
# ,
# X =  \begin{bmatrix}
#     x_1 & 1 \\
#     x_2 & 1\\
#     ... & ...\\
#     x_n & 1 \\
# \end{bmatrix},
# h =  \begin{bmatrix}
#     m \\
#     b \\
# \end{bmatrix}
# $$

# TODO 证明:
# 
# 因为
# $$
# X =  \begin{bmatrix}
#     x_1 & 1 \\
#     x_2 & 1\\
#     ... & ...\\
#     x_n & 1 \\
# \end{bmatrix}
# ,
# X^T = \begin{bmatrix}
#     x_1 & x_2 & ....& x_n \\
#     1 & 1 & ....& 1\\
# \end{bmatrix}
# $$
# 
# $$
# X^TXh = \begin{bmatrix}
#     \sum_{i=1}^{n}{x_i^2} + \sum_{i=1}^{n}{bx_i} \\
#     \sum_{i=1}^{n}{mx_i} + nb \\
# \end{bmatrix}
# $$
# 
# $$
# X^TY = \begin{bmatrix}
#     \sum_{i=1}^{n}{x_iy_i} \\
#     \sum_{i=1}^{n}{y_i} \\
# \end{bmatrix}
# $$
# 
# $$
# X^TXh - X^TY = \begin{bmatrix}
#     \sum_{i=1}^{n}{-x_i(y_i - mx_i - b)} \\
#     \sum_{i=1}^{n}{-(y_i - mx_i - b)} \\
# \end{bmatrix}
# $$
# 
# 由上面的结论知道：
# $$
# \begin{cases}
# \displaystyle
# \sum_{i=1}^{n}{-x_i(y_i - mx_i - b)} =0 \\
# \\
# \displaystyle
# \sum_{i=1}^{n}{-(y_i - mx_i - b)} =0 \\
# \end{cases}
# $$
# 
# 所以可以得出
# 
# 
# $$
# X^TXh - X^TY = 
# \begin{bmatrix}
#     \frac{\partial E}{\partial m} \\
#     \frac{\partial E}{\partial b} 
# \end{bmatrix}
# $$
# 

# 至此我们知道，通过求解方程 $X^TXh = X^TY$ 来找到最优参数。这个方程十分重要，他有一个名字叫做 **Normal Equation**，也有直观的几何意义。你可以在 [子空间投影](http://open.163.com/movie/2010/11/J/U/M6V0BQC4M_M6V2AJLJU.html) 和 [投影矩阵与最小二乘](http://open.163.com/movie/2010/11/P/U/M6V0BQC4M_M6V2AOJPU.html) 看到更多关于这个方程的内容。

# ### 3.4 求解 $X^TXh = X^TY$ 
# 
# 在3.3 中，我们知道线性回归问题等价于求解 $X^TXh = X^TY$ (如果你选择不做3.3，就勇敢的相信吧，哈哈)

# In[89]:


# TODO 实现线性回归
'''
参数：X, Y
返回：m，b
'''
def linearRegression(X,Y):
    #先构建一个X矩阵
    augmented_martix = []
    new_Y = []
    for i in range(len(X)):
        augmented_martix.append([]) 
        new_Y.append([Y[i]])
    
    
    for i in range(len(X)):
        augmented_martix[i].append(X[i])
        augmented_martix[i].append(1)
        
    transpose_augmented = [[row[col] for row in augmented_martix] for col in range(len(augmented_martix[0]))]
    new_martix = [[sum(a * b for a, b in zip(a, b)) for b in zip(*augmented_martix)] for a in transpose_augmented]
    constant_martix = [[sum(a * b for a, b in zip(a, b)) for b in zip(*new_Y)] for a in transpose_augmented]

    a = gj_Solve(new_martix,constant_martix)
    return  a[0],a[1]
m,b = linearRegression(X,Y)
print(m,b)


# 你求得的回归结果是什么？它足够好了吗？请使用运行以下代码将它画出来。
# 
# 请老师指导一下，下面的y不知道是哪一个？需要自己根据m和b来构造么？

# In[94]:


# 请不要修改下面的代码
x1,x2 = -5,5
y1,y2 = x1*m+b, x2*m+b

plt.xlim((-5,5))
plt.xlabel('x',fontsize=18)
plt.ylabel('y',fontsize=18)
plt.scatter(x,y,c='b')
plt.plot((x1,x2),(y1,y2),'r')
plt.text(1,2,'y = {m}x + {b}'.format(m=m,b=b))
plt.show()

