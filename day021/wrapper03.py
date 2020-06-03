import time, random
from functools import wraps

class RecordTime:

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f'{func.__name__}执行时间：{end - start:.3f}秒')
            return result
        return wrapper

#使用装饰器语法糖加载装饰器
@RecordTime()
def download(filename):
    print(f'开始下载 {filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename} 下载完成.')

def upload(filename):
    print(f'开始上传 {filename}')
    time.sleep(random.randint(4, 8))
    print(f'{filename} 上传完成.')


#直接创建对象并调用对象传入被装饰的函数
upload = RecordTime()(upload)
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
