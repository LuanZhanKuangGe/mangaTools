import os
import os.path
from gooey import Gooey, GooeyParser

@Gooey(
    program_name='IwaraTools',
    image_dir='./',
    language="chinese")

def main():
    parser = GooeyParser(description='AV生成网页, 配合油猴脚本使用.')
    parser.add_argument('input', help="选择目标文件夹", widget='DirChooser')
    parser.add_argument('output', help="选择目标文件夹", widget='DirChooser')
    return parser.parse_args()

if __name__ == '__main__':
    args = main()

    input = args.input + r'\\'
    output = args.output + r'\\av.html'

    fo = open(output, "w", encoding="utf-8")

    fo.write("<html>\n")

    fo.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
    fo.write("<body>\n")

    for root, dirs, files in os.walk(input, topdown=False):
        for name in files:
            if name.endswith(".nfo"):
                fo.write("<p>"+name.split(" ")[0]+"</p>\n")

    fo.write("</body>\n")
    fo.write("</html>\n")

    fo.close()

    print("完成, 请查看" + output )