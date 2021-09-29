# DEVELOPED BY TUSHAR CHOPRA
# CLASS-> 12TH
# TOPIC-> GROSS DOMESTIC PRODUCT ANALYSIS

# LIBRARIES USED
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

# DATAFRAME USED
df = pd.read_csv('gdp_proj.csv')
pd.set_option('display.max_columns', None)


# FUNCTION FOR MAIN MENU
def menu():
    ans = True
    while ans:
        print("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GROSS DOMESTIC PRODUCT ANALYSIS SYSTEM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1- DATA VISUALISATION
2- DATA ANALYSIS
3- READ CSV/EXCEL FILE
4- DATA MANIPULATION
5- EXIT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
        inp = int(input('Enter your choice:'))
        if inp == 1:
            datavisual()
        elif inp == 2:
            gdpanalysis()
        elif inp == 3:
            read_csv_excel()
        elif inp == 4:
            manuplt()
        elif inp == 5:
            ex = input('Are you sure you want to exit?(y/n)')
            if ex == 'y' or ex == 'Y':
                print('Have a nice day')
                sys.exit()
        else:
            print('Try again')


# FUNCTION FOR PLOTTING GRAPHS
def datavisual():
    ans = True
    while ans:
        print("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DATA VISUALISATION OF STATES/UTs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
a- LINE CHART-> GSDP CURRENT PRICE VS YEAR
b- BAR GRAPH-> YEAR VS GSDP CURRENT PRICE OF TOP 5 STATES/UTs
c- BAR GRAPH-> % GROWTH OVER PREVIOUS YEAR VS YEAR OF TOP 5 STATES/UTs
d- EXIT TO MAIN MENU
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
        ans = input('Enter choice:')
        if ans == 'a':
            print(line_chart1())
        elif ans == 'b':
            print(bar_chart1())
        elif ans == 'c':
            print(bar_chart2())
        elif ans == 'd':
            print(menu())
        else:
            print("Error. Try again")
            continue


# LINE CHART-> GSDP CURRENT PRICE VS YEAR
def line_chart1():
    df = pd.read_csv('gdp_proj.csv')
    df.sort_values('All_India GDP', ascending=False, inplace=True)
    df = df.loc[:, ['All_India GDP', 'Duration']]
    df1 = df.head(6)
    gdp = df1['All_India GDP']
    durations = df1['Duration']
    plt.plot(durations, gdp, color='green', marker='.')
    x = np.arange(len(durations))
    plt.xticks(x, durations, rotation=30)
    plt.xlabel('Year')
    plt.ylabel('GSDP CURRENT PRICE VS YEAR IN CRORES')
    plt.fill_between(durations, gdp, color='pink')
    plt.show()


# BAR GRAPH-> YEAR VS GSDP CURRENT PRICE OF TOP 5 STATES/UTs
def bar_chart1():
    df = pd.read_csv('gdp_proj.csv')
    df = df.sort_values('All_India GDP', ascending=False)
    df = df.loc[:, ['Duration', 'Andhra Pradesh', 'Delhi', 'Madhya Pradesh', 'Tamil Nadu', 'Telangana']]
    df1 = df.head(6)
    st1 = df1['Andhra Pradesh']
    st2 = df1['Delhi']
    st3 = df1['Madhya Pradesh']
    st4 = df1['Tamil Nadu']
    st5 = df1['Telangana']
    dur = df1['Duration']
    plt.barh(dur, st1, color='b', label='Andhra Pradesh')
    plt.barh(dur, st2, color='r', label='Delhi')
    plt.barh(dur, st3, color='pink', label='Madhya Pradesh')
    plt.barh(dur, st4, color='g', label='Tamil Nadu')
    plt.barh(dur, st5, color='c', label='Telangana')
    y = np.arange(len(dur))
    plt.yticks(y, dur, rotation=30)
    plt.xlabel('GSDP Current Price of Top 5 States/UTs in crores')
    plt.ylabel('Year')
    plt.legend()
    plt.show()


# BAR GRAPH-> % GROWTH OVER PREVIOUS YEAR VS YEAR OF TOP 5 STATES/UTs
def bar_chart2():
    df = pd.read_csv('gdp_proj.csv')
    df = df.sort_values('All_India GDP', ascending=False)
    df = df.loc[:, ['Duration', 'Andhra Pradesh', 'Assam', 'Jammu & Kashmir', 'Madhya Pradesh', 'Uttarakhand']]
    df1 = df.tail(11)
    st1 = df1['Andhra Pradesh']
    st2 = df1['Assam']
    st3 = df1['Jammu & Kashmir']
    st4 = df1['Madhya Pradesh']
    st5 = df1['Uttarakhand']
    dur = df1['Duration']
    plt.bar(dur, st1, color='g', label='Andhra Pradesh')
    plt.bar(dur, st2, color='pink', label='Assam')
    plt.bar(dur, st3, color='c', label='Jammu & Kashmir')
    plt.bar(dur, st4, color='y', label='Madhya Pradesh')
    plt.bar(dur, st5, color='b', label='Uttarakhand')
    x = np.arange(len(dur))
    plt.xticks(x, dur, rotation=30)
    plt.xlabel('Year')
    plt.ylabel('% Growth over previous years')
    plt.legend()
    plt.show()


# FUNCTION FOR ANALYSIS OF DATA
def gdpanalysis():
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Data Frame Analysis")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('''1->To print gsdp at current rate of top five states/uts
2->To print % Growth of top five states/uts
3->To print gsdp at current rate of all union territories
4->To print gsdp at current rate of All india 
5->To print % Growth of All India
6->Exit''')
        x = int(input('Enter Choice:'))
        if x == 1:
            df1 = df.sort_values('All_India GDP', ascending=False, ignore_index=True)
            df1 = df.loc[:, ['Duration', 'Andhra Pradesh', 'Delhi', 'Madhya Pradesh', 'Tamil Nadu', 'Telangana']]
            n = int(input('Enter number of years to be displayed(maximum 6)-'))
            print(n)
            print(df1.head(n))
        elif x == 2:
            df1 = df.sort_values('All_India GDP', ascending=False, ignore_index=True)
            df1 = df.loc[:, ['Duration', 'Andhra Pradesh', 'Assam', 'Jammu & Kashmir', 'Madhya Pradesh', 'Uttarakhand']]
            n = int(input("Enter number of years to be displayed(maximum 5)-"))
            print(n)
            print(df1.tail(n))
        elif x == 3:
            df1 = df.sort_values('All_India GDP', ascending=False, ignore_index=True)
            df1 = df.loc[:,
                  ['Duration', 'Delhi', 'Jammu & Kashmir', 'Andaman & Nicobar Islands', 'Chandigarh', 'Puducherry']]
            n = int(input("Enter number of years to be displayed(maximum 6)-"))
            print(n)
            print(df1.head(n))
        elif x == 4:
            df1 = df.sort_values('All_India GDP', ascending=False, ignore_index=True)
            df1 = df.loc[:, ['Duration', 'All_India GDP']]
            n = int(input("Enter number of years to be displayed(maximum 6)-"))
            print(n)
            print(df1.head(6))
        elif x == 5:
            df1 = df.sort_values('All_India GDP', ascending=False, ignore_index=True)
            df1 = df.loc[:, ['Duration', 'All_India GDP']]
            n = int(input("Enter number of years to be displayed(maximum 5)-"))
            print(n)
            print(df1.tail(5))
        elif x == 6:
            print(menu())
        else:
            print("Error. Try again")


# FUNCTION TO READ CSV/EXCEL FILE
def read_csv_excel():
    ans = True
    while ans:
        print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1->Read csv file and display DataFrame
2->Press 2 to go back to the main menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
        ans = int(input("Enter choice"))
        if ans == 1:
            df = pd.read_csv('gdp_proj.csv')
            print(df)
        elif ans == 2:
            menu()


# FUNCTION FOR DATA MANIPULATION
def manuplt():
    df = pd.read_csv('gdp_proj.csv')
    ans = True
    while ans:
        print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1-> Deleting a Row
2-> Deleting a Column
3-> Renaming a Column
4-> Exit to main menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
        ans = int(input("Enter choice"))
        pd.set_option('display.max_columns', None)

        if ans == 1:
            inp = int(input("Enter the row's index you want to be deleted"))
            print('original dataframe')
            print(df)
            df1 = df.drop(inp, axis=0)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(df1)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        elif ans == 2:
            print('DataFrame before deletion of columns')
            print(df)
            inp = input("column name u want to delete")
            df = df.drop(inp, axis=1)
            print(inp)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('DataFrame after deletion', df)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        elif ans == 3:
            print("DataFrame before changing the column name")
            print(df)
            old = input("Enter the column name you want to rename")
            new = input("Enter new column name")
            df = df.rename(columns={old: new})
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('DataFrame after changing the column')
            print(df)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        elif ans == 4:
            menu()


menu()
