from vectorizer import convert_image_to_vector

if __name__ == "__main__":
    input_path = "image_path"
    svg_file, ai_file = convert_image_to_vector(
        input_path,
        save_svg=True,
        save_ai=True
    )
    if svg_file:
        print(f"SVG file created: {svg_file}")
    if ai_file:
        print(f"AI file created: {ai_file}")