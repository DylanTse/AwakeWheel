import base64

def base64_to_image(base64_string, filename):
    try:
        # Decode base64 string to binary data
        binary_data = base64.b64decode(base64_string)
        
        # Write binary data to a file
        with open(filename, 'wb') as file:
            file.write(binary_data)
        
        print(f"Image saved as {filename}")
    except Exception as e:
        print("Error:", e)

# Example base64 string

with (open("base64.txt", "r")) as file:
    base64_string = file.readline().strip()
    filename = "image.jpg"  # Output filename

# Convert base64 to image
    base64_to_image(base64_string, filename)