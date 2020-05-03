"""
获取文件扩展名
"""
def get_suffix(filename):
    """获取文件名的后缀名
    :param filename:文件名
    :return:文件的后缀名
    """
    #从字符串中你想查找.出现的位置
    pos = filename.rfind('.')
    #通过切片操作从文件名中取出后缀名
    return filename[pos + 1:] if pos > 0 else ''


print(get_suffix('readme.txt'))       # txt
print(get_suffix('readme.txt.md'))    # md
print(get_suffix('.readme'))          #
print(get_suffix('readme.'))          #
print(get_suffix('readme'))           #