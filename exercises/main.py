
import re
# Splitting the options into separate columns (A, B, C, D) in the DataFrame

# Function to split options into separate columns
def split_options(options):
    split_opt = options.split(' ')
    options_dict = {}
    for opt in split_opt:
        if opt.startswith('A.'):
            options_dict['A'] = opt[2:].strip()
        elif opt.startswith('B.'):
            options_dict['B'] = opt[2:].strip()
        elif opt.startswith('C.'):
            options_dict['C'] = opt[2:].strip()
        elif opt.startswith('D.'):
            options_dict['D'] = opt[2:].strip()
    return options_dict

# Applying the function to each row
df[['A', 'B', 'C', 'D']] = df.apply(lambda row: pd.Series(split_options(row['选项'])), axis=1)

# Dropping the old '选项' column
df = df.drop(columns=['选项'])

# Saving the updated DataFrame to an Excel file
updated_excel_file_path = '/mnt/data/毛概_questions_updated.xlsx'
df.to_excel(updated_excel_file_path, index=False)

updated_excel_file_path






format_question('test.txt', 'output.txt')