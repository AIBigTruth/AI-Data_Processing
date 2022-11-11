import os

# 获取目录下的要删除文件


def get_file(file_dir):
    lists = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if (os.path.splitext(file)[1] == '.txt' ):
                # 再那位仁兄的基础上加入这一句逻辑判断，首先筛选出srt后缀
                # 再选出不包含中文字幕的文件，也就是剩下所有字幕。
                lists.append(os.path.basename(file))
        print('文件名获取成功')
        return lists

# 批量删除文件
def removeFile():
    lists = get_file(path)
    for index in range(len(lists)):
        os.remove(path + lists[index])
    print('文件删除成功')

path = 'F://test/make label/12-fire-smoke-white-black-merge/label/'
removeFile()
