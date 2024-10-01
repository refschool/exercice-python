import requests
image_url = "https://www.candidattitreprofessionnel.fr/uploads/2023/10/sized/pexels-fauxels-3184418-aspect-ratio-545-390-350x0.jpg"
img_data = requests.get(image_url).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)