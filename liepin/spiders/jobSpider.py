# -*- coding: utf-8 -*-
import scrapy
from liepin.items import LiepinItem


class JobspiderSpider(scrapy.Spider):
    name = 'jobSpider'
    allowed_domains = ['liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/?isAnalysis=&dqs=070020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=python&init=-1&searchType=1&headckid=c8fe26f1d5c4100c&compkind=&fromSearchBtn=2&sortFlag=15&ckid=c8fe26f1d5c4100c&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=I-7rQ0e90mv8a37po7dV3Q%7Eb82XZEfT3k9nLaGd2nO5lg&d_sfrom=search_fp_bar&d_ckId=0204c3d67dcde098d56eb1e19dfd2eeb&d_curPage=98&d_pageSize=40&d_headId=50f1cda57340e9fccf14ec8aebad8d4b&curPage=0']

    def parse(self, response):
        print(response)
        title=response.css('title::text').extract_first()
        print(title)
        item=LiepinItem()
        positions=response.xpath('//div[@class="job-content"]/div[@class="sojob-result "]/ul[@class="sojob-list"]')
        ps=positions.xpath('//li')
        for p in ps:
            print(p)
            job_name = p.xpath('//div[@class="job-info"]/h3/a/text()').extract()
            for j in job_name:
                item['job']=j
                yield item





        #for po in positions:
            #print(po)
            #job_name=po.xpath('//li/div[@class="job-info"]/h3/a/text()')
            #job_desc=po.xpath('//li/div[@class="job-info"]/p/@title')
            #print('1111111')
            #print(job_desc)
            #print(job_name)




