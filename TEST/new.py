# encoding=utf-8
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
from sklearn.naive_bayes import BernoulliNB 
import matplotlib.pyplot as plt
def read_data():
    labels = []
    data_set = []
    with open("./TrainData.txt","r") as f:
        lines = f.readlines()

        for line in lines:
            line = list(map(int,line.strip("\n").split(" ")))
            # line = re.sub("\D", "", line)
            data_set.append(line[1:-1])
            labels.append(line[-1])
    return labels,data_set

def training(data_set,labels):
    labels = np.array(labels)
    data_set = np.array(data_set)
    print(labels)
    # clf =  MultinomialNB().fit(data_set, labels)
    clf = BernoulliNB()  
    clf.fit(data_set, labels)  
    BernoulliNB(alpha=1.0, binarize=0.0, class_prior=None, fit_prior=True)
    joblib.dump(clf, 'clf.model')
    return clf

def predicting(test):
    clf = joblib.load('clf.model')
    test = np.array(test).reshape(1, -1)
    # print(clf.predict(test))
    res = clf.predict(test)
    return res
def pieChart(*state):
    focus=0
    semif=0
    distr=0
    for i in range(len(state)):
        if state[i]==1:
            focus+=1
        elif state[i]==2:
            semif+=1
        elif state[i]==3:
            distr+=1
    labels=['focus','seminfocus','distraction']  
    X=[focus,semif,distr]    
  
    fig = plt.figure()  
    plt.pie(X,labels=labels,autopct='%1.2f%%') #画饼图（数据，数据对应的标签，百分数保留两位小数点）  
    plt.title("Pie chart")  
    plt.show()    
    plt.savefig("PieChart.jpg")  

if __name__ == "__main__":
    labels,data_set = read_data()
    # clf = training(data_set,labels)
    with open('TrainData.txt',"r") as f:
        lines = f.readlines()
        x = len(lines)
        y = 0
        state=[]
        focus_focus=0
        focus_semif=0
        focus_distraction=0
        semif_focus=0
        semif_semif=0
        semif_distr=0
        distr_distr=0
        distr_semif=0
        distr_focus=0
        for line in lines:
            line = list(map(int,line.strip("\n").split(" ")))
            test = []
            test.extend(line[1:-1])
            res = predicting(test)
            state.append(res)
            if res == line[-1]:
                # print(res)
               
                y += 1
        for i in range(len(state)-1):
            if state[i]==1 and state[i+1]==1:
                focus_focus+=1
            elif state[i]==1 and state[i+1]==2:
                focus_semif+=1
            elif state[i]==1 and state[i+1]==3:
                focus_distraction+=1
            elif state[i]==2 and state[i+1]==1:
                semif_focus+=1
            elif state[i]==2 and state[i+1]==2:
                semif_semif+=1
            elif state[i]==2 and state[i+1]==3:
                semif_distr+=1
            elif state[i]==3 and state[i+1]==1:
                distr_focus+=1
            elif state[i]==3 and state[i+1]==2:
                distr_semif+=1
            elif state[i]==3 and state[i+1]==3:
                distr_distr+=1
                
        print(len(state))      
        print("x",x)
        print("y",y)
        print("准确度",y/x)
        print("focus_focus",focus_focus/(x-1))
        print("focus_focus",focus_semif/(x-1))
        print("focus_focus",focus_distraction/(x-1))
        print("focus_focus",semif_focus/(x-1))
        print("focus_focus",semif_semif/(x-1))
        print("focus_focus",semif_distr/(x-1))
        print("focus_focus",distr_focus/(x-1))
        print("focus_focus",distr_semif/(x-1))
        print("focus_focus",distr_distr/(x-1))
        print((focus_distraction+focus_focus+focus_semif+distr_distr+distr_focus+distr_semif+semif_distr+semif_focus+semif_semif)/1999)
        pieChart(*state)
        
        





