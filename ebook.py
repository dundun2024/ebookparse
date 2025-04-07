from bs4 import BeautifulSoup, Tag
import requests
import json

chapter_url = "https://m.johere.com/jok/105701/16198502.html"

# 保存小说内容
book = {"id": "67f33e81998c4e7522d75a11", "title": "躺平：老婆修炼我变强韩风姜酥柔", "author": "万红壮"}
chapters = []
# 章节序号
chapter_number = 0
next_chapter_tag = True
# 当还有下一章时，循环执行
while next_chapter_tag:
    if isinstance(next_chapter_tag, Tag):
        chapter_url = "https:" + next_chapter_tag.get("href")
    try:
        response = requests.get(chapter_url)
        print(response.text)
        # print(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        # 定义章节
        chapter_number = chapter_number + 1
        chapter = {"chapter_number": chapter_number, "bookId": "67f33e81998c4e7522d75a11"}
        # 章节标题
        chapter_title = soup.find("body").find("header").find("div", attrs={"class": "zhong"})
        chapter["chapterTitle"] = chapter_title.text
        # 章节内容
        chapter_content_elements = soup.find("body").find("section").find("article").find_all("p")
        chapter_content = ""
        for element in chapter_content_elements:
            chapter_content = chapter_content + str(element)
        chapter["chapterContent"] = chapter_content
        chapters.append(chapter)

        # 获取下一章链接
        next_chapter_tag = soup.find("a", string="下一章")
    except Exception as e:
        print(f"发生异常：{e}")

try:
    with open("book.json", "w", encoding="UTF-8") as file:
        json.dump(chapters, file, ensure_ascii=False, indent=4)
except Exception as e:
    print(f"文件写入错误: {e}")
