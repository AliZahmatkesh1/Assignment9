from colorama import *
init()
""" You need to install the colorama library
    Install the library
    Type in CMD ( pip install colorama )
"""
def error(m = None):
    print (Style.BRIGHT+Fore.RED+m+Style.RESET_ALL + Fore.RESET)
def matn(m = None) :
    print (Style.BRIGHT+Fore.LIGHTBLACK_EX+m+Style.RESET_ALL+ Fore.RESET)
def title(m = None) :
    print (Style.BRIGHT+Fore.BLUE+m+Style.RESET_ALL+ Fore.RESET)
# data
class Data :
    def __init__(self,y, m, d):
        self.y = y
        self.m = m
        self.d = d

    def show(self):
        if len(str(self.y)) == 1 :
            self.y = "0"+str(self.y)
        if len(str(self.m)) == 1 :
            self.m = "0"+str(self.m)
        if len(str(self.d)) == 1 :
            self.d = "0"+str(self.d)

        title(str(self.y)+" / "+str(self.m)+" / "+str(self.d))
        t = Data.GetMonthName(self)
        title(t)

    def GetMonthName(self) :
        
        if self.m == "01" :
            return "Farvardin"
        elif self.m == "02" :
            return "Ordibehesht"
        elif self.m == "03" :
            return "Khordad"
        elif self.m == "04" :
            return "Tir"
        elif self.m == "05" :
            return "Mordad"
        elif self.m == "06" :
            return "Shahrivar"
        elif self.m == "07" :
            return "Mehr"
        elif self.m == "08" :
            return "Aban"
        elif self.m == "09" :
            return "Azar"
        elif self.m == 10 :
            return "Dey"
        elif self.m == 11 :
            return "Bahman"
        elif self.m == 12 :
            return "Esfand"
        else :
            return ""

    def IsValidDate(self) :
        if 0 <= self.d <= 30 and 0 <= self.m <= 12 and 0 <= self.y <= 9999 :
            return True
        else :
            return False

    def sum(self, a):

        result = Data(None ,None ,None)

        s1 = ""
        s2 = ""
        sal1 = str(a.y)
        sal2 = str(self.y)
        if sal1 > sal2 :
            for r in range(len(sal1)) :
                if sal1[r] != sal2[r] :
                    s1 += str(sal1[r])
                    s2 += str(sal2[r])
        else :
            for r in range(len(sal2)) :
                if sal1[r] != sal2[r] :
                    s1 += str(sal1[r])
                    s2 += str(sal2[r])

        if s1 == "" or s2 == "" :
            result.y = 0
        else :
            result.y = int(s1) + int(s2)
        result.m = self.m + a.m
        result.d = self.d + a.d
        while True :
            if result.d >= 30:
                result.d -= 30
                result.m += 1
            else : break

        while True :
            if result.m >= 12:
                result.m -= 12
                result.y += 1
            else : break

        return result

    def sub(self, a):

        result = Data(None, None, None)

        if self.y > a.y :
            result.y = self.y - a.y
            result.m = self.m - a.m
            result.d = self.d - a.d
        else :
            result.y = a.y - self.y
            result.m = a.m - self.m
            result.d = a.d - self.d

        while True :
            if result.d < 0:
                result.d += 30
                result.m -= 1
            else : break
        while True :
            if result.m < 0 :
                result.m += 12
                result.y -= 1
            else : break

        return result
    
    def menu () :
        while True :
            t1_y = int(input("\nEnter year 1   : ").strip())
            t1_m = int(input("Enter month 1 : ").strip())
            t1_d = int(input("Enter day 1   : ").strip())
            Data1 = Data(t1_y ,t1_m ,t1_d)
            a = Data1.IsValidDate()
            if a == True :
                break
            else :
                error("\nThis is not a date")
                error("Enter again")
                continue
        while True :
            t2_y = int(input("\nEnter year 2   : ").strip())
            t2_m = int(input("Enter month 2 : ").strip())
            t2_d = int(input("Enter day 2   : ").strip())
            Data2 = Data(t2_y ,t2_m ,t2_d)
            a = Data2.IsValidDate()
            if a == True :
                break
            else :
                error("\nThis is not a date")
                error("Enter again")
                continue
        result_sum = Data1.sum(Data2)
        result_sub = Data1.sub(Data2)
        while True :
            a = input("\nEnter | + | - | ALL | : ").strip().lower()

            if a == "+" :
                print("\n" , end= "")
                result_sum.show()
                break
            elif a == "-" :
                print("\n" , end= "")
                result_sub.show()
                break
            elif a == "all" :
                print("\n" , end= "")
                matn("SUM")
                result_sum.show()
                print("\n" , end= "")
                matn("SUB")
                result_sub.show()
                break
            else :
                error("\nInvalid input !")

