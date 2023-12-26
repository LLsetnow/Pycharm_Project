
import re

def format_question_v3(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    formatted_lines = []
    for line in lines:
        # 处理题目行
        if line.startswith('【单选题】'):
            formatted_lines.append('【单选题】\n')
        # 处理问题、选项和答案行
        elif line.strip() and not line.startswith('正确答案') and not line.startswith('我的答案'):
            # 为问题行添加编号
            if line.strip().isdigit():
                formatted_lines.append(line.strip() + '.')
            else:
                formatted_lines.append(line.strip() + '\n')
        # 处理正确答案行
        elif line.startswith('正确答案'):
            answer = line.split('：')[1].split(';')[0].strip()
            formatted_lines.append('正确答案： ' + answer + '\n')

    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(formatted_lines)

# 调用函数（假设文件存在）
# format_question_v3('test.txt', 'output.txt')



# 定义一个函数来检查字符串是否仅以数字开头
def starts_with_number(line):
    match = re.match(r'^\d+', line)
    return int(match.group()) if match else None

# 分割题型和题目主体
def split_question_type_and_content(line):
    split_index = line.find('】')
    if split_index != -1:
        return line[:split_index + 1], line[split_index + 1:]
    else:
        return None, line




def format_question(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    output_lines = []

    for line in lines:

        # 题号识别
        number = starts_with_number(line)
        if(number != None) :
            question_number = number

        # 题干识别
        if line.startswith('【单选题】'):
            split_question_type_and_content(line)
            question_type, content = split_question_type_and_content(line)
            print(question_type)
            print(content)

        if line.startswith('A、'):
            question_A = line
            print(question_A)

        if line.startswith('B、'):
            question_B = line
            print(question_B)

        if line.startswith('C、'):
            question_C = line
            print(question_C)

        if line.startswith('D、'):
            question_D = line
            print(question_D)







format_question('test.txt', 'output.txt')