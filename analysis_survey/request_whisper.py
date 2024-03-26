import openai
import json
import os
from pydub import AudioSegment, silence

# Открытие файла с ключем openai
with open('config.json', 'r') as file:
    config = json.load(file)
    openai.api_key = config['openai']


def transcribe_audio(audio_parts):
    transcriptions = ""
    for i, part in enumerate(audio_parts):
        # Проверяем длительность фрагмента
        if len(part) < 1000:
            # Пропускаем слишком короткие фрагменты
            continue
        else:
            # Создаем временный файл для фрагмента
            temp_audio_file = f"temp_audio_{i}.wav"
            part.export(temp_audio_file, format="wav")

            # Выполняем транскрибацию для этого фрагмента
            with open(temp_audio_file, "rb") as audio_file:
                transcript = openai.Audio.transcribe(
                    file=audio_file,
                    model="whisper-1",
                    response_format="text",
                    language="uk"
                )
                print(transcript)  # Выводим транскрипцию на экран
                transcriptions += transcript

            # Удаляем временный файл после использования
            os.remove(temp_audio_file)
    print(transcriptions)
    return transcriptions



def split_audio(input_audio_file, min_silence_len, silence_thresh=-50, padding_duration=100):

    # Загрузка аудиозаписи
    audio = AudioSegment.from_file(input_audio_file)

    # Определение интервалов тишины
    silence_intervals = silence.detect_silence(audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh)

    # Разрезание аудиофайла на части по интервалам тишины
    parts = []
    start = 0
    for silence_start, silence_end in silence_intervals:
        # Добавляем аудиофрагмент с увеличенной дополнительной длительностью времени
        part = audio[start:silence_start] + AudioSegment.silent(duration=padding_duration)
        parts.append(part)
        start = silence_end

    # Добавление последней части
    parts.append(audio[start:])

    return parts

