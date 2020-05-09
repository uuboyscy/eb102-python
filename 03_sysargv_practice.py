import sys

# 接收外部參數(List)
input_args = sys.argv
# print(input_args)

# 因為第零個是檔案名稱
input_args = input_args[1:]
output = 0
for i in input_args:
    output += int(i)
print(output)
