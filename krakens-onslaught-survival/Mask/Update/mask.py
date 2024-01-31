from PIL import Image


def convert_to_mask(input_path, output_path):
    img = Image.open(input_path)
    img = img.convert("RGBA")
    data = img.getdata()

    new_data = []
    for item in data:
        r, g, b, a = item

        # Set pixels with transparent alpha values to black
        if a == 0:
            new_data.append((0, 0, 0, 255))  # Transparent background to black
        # Convert pixels with RGB values between (235, 235, 235) and (245, 245, 245) to black
        elif (237 <= r <= 247) and (237 <= g <= 247) and (237 <= b <= 247):
            new_data.append((0, 0, 0, a))  # Convert to black while keeping alpha
        else:
            new_data.append(item)  # Keep non-transparent pixels unchanged

    img.putdata(new_data)
    img.save(output_path, "PNG")


def main():
    for i in range(10):
        input_path = f"kraken_frame_{i}.png"
        output_path = f"kraken_frame_{i}_mask.png"

        convert_to_mask(input_path, output_path)
        print(f"Converted {input_path} to {output_path}")


if __name__ == "__main__":
    main()
