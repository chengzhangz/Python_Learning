import urllib.request
import urllib
from lxml import etree


def get_url_html(url):
    user_header = {"User-Agent":
                       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
                    "Connection": "keep-alive",
                    "Cookie":
                        'bid=2wQs1fKOGio; __yadk_uid=uC1WJoIwVMhpiBHhynCxOisra1Tiq46l; gr_user_id=369fd8f4-a88c-4df9-953f-264abb88d368; _vwo_uuid_v2=087CFDD48FE16824A1ACB0D68B5AA440|69ba7b97d6bcf26a65c3b64f53b16e88; viewed="5908727_3227098_1477390_4199741_5387402"; ll="118163"; ap=1; _ga=GA1.2.169048868.1515319145; ue="1007679366@qq.com"; __utmv=30149280.8848; push_noty_num=0; ps=y; __utmz=30149280.1526045442.29.24.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; push_doumail_num=0; ct=y; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1526199909%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dm1RJF1Ywae8WCTdp8ttvPqzBG79q636oncIZXYN4Kzc-YgsaCf0cbYXmNX-DZsMY%26wd%3D%26eqid%3Dbfe3588b000187c8000000035af7f661%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.169048868.1515319145.1526098872.1526199924.35; __utmc=30149280; __utmt=1; dbcl2="88488555:SxST0UtL/q0"; ck=EcFi; _pk_id.100001.8cb4=3b36a070c79df4d3.1515319145.26.1526200410.1526100120.; __utmb=30149280.46.1.1526200410294'   
                       }
    request = urllib.request.Request(url, headers=user_header)
    response = urllib.request.urlopen(request)
    return response.read()


def write_image(image_name, image):
    # 获取网页中帖子的帖子名 作者 回应数量 最后回应的时间
    with open("./image/" + image_name + ".jpg", "wb") as f:
        f.write(image)


def list_to_dict(title, author, id):
    i = 0
    dict = {}
    for each_title in title:
        full_title = each_title + str(id)
        id += 1
        dict[full_title] = author[i]
        i += 1
    return dict, id


def main():
    url = "https://www.douban.com/group/haixiuzu/discussion?start="
    page = 0
    count = 0
    my_dict = {}
    while page < 3774:
        full_url = url + str(page * 25)
        print(full_url)
        html = get_url_html(full_url)
        content = etree.HTML(html)

        title = content.xpath('//table[@class="olt"]/tr/td[@class="title"]/a/@title')
        author = content.xpath('//table[@class="olt"]/tr/td[@nowrap="nowrap"]/a/text()')
        html_list = content.xpath('//table[@class="olt"]/tr/td[@class="title"]/a/@href')
        print("----->1、title, author")
        # print(title)
        # print(author)
        # my_dict, count = list_to_dict(title, author, count)
        print("----->2、html_list")
        # print(html_list)
        # add_title_author
        for each_html_addr in html_list:
            # 获取每个帖子的信息
            each_content = get_url_html(each_html_addr)
            new_content = etree.HTML(each_content)


            # 获取图片的url
            image_link = new_content.xpath('//div[@class="image-wrapper"]/img/@src')
            print("+++++++")
            if len(image_link):
                for each_image_link in image_link:
                    print("---->3、image link")
                    print(each_image_link)
                    # 取图片的url
                    image = get_url_html(each_image_link)
                    write_image(each_image_link[-10:-3], image)
            else:
                print("---->4、no image link")
        page += 1


if __name__ == "__main__":
    main()