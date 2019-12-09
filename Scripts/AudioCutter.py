from pydub import AudioSegment
import os


# TODO test it
def create_samples(original_path, output_folder_path, output_file_name, count=0):
    sound = AudioSegment.from_file(original_path)
    size = len(sound)

    if size < 30:
        return

    for i in range(0, size, 30):
        if i + 30 > size:
            return

        clip = sound[i:i + 30]

        clip.export(output_folder_path + "/" + output_file_name + "-" + count + ".wav", format="wav")
        count += 1

        os.remove(original_path)
