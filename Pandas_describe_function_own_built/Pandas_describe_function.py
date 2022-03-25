import pandas as pd
df=pd.read_csv(r"E:\10.python\project\project2\house-prices-advanced-regression-techniques\test.csv")
###########################################################################################################
# 'Create here own function is same functionality like pandas describe function'
############################################################################################################
class StatsPandas:
    import numpy as np
    import pandas as pd
    def __init__(self,*args):
        """Pass DataFrame as positional arguments in when you create the class instance
        *args=df
        --------------------------------------------------------------------------------
        If you check only any individual stats>>
        e.g. Stats_ob=StatsPandas(df)
        1. mean>>  Stats_ob.mean()
        2. median>> Stats_ob.median()
        3. Mode >> Stats_ob.mode()
        4. STD >> Stats_ob.std()
        5. Var >> Stats_ob.var()
        6. Maximum >> Stats_ob.maximum()
        7. Minimum >> Stats_ob.minimum()
        ---------------------------------------------------------------------------------
        If you check all above stats by using only one function>>
        1. Stats_ob.describe()
        ----------------------------------------------------------------------------------
        Thank You..................."""
        self.array1=args[0]
        self.c=[]
        for i in self.array1.columns:
             if self.array1[i].dtype!=object:
                self.c.append(i)
    ######################################
    def mean(self):
        """we are finding here mean of only numeric columns"""
        meanl1=[]
        for i in self.array1.columns:
            if self.array1[i].dtype!=object:
                z=self.np.sort(self.array1[i])
                sum1=sum(z)
                mean1=sum1/len(z)
        #         print(len(self.array))
                meanl1.append(round(mean1,2))
    #             print(f'The mean of columns {i} is >>\n',round(mean1,2))
    #             print(meanl1)
        meanl=self.np.array(meanl1)
#         print(meanl)
        meanl=meanl.reshape(1,len(meanl))
        df6=self.pd.DataFrame(meanl,index=['Mean'],columns=self.c)
#         print(df6)
        return df6
    def median(self):
        medianl=[]
        for i in self.array1.columns:
             if self.array1[i].dtype!=object:
                sort=self.np.sort(self.array1[i])
    #             print(sort)
                length=len(sort)
                first=length//2
        #         print(first)
                if len(sort)%2==0:
                    avg=(sort[first]+sort[first-1])/2
                    medianl.append(round(avg,2))
    #                 print(f'The "median" of columns {i} is >>\n',round(avg,2))
                else:
                    median=sort[first]
                    medianl.append(round(median,2))
    #                 print(f'The "median" of columns {i} is >>\n',round(median,2))
        medianl1=self.np.array(medianl)
        medianl1=medianl1.reshape(1,len(medianl1))
        df5=self.pd.DataFrame(medianl1,index=['Median'],columns=self.c)
#         print(df5)
        return df5
    def mode(self):
        model=[]
        for k in self.array1.columns:
             if self.array1[k].dtype!=object:
                array=self.array1[k]
    #             print(array)
                dict1={}
                set1=set(self.array1[k])
    #             print(set1)
                for i in set1:
                    a=array[array==i]
#                     print(a)
                    dict1.update({i:len(a)})
    #             print(dict1)
        #         print(min(dict1))
        #         print(max(dict1.values()))
                list1=[]
                for key in dict1:
                    if dict1[key]==max(dict1.values()):
                        list1.append(key)
    #             print(list1)
                model.append(round(min(list1)))
    #             print('The "Mode" of array is >>\n',round(min(list1)))
        model1=self.np.array(model)
        model1=model1.reshape(1,len(model1))
        df4=self.pd.DataFrame(model1,index=['Mode'],columns=self.c)
#         print(df)
        return df4
    def std(self):
        stdl=[]
        for i in self.array1.columns:
             if self.array1[i].dtype!=object:
                z=self.np.sort(self.array1[i])
                sum1=sum(z)
                mean1=sum1/len(z)
                count=0
                for i in z:
                    ad=(i-mean1)**2
                    count +=ad
                std1=(count/len(z))**0.5
                stdl.append(self.np.round(std1,5))
    #             print('The "Standard deviation" of array is >>\n',np.round(std1,5))
        stdl1=self.np.array(stdl)
        stdl1=stdl1.reshape(1,len(stdl1))
        df3=self.pd.DataFrame(stdl1,index=['Std Deviation'],columns=self.c)
#         print(df)
        return df3
    def var(self):
        varl=[]
        for i in self.array1.columns:
             if self.array1[i].dtype!=object:
                z=self.np.sort(self.array1[i])
                sum1=sum(z)
                mean1=sum1/len(z)
                count=0
                for g in z:
                    ad=(g-mean1)**2
                    count +=ad
                std1=(count/len(z))**0.5
                var1=std1**2
                varl.append(self.np.round(var1,4))
    #             print('The "Varienace" of array is >>\n',np.round(var1,4))
        varl1=self.np.array(varl)
        varl1=varl1.reshape(1,len(varl1))
        df2=self.pd.DataFrame(varl1,index=['Varience'],columns=self.c)
        return df2
    def maximun(self):
        maxl=[]
        for i in self.array1.columns:
             if self.array1[i].dtype!=object:
                z=self.np.sort(self.array1[i])
                m=self.np.max(z)
                maxl.append(m)
    #             print('The "Max" of array is >>\n',m)
        maxl1=self.np.array(maxl)
        maxl1=maxl1.reshape(1,len(maxl1))
        df2=self.pd.DataFrame(maxl1,index=['Max'],columns=self.c)
        return df2
    def minimum(self):
        minl=[]
        for i in self.array1.columns:
             if self.array1[i].dtype!=object:
                z=self.np.sort(self.array1[i])
                m=self.np.min(z)
                minl.append(m)
    #             print('The "Max" of array is >>\n',m)
        minl1=self.np.array(minl)
        minl1=minl1.reshape(1,len(minl1))
        df2=self.pd.DataFrame(minl1,index=['Min'],columns=self.c)
        return df2
    def describe(self):
        d6=self.mean()
        d5=self.median()
        d4=self.mode()
        d3=self.std()
        d2=self.var()
        d1=self.maximun()
        d0=self.minimum()
        df1=pd.concat([d6,d5,d4,d3,d2,d1,d0])
        return df1
if __name__=="__main__":      
    s=StatsPandas(df)
    # a=s.mean()
    # print(a)
    # print('*'*50)
    # b=s.median()
    # print(b)
    # print('*'*50)
    # c=s.mode()
    # print(c)
    # print('*'*50)
    # d=s.std()
    # print(d)
    # print('*'*50)
    # e=s.var()
    # print(e)
    # print('*'*50)
    # s.maximun()
    # print('*'*50)
    Z=s.describe()
    print(Z)