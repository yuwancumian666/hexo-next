#! py -3
# -*- coding: utf-8 -*-

'''
脚本功能是将所有markdown文件中形如“{{ site.data.oss_images.word-cloud-sb2 }}”
Jekyll变量引用改为yaml文件中的图片链接，以解决hexo的语法不兼容问题（md中不能使用变量）
'''

import os
import re
import sys
import yaml

# os.chdir(sys.path[0])


def parse(string, yml_data):
    """
    找到 “{{ site.data.oss_images.word-cloud-sb2 }}” 对应的链接
    """
    image_key = re.sub(" }}", "", re.sub("{{.+\.", "", string))
    return yml_data[image_key]


def replace_year_book():
    yml = open("Hexo/moeext.github.io/source/_data/year_book/January.yml", 'r')
    md = open("Hexo/moeext.github.io/source/_posts/2019-01-19-first-month.markdown", 'r+')
    yml_data = yaml.load(yml)
    md_contents = md.read()
    for string in re.findall("{{ .+ }}", md_contents):
        md_contents = md_contents.replace(string, parse(string, yml_data))
        # print(string, parse(string))
    md.seek(0)
    md.write(md_contents)
    yml.close()
    md.close()

def parse_all():
    # 替换所有markdown文件中的“{{ site.data.oss_images.word-cloud-sb2 }}”为链接
    path = "Hexo/moeext.github.io/source/"
    file_list_md = os.listdir(path + "_posts")
    file_list_yml = os.listdir(path + "_data/post_images")
    yaml_data = {}
    for yml in file_list_yml:
        yaml_data.update(yaml.load(open(path+"_data/post_images/"+yml, 'r').read()))

    for file_md in file_list_md:
        with open(path+"_posts/"+file_md, 'r+') as f:
            md_content = f.read()
            for string in re.findall("{{ .+ }}", md_content):
                md_content = md_content.replace(string, parse(string, yaml_data))
            f.seek(0)
            f.write(md_content)

    

if __name__ == "__main__":
    parse_all()
