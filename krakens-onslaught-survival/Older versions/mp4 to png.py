import os
from moviepy.editor import VideoFileClip
from PIL import Image


def mp4_to_png(input_file, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Load the video clip
    video_clip = VideoFileClip(input_file)

    # Set the counter for naming the PNG files
    frame_count = 0

    for frame in video_clip.iter_frames(fps=video_clip.fps):
        # Convert numpy array to PIL Image
        pil_image = Image.fromarray(frame)

        # Construct the output file name with the correct frame number
        output_file = f"{output_folder}/frame_{frame_count:04d}.png"

        # Save the frame as a PNG image
        pil_image.save(output_file)

        # Increment the frame counter
        frame_count += 1

        # Close the video clip
        video_clip.reader.close()

        # Check if the audio attribute is present before calling close_proc()
        if video_clip.audio is not None:
            video_clip.audio.reader.close_proc()

    if __name__ == "__main__":
        # Replace "kraken.mp4" with the path to your input MP4 file
        # Replace "kraken" with the folder where you want to save the PNG images
        mp4_to_png("kraken.mp4", "kraken")