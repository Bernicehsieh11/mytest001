
#寫一個 Python 程式，請求使用者輸入一個數字，然後判斷它是否為偶數（被 2 整除）。如果是偶數，輸出 "是偶數"，否則輸出 "不是偶數"。

num = int(input('請輸入一個數字：'))
if num%2==0:
    print("是偶數")
else:
    print("不是偶數")


#創建一個包含五個整數的 Python 列表，然後遍歷該列表，並將每個整數加 10 後輸出。

intList = [2, 6, 2, 4, 8]
for i in range(len(intList)):
    intList[i] += 10  # 將每個整數加 10
print(intList)



#寫一個 Python 函數，接收一個字串作為參數，並回傳該字串的反轉版本。

s = "Sweat is the lubricant of success."

print(s[::-1])    



#請寫一個 Python 程式，將兩個數字相加並輸出結果。
def addnum(num1, num2):
    return num1 + num2

new_num = []

for i in range(2):
    test01 = int(input("請輸入數字："))
    new_num.append(test01)

sums = addnum(new_num[0], new_num[1])
print(sums)




