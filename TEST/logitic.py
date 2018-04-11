#线性回归

def compute_error(b, m, data):
    totalError = 0
    for i in range(0,len(data)):
        x = data[i,0]
        y = data[i,1]
        totalError += (y-(m*x+b))**2

    return totalError

def compute_gradient(b_current,m_current,data ,learning_rate):

    b_gradient = 0
    m_gradient = 0

    N = float(len(data))
    #Two ways to implement this
    #first way
    for i in range(0,len(data)):
        x = data[i,0]
        y = data[i,1]
    #computing partial derivations of our error function
        b_gradient = -(2/N)*sum((y-(m_current*x+b_current))^2)
        m_gradient = -(2/N)*sum(x*(y-(m_current*x+b_current))^2)
        b_gradient += -(2/N)*(y-((m_current*x)+b_current))
        m_gradient += -(2/N) * x * (y-((m_current*x)+b_current))

    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    return [new_b,new_m]
def optimizer(data, initial_b, initial_m, learning_rate, num_iter):
    a = 0

def linear_regression(day, v_f, day_f_num):
    #file = open("")
    file = open(r"D:\\python27\untitled\data.csv", "r")
    data = file.readlines()

    learning_rate = 0.001
    initial_b =0.0
    initial_m = 0.0
    num_iter = 1000
    print('initial variables:\n initial_b = {0}\n intial_m = {1}\n error of begin = {2} \n' \
        .format(initial_b, initial_m, compute_error(initial_b, initial_m, data)))

    # optimizing b and m
    [b, m] = optimizer(data, initial_b, initial_m, learning_rate, num_iter)

    # print final b m error
    print('final formula parmaters:\n b = {1}\n m={2}\n error of end = {3} \n'.\
        format(num_iter, b, m, compute_error(b, m, data)))