import ebooklib
from ebooklib import epub
from ebooklib.utils import debug
from bs4 import BeautifulSoup
import os
import json

def split_epub_by_chapter(epub_path):
    """

    :param epub_path:
    :return:
    """

    # 读取EPUB文件
    book = epub.read_epub(epub_path)

    # 提取目录
    chapters = []
    for item in book.get_items_of_type(ebooklib.ITEM_IMAGE):
        print(item)