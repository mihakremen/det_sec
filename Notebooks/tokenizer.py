import nltk
import string
import csv
import pandas as pd
import nltk.data


#функция для проверки, являются ли символы латиницей:
def check_ascii(text):
    for each_char in text:
        if each_char not in string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation:
            return False
    else:
        return True


def tokenization(file_text):
    tokens = []
    #разбивка на токены:
    for line in open(file_text, encoding='utf8'):
        tokens += nltk.word_tokenize(str(line))
    #Очистка от знаков препинания:
    tokens = [i for i in tokens if (i not in string.punctuation)]
    #Очистка от лишних символов:
    tokens = [i.replace("'", "").replace("`", "").replace("=", "").replace("/", "").replace("\\", "").replace("-", "")
          .replace(':', '').replace('|', '') for i in tokens]
    #Очистка от пустых элементов и элементов длинной <= 3:
    tokens = [i for i in tokens if len(i) > 3 and len(i) < 20]
    return tokens


#Загрузка в DataFrame Pandas:
df = pd.DataFrame(tokens)
df = df.rename(columns={0: 'Input'})
#Удаление дубликатов и нулевых значений
df = df.drop_duplicates()
df.dropna()
df = df.reset_index(drop=True)
#Удаление фреймов с не латинскими символами:
df['not ascii'] = df['Input'].apply(check_ascii)
df = df[df['not ascii'] == True]
df.drop('not ascii', axis=1, inplace=True)
df = df.reset_index(drop=True)
#Ограничение по количеству фреймов:
df = df.loc[::5]
df = df.reset_index(drop=True)
df = df.head(490983)
#Добавление столбца Target с нулевыми значениями:
df = df.assign(Target=0)
print(df)
#Сохранение в файл csv:
#df.to_csv('useful_data(less).csv',index=False)