# Time
class Time :
    def __init__(self,h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def show(self):
        if len(str(self.h)) == 1 :
            self.h = "0"+str(self.h)
        if len(str(self.m)) == 1 :
            self.m = "0"+str(self.m)
        if len(str(self.s)) == 1 :
            self.s = "0"+str(self.s)

        title(str(self.h)+" : "+str(self.m)+" : "+str(self.s))

    def sum(self, t):

        result = Time(None ,None ,None)

        result.h = self.h + t.h
        result.m = self.m + t.m
        result.s = self.s + t.s

        while True :
            if result.s >= 60:
                result.s -= 60
                result.m += 1
            else : break

        while True :
            if result.m >= 60:
                result.m -= 60
                result.h += 1
            else : break

        return result

    def sub(self, t):

        result = Time(None, None, None)

        if self.h > t.h :
            result.h = self.h - t.h
            result.m = self.m - t.m
            result.s = self.s - t.s
        else :
            result.h = t.h - self.h
            result.m = t.m - self.m
            result.s = t.s - self.s

        while True :
            if result.s < 0:
                result.s += 60
                result.m -= 1
            else : break
        while True :
            if result.m < 0 :
                result.m += 60
                result.h -= 1
            else : break

        return result
    
    def Sec_time (self) :
        m = 0
        h = 0
        while True :
            if self.s >= 60 :
                self.s -= 60
                m += 1
            else : break

        while True :
            if m >= 60 :
                m -= 60
                h += 1
            else : break

        result = Time(h, m, self.s)

        """ or
        result = Time(None, None, None)
        h = self.s / 3600
        h_m = str(h).split(".")
        result.h = int(h)
        m = float("0."+h_m[1]) * 60
        m_s = str(m).split(".")
        result.m = int(m)
        s = float("0."+m_s[1]) * 60
        result.s = int(s)
        """
        
        
        return result


    def Time_sec (self) :
        
        sec = ((self.h * 60) + self.m ) * 60 + self.s
        
        """ or
        sec = self.h * 3600
        sec += self.m * 60
        sec += self.s
        """
        return sec

    def menu () :
        while True :
            matn ("\n1. Sum & Sub Time")
            matn ("2. Convert seconds to time")
            matn ("3. Convert time to seconds")
            matn ("0. Back")
            v = int(input("Enter namber : ").strip())

            if v == 0 :
                break
            elif v == 1 :

                t1_h = int(input("\nEnter hour time 1   : ").strip())
                while True :
                    t1_m = int(input("Enter minute time 1 : ").strip())
                    if 0 <= t1_m <= 60 :
                        break
                    else :
                        error("\n0 to 60\n")
                
                while True :
                    t1_s = int(input("Enter Second time 1 : ").strip())
                    if 0 <= t1_s <= 60 :
                            break
                    else :
                        error("\n0 to 60\n")

                t2_h = int(input("\nEnter hour time 2 : ").strip())
                while True :
                    t2_m = int(input("Enter minute time 2 : ").strip())
                    if 0 <= t2_m <= 60 :
                            break
                    else :
                        error("\n0 to 60\n")
                
                while True :
                    t2_s = int(input("Enter Second time 2 : ").strip())
                    if 0 <= t2_s <= 60 :
                            break
                    else :
                        error("\n0 to 60\n")
                time1 = Time(t1_h ,t1_m ,t1_s)
                time2 = Time(t2_h ,t2_m ,t2_s)
                result_sum = time1.sum(time2)
                result_sub = time1.sub(time2)

                while True :
                    a = input("\nEnter | + | - | ALL | : ").strip().lower()

                    if a == "+" :
                        print("\n" , end= "")
                        result_sum.show()
                        break
                    elif a == "-" :
                        print("\n" , end= "")
                        result_sub.show()
                        break
                    elif a == "all" :
                        print("\n" , end= "")
                        matn("SUM")
                        result_sum.show()
                        print("\n" , end= "")
                        matn("SUB")
                        result_sub.show()
                        break
                    else :
                        error("\nInvalid input !")

            elif v == 2 :
                t1_s = int(input("\nEnter Second : ").strip())

                time1 = Time(None ,None ,t1_s)
                t = time1.Sec_time()
                print("\n" , end= "")
                t.show()


            elif v == 3 :
                t1_h = int(input("\nEnter hour time 1   : ").strip())
                while True :
                    t1_m = int(input("Enter minute time 1 : ").strip())
                    if 0 <= t1_m <= 60 :
                        break
                    else :
                        error("\n0 to 60\n")
                
                while True :
                    t1_s = int(input("Enter Second time 1 : ").strip())
                    if 0 <= t1_s <= 60 :
                            break
                    else :
                        error("\n0 to 60\n")
                
                time1 = Time(t1_h ,t1_m ,t1_s)
                title("\n"+str(time1.Time_sec())+" Second")

            else :
                error("\nInvalid input !")

# Fraction
class Fraction:
    def __init__(self, s, m):
        self.soorat = s
        self.makhraj = m

    def show(self):
        title(str(self.soorat)+" / "+str(self.makhraj))

    def mul(self, a):
        result = Fraction(None , None)
        result.soorat = self.soorat * a.soorat
        result.makhraj = self.makhraj * a.makhraj
        return result

    def sum(self, a):
        result = Fraction(None , None)
        result.soorat = (self.soorat * a.makhraj)+(self.makhraj * a.soorat)
        result.makhraj = self.makhraj * a.makhraj
        return result

    def sub(self, a):
        result = Fraction(None, None)
        result.soorat = (self.soorat * a.makhraj)-(self.makhraj * a.soorat)
        result.makhraj = self.makhraj * a.makhraj
        return result

    def div(self, a):
        result = Fraction(None ,None)
        result.soorat = self.soorat * a.makhraj
        result.makhraj = self.makhraj * a.soorat
        return result

    def menu () :
        soret1 = int(input("\nnumerator 1   : ").strip())
        makhraj1 = int(input("denominator 1 : ").strip())
        soret2 = int(input("\nnumerator 2   : ").strip())
        makhraj2 = int(input("denominator 2 : ").strip())
        fraction1 = Fraction(soret1 , makhraj1)
        fraction2 = Fraction(soret2 , makhraj2)
        while True :
            a = input("\nEnter | + | - | * | / | All | : ").strip().lower()
            if a == "+" :
                result_sum = fraction1.sum(fraction2)
                print("\n" , end= "")
                result_sum.show()
                break
            elif a == "-" :
                result_sub = fraction1.sub(fraction2)
                print("\n" , end= "")
                result_sub.show()
                break
            elif a == "*" :
                result_mul = fraction1.mul(fraction2)
                print("\n" , end= "")
                result_mul.show()
                break
            elif a == "/" :
                result_div = fraction1.div(fraction2)
                print("\n" , end= "")
                result_div.show()
                break
            elif a == "all" :
                result_sum = fraction1.sum(fraction2)
                result_sub = fraction1.sub(fraction2)
                result_mul = fraction1.mul(fraction2)
                result_div = fraction1.div(fraction2)
                print("\n" , end= "")
                matn("SUM")
                result_sum.show()
                print("\n" , end= "")
                matn("SUB")
                result_sub.show()
                print("\n" , end= "")
                matn("MUL")
                result_mul.show()
                print("\n" , end= "")
                matn("DIV")
                result_div.show()
                break
            else :
                error("\nInvalid input !")

def menu () :
    matn("""\n1. Fraction
2. Time
3. Date
0. Exit""")


while True :
    menu ()
    a = int(input("Enter namber : ").strip())
    if a == 0 :
        break
    elif a == 1 :
        Fraction.menu()
    elif a == 2 :
        Time.menu()
    elif a == 3 :
        Data.menu()
    else :
        error("\nInvalid input !")