import os

def convert_video_to_audio(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        if file.endswith(".mp4"):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file.replace(".mp4", ".mp3"))

            os.system(f'ffmpeg -i "{input_path}" "{output_path}"')