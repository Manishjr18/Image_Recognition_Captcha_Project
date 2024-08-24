# Image Recognition Captcha

**CAPTCHA Generation**

Storage:
A number of random images will be pre-stored in the database categorically (relevant to the image).

Random Image Selection:
Select random images from the stored images to be shown as a sample image and images to be shown for validation.

CAPTCHA Creation:
The selected random images will be displayed as a sample image and the collection of images that have to be validated based on the sample image.

**CAPTCHA Validation**

User Input:
Capture the user's input for the CAPTCHA.

Comparison:
Compare the user's input with the stored correct CAPTCHA validation result.

Response:
Return a success or failure response based on the comparison.
