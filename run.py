def process_video(input_file, output_file):
    # Искомая сигнатура WEBM
    signature = b'\x1A\x45\xDF\xA3'
    
    # Читаем входной файл
    with open(input_file, 'rb') as f:
        data = f.read()
    
    # Ищем позицию сигнатуры WEBM
    start_pos = data.find(signature)
    
    if start_pos == -1:
        print("WEBM сигнатура не найдена")
        return
    
    # Обрезаем начало до сигнатуры
    video_data = data[start_pos:]
    
    # Находим последний ненулевой байт
    end_pos = len(video_data) - 1
    while end_pos > 0 and video_data[end_pos] == 0:
        end_pos -= 1
    
    # Обрезаем нули в конце
    video_data = video_data[:end_pos + 1]
    
    # Сохраняем результат
    with open(output_file, 'wb') as f:
        f.write(video_data)
    
    print(f"Готово! Сохранено в {output_file}")

# Укажите пути к файлам
input_file = 'input.bin'  # Исходный файл
output_file = 'output.webm'  # Результат

process_video(input_file, output_file)