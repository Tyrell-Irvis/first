#Tyrell Irvis

def read():
#put the file into a list
    info = []
    employee = open("employees.txt", "r")
    for i in range(24):
        x = employee.readline().rstrip()
        info.append(x)
    return info

def names(info):
    # takes all the names into a list
    names = []
    for i in range(0, len(info), 3):
        names.append(info[i])
    return names

def ages(info):
    ages = []
    for i in range(1, len(info), 3):
        ages.append(int(info[i]))
    return ages

def salaries(info):
    sal = []
    for i in range(2, len(info), 3):
        sal.append(int(info[i]))
    return sal

def find_min(y):#y is the list that goes into the function
    x = min(y)
    for i in range(len(y)):
        if x == y[i]:
            return i

def find_max(j):#j is the list that goes into the function
    x = max(j)
    for i in range(len(j)):
        if x == j[i]:
            return i


def main():
    info = read()

    name = names(info)
    age = ages(info)
    sal = salaries(info)
    print("list of names: " , name)
    print("list of ages: ", age)
    print("list of salaries: " , sal)
    lowSal = find_min(sal)
    print("lowest paid emplyee: ", name[lowSal])
    maxSal = find_max(sal)
    print("highest paid employee: ", name[maxSal])
    youngest = find_min(age)
    print("the youngest employee name and salary: ",name[youngest], ", ",sal[youngest] )
    oldest = find_max(age)
    print("the oldest employee name and salary: ",name[oldest], ", ", sal[oldest] )




main()