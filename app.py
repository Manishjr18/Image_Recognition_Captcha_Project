# # import os
# # import random
# # from flask import Flask, jsonify, request, render_template

# # app = Flask(__name__)

# # # Example image categories and paths
# # image_categories = {
# #     "animals": ["static/images/animal1.jpg", "static/images/animal2.jpg", "static/images/animal3.jpg"],
# #     "buildings": ["static/images/building1.jpg", "static/images/building2.jpg", "static/images/building3.jpg"],
# #     "nature": ["static/images/nature1.jpg", "static/images/nature2.jpg", "static/images/nature3.jpg"],
# # }

# # @app.route('/generate_captcha')
# # def generate_captcha():
# #     sample_category = random.choice(list(image_categories.keys()))
# #     sample_image = random.choice(image_categories[sample_category])
# #     captcha_images = []

# #     for category, images in image_categories.items():
# #         if category == sample_category:
# #             captcha_images.extend(images)  # Ensure all images from the sample category are included
# #         else:
# #             captcha_images.append(random.choice(images))  # Add one random image from each other category

# #     random.shuffle(captcha_images)

# #     response = {
# #         "captcha_id": sample_category,
# #         "sample_image": sample_image,
# #         "captcha_images": captcha_images
# #     }
# #     return jsonify(response)

# # @app.route('/verify_captcha', methods=['POST'])
# # def verify_captcha():
# #     data = request.get_json()
# #     captcha_id = data['captcha_id']
# #     user_selection = data['user_selection']

# #     correct_images = set(image_categories[captcha_id])
# #     selected_images = set(user_selection)

# #     if correct_images == selected_images:
# #         result = "Captcha Verified Successfully"
# #     else:
# #         result = "Captcha Verification Failed"

# #     return jsonify({"result": result})

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # if __name__ == '__main__':
# #     app.run(debug=True)


# import os
# import random
# from flask import Flask, jsonify, request, render_template

# app = Flask(__name__)

# # Example image categories and paths
# image_categories = {
#     "animals": ["static/images/animal1.jpg", "static/images/animal2.jpg", "static/images/animal3.jpg"],
#     "buildings": ["static/images/building1.jpg", "static/images/building2.jpg", "static/images/building3.jpg"],
#     "nature": ["static/images/nature1.jpg", "static/images/nature2.jpg", "static/images/nature3.jpg"],
# }

# def generate_captcha_images(sample_category):
#     captcha_images = []
#     other_categories = [cat for cat in image_categories.keys() if cat != sample_category]
    
#     # Add 3 random images from the sample category
#     captcha_images.extend(random.sample(image_categories[sample_category], 3))
    
#     # Add 5 random images from other categories
#     for category in other_categories:
#         captcha_images.extend(random.sample(image_categories[category], 2))
    
#     # Ensure we have exactly 8 images
#     random.shuffle(captcha_images)
#     return captcha_images[:8]

# @app.route('/generate_captcha')
# def generate_captcha():
#     sample_category = random.choice(list(image_categories.keys()))
#     sample_image = random.choice(image_categories[sample_category])
#     captcha_images = generate_captcha_images(sample_category)

#     response = {
#         "captcha_id": sample_category,
#         "sample_image": sample_image,
#         "captcha_images": captcha_images
#     }
#     return jsonify(response)

# @app.route('/verify_captcha', methods=['POST'])
# def verify_captcha():
#     data = request.get_json()
#     captcha_id = data['captcha_id']
#     user_selection = data['user_selection']

#     correct_images = set(image_categories[captcha_id])
#     selected_images = set(user_selection)

#     if correct_images == selected_images:
#         result = "Captcha Verified Successfully"
#     else:
#         result = "Captcha Verification Failed"

#     return jsonify({"result": result})

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)


import os
import random
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Example image categories and paths
image_categories = {
    "animals": ["static/images/animal1.jpg", "static/images/animal2.jpg", "static/images/animal3.jpg"],
    "buildings": ["static/images/building1.jpg", "static/images/building2.jpg", "static/images/building3.jpg"],
    "nature": ["static/images/nature1.jpg", "static/images/nature2.jpg", "static/images/nature3.jpg"],
}

def generate_captcha_images(sample_category):
    captcha_images = []
    other_categories = [cat for cat in image_categories.keys() if cat != sample_category]
    
    # Add 3 random images from the sample category
    captcha_images.extend(random.sample(image_categories[sample_category], 3))
    
    # Add 5 random images from other categories
    for category in other_categories:
        captcha_images.extend(random.sample(image_categories[category], 2))
    
    # Add one more random image from the remaining images if the total is less than 8
    if len(captcha_images) < 8:
        remaining_images = []
        for category in other_categories:
            remaining_images.extend([img for img in image_categories[category] if img not in captcha_images])
        remaining_images.extend([img for img in image_categories[sample_category] if img not in captcha_images])
        captcha_images.append(random.choice(remaining_images))
    
    random.shuffle(captcha_images)
    return captcha_images[:8]

@app.route('/generate_captcha')
def generate_captcha():
    sample_category = random.choice(list(image_categories.keys()))
    sample_image = random.choice(image_categories[sample_category])
    captcha_images = generate_captcha_images(sample_category)

    response = {
        "captcha_id": sample_category,
        "sample_image": sample_image,
        "captcha_images": captcha_images
    }
    return jsonify(response)

@app.route('/verify_captcha', methods=['POST'])
def verify_captcha():
    data = request.get_json()
    captcha_id = data['captcha_id']
    user_selection = data['user_selection']

    correct_images = set(image_categories[captcha_id])
    selected_images = set(user_selection)

    if correct_images == selected_images:
        result = "Captcha Verified Successfully"
    else:
        result = "Captcha Verification Failed"

    return jsonify({"result": result})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
