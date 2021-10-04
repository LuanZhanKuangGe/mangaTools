import os
import os.path
from gooey import Gooey, GooeyParser

@Gooey(
    program_name='IwaraTools',
    image_dir='./',
    language="chinese")

def main():
    parser = GooeyParser(description='漫画收藏生成网页, 配合油猴脚本使用.')
    parser.add_argument('input', help="选择目标文件夹", widget='DirChooser')
    parser.add_argument('output', help="选择目标文件夹", widget='DirChooser')
    return parser.parse_args()

if __name__ == '__main__':
    args = main()

    input = args.input + r'\\'
    output = args.output + r'\\manga.html'

    fo = open(output, "w", encoding="utf-8")

    fo.write("<html>\n")

    fo.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
    fo.write("<body>\n")

    for files in os.listdir(input):
        if files.endswith(".zip") or files.endswith(".rar"):
            fo.write("<p>"+files.replace(".zip","")+"</p>\n")

    fo.write("</body>\n")
    fo.write("</html>\n")

    fo.close()

    print("完成, 请查看" + output )