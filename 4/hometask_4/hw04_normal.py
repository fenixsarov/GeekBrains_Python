# Задание-1:
# Вывести символы в нижнем регистре, которые окружают 1 или более символа в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
# Разделитель
print(40*'=','\nЗадание-1:\n')

import re

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp' \
       'PLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANv' \
       'IoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkp' \
       'YOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
       'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAb' \
       'fCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyA' \
       'xDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFN' \
       'IsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
       'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZC' \
       'nZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxy' \
       'GPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXi' \
       'UWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'
# Можно для наглядности проверки использовать сначала короткую строку
# test = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkg'

pattern = r'[:upper:]*[a-z]{1,}[:upper:]*'

print(re.findall(pattern, line))

# Задание-2:
# Вывести символы в верхнем регистре, которые окружают ровно два символа в нижнем регистре слева
# и два символа в верхнем регистре справа. Решить задачу двумя способами: с помощью re и без.
# Т.е. из строки "sGAMkgAYEOmHBSQs" нужно получить ['GAM', 'EO']
# Разделитель
print(40*'=','\nЗадание-2:\n')

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp' \
       'PLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANv' \
       'IoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkp' \
       'YOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
       'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAb' \
       'fCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyA' \
       'xDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFN' \
       'IsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
       'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZC' \
       'nZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxy' \
       'GPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXi' \
       'UWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

# Задание 2 написано явно с ошибкой, либо некорректно сформулировано
# В комментариях писали, что проконсультировавшись с Вами, решили, что из строки test должно получиться
#  "GAMkgAYEO -> kgAY , если это так, то решение приведено ниже

# test = 'sGAMkgAYEOmHBSQs'
pattern_2 = r'[a-z]{2}[A-Z]{2}[A-Z]{0,}?'

print(re.findall(pattern_2, line_2))

# Задача-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла) произвольными целыми
# числами, в результате в файле должно быть 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр в вышезаполненном файле.
# Разделитель
print(40*'=','\nЗадание-3:\n')

from random import randint

nums = [randint(0, 9) for x in range(25)]
nums_str = ''

for i in nums:
       nums_str+=str(i)

file = open('file.txt', 'w')
file.write(nums_str)
file.close()

# Вот просто для примера вывел строчку с числами, далее он находит только каких цифр последовательно больше всего
# а как вывести саму последовательность пока не понял...(
test1 = '428481399999930224048356888888881790'
pattern_3 = r'(\d)\1{2,}'

print(re.findall(pattern_3, test1))



