import subprocess

"""
print(str(os.system('taskkill /im chrome.exe /F')))
conhost.exe
chromedriver.exe
"""
# win10系统编码是gbk，pycharm全局编码是utf-8，导致控制台输出乱码，这里输出转码为gbk
end_process = subprocess.Popen(["taskkill", "/IM", "conhost.exe", "/F"], stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
out, error = end_process.communicate()
print(out.decode('gbk'))
