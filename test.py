import text_to_image

# encoded_image_path = text_to_image.encode("Hello World!", "image.png")
encoded_image_path = text_to_image.encode_file("test.txt", "output_image.png")

# decoded_text = text_to_image.decode("encoded_image.png")

decoded_file_path = text_to_image.decode_to_file("output_image.png", "output_text_file.txt")