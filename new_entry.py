import argparse
import os
PREFIX="25-"
SUFFIX=".md"
IMG_PRE="assets/2025/"
IMG_SUF="_files/"

### python new_entry.py -n -i 12-23-blog-title
### will generate _posts/2024/24-12-23-blog-title.md
### and a folder assets/2024/24-12-23-blog-title_files
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "-n", "--name", type=str, default="25-00-00-name", help="Test frame name"
    )
    parser.add_argument(
            "-i", "--image", action='store_true', help="if adding image folder"
    )
    args = parser.parse_args()
    post_name = PREFIX + args.name + SUFFIX
    imgf_name = IMG_PRE + PREFIX + args.name + IMG_SUF

    os.system(f"cp _posts/2025/25-06-20-1st.md _posts/2025/{post_name}")
    if args.image:
        os.mkdir(imgf_name)
