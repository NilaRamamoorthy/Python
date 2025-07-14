# 3. Image Pixel Color Analyzer
pixels = [(255, 0, 0), (0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 0, 0)]
red_count = pixels.count((255, 0, 0))
print("Red pixel count:", red_count)
region = pixels[1:4]
print("Subregion pixels:", region)
