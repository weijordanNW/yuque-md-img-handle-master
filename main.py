import re
import requests
import os
import sys

yuque_cdn_domain = 'cdn.nlark.com'
output_content = []
image_file_prefix = 'image-'

def main():
    fileName = sys.argv[1] + '.md'
    filepath = 'D:/yuque_change/yuque-md-img-handle-master/md/'  # 直接指向 md 文件夹
    # # filepath = '/Users/yang/SoftWare/knowledge-base/docs/yuque/' + sys.argv[1] + "/"
    # origin_md_path = sys.argv[1]
    origin_md_path = filepath + fileName
    # output_md_path = sys.argv[2]
    output_md_path = filepath + "new_" + fileName
    # image_dir = sys.argv[3]
    image_dir = filepath + "images/"
    # image_url_prefix = sys.argv[4]
    image_url_prefix = './images/'
    # image_rename_mode = sys.argv[5] # raw asc
    image_rename_mode = 'raw' # raw asc
    mkdir(image_dir)
    cnt = handler(origin_md_path, output_md_path, image_dir, image_url_prefix, image_rename_mode)
    print('处理完成, 共{}张图片'.format(cnt))
    print('准备删除语雀导出的原始文件{}'.format(fileName))
    os.remove(origin_md_path)
    print('删除语雀导出的原始文件成功')
    # 重命名文件
    os.rename(output_md_path, origin_md_path)


def mkdir(image_dir):
    isExists = os.path.exists(image_dir)
    if isExists:
        print('图片存储目录已存在')
    else:
        os.makedirs(image_dir)
        print('图片存储目录创建成功')


def handler(origin_md_path, output_md_path, image_dir, image_url_prefix, image_rename_mode):
    idx = 0
    with open(origin_md_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f.readlines():
            line = re.sub(r'png#(.*)+', 'png)', line)
            image_url = str(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',line))
            if yuque_cdn_domain in image_url:
                image_url = image_url.replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace("'", '')
                if '.png' in image_url:
                    suffix = '.png'
                elif '.jpeg' in image_url:
                    suffix = '.jpeg'
                download_image(image_url, image_dir, image_rename_mode, idx, suffix)
                to_replace = '/'.join(image_url.split('/')[:-1])
                new_image_url = image_url.replace(to_replace, 'placeholder')
                if image_rename_mode == 'asc':
                    new_image_url = image_url_prefix + image_file_prefix + str(idx) + suffix
                else:
                    new_image_url = new_image_url.replace('placeholder/',image_url_prefix)
                idx += 1
                line = line.replace(image_url, new_image_url)
            output_content.append(line)
    with open(output_md_path, 'w', encoding='utf-8', errors='ignore') as f:
        for _output_content in output_content:
            f.write(str(_output_content))
    return idx
            

def download_image(image_url, image_dir, image_name_mode, idx, suffix):
    r = requests.get(image_url, stream=True)
    image_name = image_url.split('/')[-1]
    if image_name_mode == 'asc':
        image_name = image_file_prefix + str(idx) + suffix
    if r.status_code == 200:
        open(image_dir+'/'+image_name, 'wb').write(r.content)
    del r

if __name__ == '__main__':
    main()