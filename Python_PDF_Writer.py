# -*- coding: utf-8 -*- 
import os
import fitz

file_path = os.path.abspath('.')+"\\file\\"
#"C:\\Users\\liumingye\\Desktop\\Python_PDF_Writer\\file\\"
print (file_path)
# os.listdir(file)会历遍文件夹内的文件并返回一个列表
path_list = os.listdir(file_path)
# print(path_list)
# 定义一个空列表,我不需要path_list中的后缀名
path_name=[]
# 利用循环历遍path_list列表并且利用split去掉后缀名
for i in path_list:
    path_name.append(i.split(".")[0])


for i in path_name:
  a =  file_path+i+".pdf"
  print (a)
  doc = fitz.open(a)
  totaling = doc.pageCount
  print (totaling)
  for pg in range(totaling):
    page = doc[pg]
  #page = doc[1]
    rect = fitz.Rect(300, 50, 550, 200) 
    text = i
    print (page)
    rc = page.insertTextbox(rect, text, fontsize = 25, # choose fontsize (float)
                   fontname = "Times-Roman",       # a PDF standard font
                   fontfile = None,                # could be a file on your system
                   align = 2)                      # 0 = left, 1 = center, 2 = right
    print (a)
    doc.saveIncr()
#111.pdf
#EH5-2-2.pdf