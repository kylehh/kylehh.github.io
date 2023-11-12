import argparse
import os
PREFIX="23-"
SUFFIX=".md"
IMG_PRE="assets/images/"
IMG_SUF="_files/"

### python new_entry.py -n 12-23-blog-title
### will generate _posts/23-12-23-blog-title.md
### and a folder assets/images/23-12-23-blog-title_files
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "-n", "--name", type=str, default="23-00-00-name", help="Test frame name"
    )
    args = parser.parse_args()
    post_name = PREFIX + args.name + SUFFIX
    imgf_name = IMG_PRE + PREFIX + args.name + IMG_SUF

    os.system(f"cp _posts/23-09-15-CORS.md _posts/{post_name}")
    os.mkdir(imgf_name)