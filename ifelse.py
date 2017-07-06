name = input('What\'s your name my dear?')
weight = float(input('input your weight in kg:'))
height = float(input('input your height in meters:'))
BMI = weight/(height**2)
if BMI<18.5:
    result= '过轻'
elif BMI>=18.5 and BMI<25:
    result = '正常'
elif BMI>=25 and BMI<28:
    result = '过重'
elif BMI>=28 and BMI<32:
    result = '肥胖'
else:
    result = '严重肥胖'
    

print(name,',','你的BMI指数是:%.1f,因此你被鉴定为%s' %(BMI,result))
