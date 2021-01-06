import pyppeteer.chromium_downloader

print('默认版本是：{}'.format(pyppeteer.__chromium_revision__))
print('可执行文件默认路径：{}'.format(pyppeteer.chromium_downloader.chromiumExecutable.get('linux')))
print('win64平台下载链接为：{}'.format(pyppeteer.chromium_downloader.downloadURLs.get('linux')))
