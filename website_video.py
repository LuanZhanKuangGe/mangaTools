from pathlib import Path, PurePath
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

    input = Path(args.input)
    output = Path(args.output) / 'av.html'

    with output.open("w", encoding="utf-8") as fo:
        fo.write("<html>\n")
        fo.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
        fo.write("<body>\n")

        for nfo in input.rglob('*.nfo'):
            fo.write("<p>"+nfo.name.split(" ")[0]+"</p>\n")

        fo.write("</body>\n")
        fo.write("</html>\n")

        fo.close()

    print("完成, 请查看" + output.name)