def check_unique(pair,matrix):
    exist=False
    for i in range(len(matrix)):
        if (pair[0]==matrix[i][1] and pair[1]==matrix[i][0]):
            exist=True
    return exist
pass_code=[]
unique_pair=[]
code_number=int(input('Кодовая цифра: '))
if 3<=code_number<=20:
    for i in range(1,code_number):
        for j in range(1,code_number):
            if code_number%(i+j)==0:
                un_pair=[i,j]
                check=check_unique(un_pair,pass_code)
                unique_pair=str(un_pair[1])+str(un_pair[0])
                if check==False and i!=j:
                    pass_code.append(un_pair)
            else:
                continue
else:
    print('Число должно быть в диапазоне от 3 до 20')
for i in range(len(pass_code)):
    pass_code[i]=str(pass_code[i][0])+str(pass_code[i][1])
print(*pass_code)