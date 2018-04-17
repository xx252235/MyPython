def text_create(name,msg):
    file_path = "D://"
    file_type = ".txt"
    file_full_path = file_path + name + file_type
    file = open(file_full_path,"w")
    file.write(msg)
    file.close()
    print("Done")

def text_filter(word,a_word = "fuck",b_word = "fXXk"):
    return word.replace(a_word,b_word)
# text_create("xinxu","Hello World!")
# file = open("D://xinxu.txt","w")
print(text_filter("fuck you"))

