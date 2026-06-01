import os
import re
import base64
import mimetypes

def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    mime_type, _ = mimetypes.guess_type(image_path)
    if not mime_type:
        mime_type = "image/jpeg"
    return f"data:{mime_type};base64,{encoded_string}"

def embed_images(html_file, output_file, base_dir):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find url('images/...')
    url_pattern = re.compile(r"url\(['\"]?(images/[^'\"]+)['\"]?\)")
    
    # Find <img src="images/...">
    img_pattern = re.compile(r"src=['\"](images/[^'\"]+)['\"]")

    def replace_url(match):
        img_path = match.group(1)
        full_path = os.path.join(base_dir, img_path)
        if os.path.exists(full_path):
            return f"url('{get_base64_encoded_image(full_path)}')"
        return match.group(0)

    def replace_img(match):
        img_path = match.group(1)
        full_path = os.path.join(base_dir, img_path)
        if os.path.exists(full_path):
            return f"src='{get_base64_encoded_image(full_path)}'"
        return match.group(0)

    content = url_pattern.sub(replace_url, content)
    content = img_pattern.sub(replace_img, content)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    base_dir = '/Users/emiliorodrigocarreiravillalta/Desktop/tributosceuta-overview'
    html_file = os.path.join(base_dir, 'index.html')
    output_file = os.path.join(base_dir, 'index-standalone.html')
    embed_images(html_file, output_file, base_dir)
    print(f"Generated {output_file}")
