import os
import os.path


rootdir = "./"
fo = open("manga.html", "w", encoding="utf-8")

fo.write("<html>\n")

fo.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
fo.write("<body>\n")

for files in os.listdir(rootdir):
    if files.endswith(".zip") or files.endswith(".rar"):
        fo.write("<p>"+files.replace(".zip","")+"</p>\n")

fo.write("</body>\n")
fo.write("</html>\n")

fo.close()

input("done")
