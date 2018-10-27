# Запись в файл


with open ('unicode2000.txt', 'wb') as f:
    f.write(b''.join([chr(v).encode('utf-8') for v in range(33, 2001)]))