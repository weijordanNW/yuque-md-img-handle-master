---
title: "语雀md文档的图片转化"
icon: "tool"
subtitle: "python"
date: 2024-10-23 10:52:27
isOriginal: true
category:
  - python
tag:
  - 工具脚本
---


:::info
<font style="color:rgb(64, 72, 91);">语雀导出markdown之后，图片链接仍然指向语雀的CDN，如果我们想发布到别的平台或者本地离线查看的话，不太方便。使用本工具可以将图片下载灵活存储到本地后，对应修改markdown文件中的链接指向。支持上传的图片(png)和生成的思维导图(jpeg)</font>

:::

打开控制台



python3 main.py fileName  就行



[main.py](https://www.yuque.com/attachments/yuque/0/2024/py/45821596/1729675444109-e349fc00-f953-4199-a21e-1c1e4e6e7196.py)

```javascript
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
    # filepath = '/Users/yang/SoftWare/knowledge-base/docs/yuque/' + sys.argv[1] + "/"
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
```



[README.md](https://www.yuque.com/attachments/yuque/0/2024/md/45821596/1729676185636-c582382b-360b-4f43-8af3-67c91c20c554.md)

```javascript
# yuque-md-img-handle

语雀导出markdown之后，图片链接仍然指向语雀的CDN，如果我们想发布到别的平台或者本地离线查看的话，不太方便。使用本工具可以将图片下载灵活存储到本地后，对应修改markdown文件中的链接指向。支持上传的图片(png)和生成的思维导图(jpeg)。

# 用法

基础

```shell
python3 main.py fileName 
```

> 1. 首先将下载的语雀原始md文件放在D:/yuque_change/yuque-md-img-handle-master/md/下 路径可以在main.py文件中修改
> 2. 执行 python3 main.py fileName
> 3. main会将原始md文件中的图片爬去下来，存放的路径是原始文件所在的文件夹下的images目录下
> 4. 并且在此目录下生成一个名为new_fileName.md的文件，该文件里边的图片指向就是刚才爬去的图片
> 5. 至此就可以完成需求。。。。
> 6. 但是我为了方便，生成新文件后，我将原始文件删除，并把新文件改名成原始的文件名
> 7. 这样就做到将语雀导出的md文件中的图片转换处成本地指向的路径

示例

```
python3 D:/yuque_change/yuque-md-img-handle-master/main.py fileName
```



如果没有安装python环境,

打开通过百度网盘分享的文件：python

链接：[https://pan.baidu.com/s/1nEvDrNWvT4LICmoCCxyv6A?pwd=tw1o](https://pan.baidu.com/s/1nEvDrNWvT4LICmoCCxyv6A?pwd=tw1o) 

提取码：tw1o

进行安装



视频教程:[PyThon环境搭建](https://www.bilibili.com/video/BV1ey411h7Wd?spm_id_from=player_end_recommend_autoplay&vd_source=ac6ab4c3cdc5d0193edf55fd77ba0b4f)

