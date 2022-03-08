'''
一、請製作大樂透,從1~49數字中抽出7個不重複號碼(6個普通號碼+1特別號)
二、判斷獎項次數(頭獎、二獎、三獎、四獎、五獎、六獎、七獎、普獎)
三、產生中獎號碼 (6個基本號碼,1個特別號),並算出中獎機率
    1、頭獎 ○○○○○○ 六個獎號全中(不包含特別號)
    2、二獎 ○○○○○● 對中任五個獎號及特別號
    3、三獎 ○○○○○ 對中任五個獎號 
    4、四獎 ○○○○● 對中任四個獎號及特別號
    5、五獎 ○○○○ 對中任四個獎號
    6、六獎 ○○○●對中任三個獎號及特別號
    7、七獎 對中任兩個獎號及特別號 
    8、普獎 對中任三個獎號
    nums = [1,2,3,55,66,77,99]
    print(nums[2:])
    print(nums[:4])
    print(nums[:])
    print(nums[1:4])
'''
import random
nums_range = [x for x in range(1, 50)]

count =[0, 0, 0, 0, 0, 0, 0, 0, 0]

while count[-1] < 100:
    chosen_nums = random.sample(nums_range, 7)
    print(f'開獎號碼：{chosen_nums}')
    buyer_nums = random.sample(nums_range, 6)
    print(f'買家投注號碼：{buyer_nums}')
    normal_num = chosen_nums[:6] #6個普通號
    special_num = chosen_nums[6] #特別號 
    
    count[-1] += 1
    
    if len(set(normal_num) & set(buyer_nums)) == 6:
        count[0] += 1
        
    elif len(set(normal_num) & set(buyer_nums)) == 5 and special_num in buyer_nums:
        count[1] += 1
        
    elif len(set(normal_num) & set(buyer_nums)) == 5 :
        count[2] += 1
        
    elif len(set(normal_num) & set(buyer_nums)) == 4 and special_num in buyer_nums:
        count[3] += 1
        
    elif len(set(normal_num) & set(buyer_nums)) == 4 :
        count[4] += 1
       
    elif len(set(normal_num) & set(buyer_nums)) == 3 and special_num in buyer_nums:
        count[5] += 1
        
    elif len(set(normal_num) & set(buyer_nums)) == 2 and special_num in buyer_nums:
        count[6] += 1
        
    elif len(set(normal_num) & set(buyer_nums)) == 3 :
        count[7] += 1

print(f'共中{sum(count[:-1])}次，中獎機率為：{sum(count[:-1])/count[-1]:.2%}')
print(f'恭禧您中{count[0]}次頭獎, 中頭獎機率為：{count[0]/(count[-1]):.2%}')
print(f'恭禧您中{count[1]}次二獎, 中二獎機率為：{count[1]/(count[-1]):.2%}')
print(f'恭禧您中{count[2]}次三獎, 中三獎機率為：{count[2]/(count[-1]):.2%}')
print(f'恭禧您中{count[3]}次四獎, 中四獎機率為：{count[3]/(count[-1]):.2%}')
print(f'恭禧您中{count[4]}次五獎, 中五獎機率為：{count[4]/(count[-1]):.2%}')
print(f'恭禧您中{count[5]}次六獎, 中六獎機率為：{count[5]/(count[-1]):.2%}')
print(f'恭禧您中{count[6]}次七獎, 中七獎機率為：{count[6]/(count[-1]):.2%}')
print(f'恭禧您中{count[7]}次普獎, 中八獎機率為：{count[7]/(count[-1]):.2%}')