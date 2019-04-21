# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from yandexnlp.items import PhoneReviews

__author__ = 'Daniel Abramov  github.com/RiskofStorm'


class MarketReviewsSpider(scrapy.Spider):
    name = 'market_reviews'
    allowed_domains = ['market.yandex.ru']

    def __init__(self):
        super().__init__()
        self.domain = 'http://market.yandex.ru'
        self.start_urls = [self.domain + page for page in open('ym_phones_urls.txt', 'r').read().split('\n')]

    def parse(self, response):
        data = BeautifulSoup(response.text, 'lxml')
        review_page = None
        for link in data.select('a.link.n-smart-link.i-bem'):
            if link.text.startswith('Отзывы'):
                review_page = link.get('href')
        if review_page:
            yield scrapy.Request(self.domain + review_page, callback=self.parse_review_page)

    # TODO: solve crawler block, handle saving data
    def parse_review_page(self, response):
        data = BeautifulSoup(response.text, 'lxml')
        parse = data.select('div.n-product-review-item')
        item = PhoneReviews()

        full_revs = [" ".join([j.text for j in i.select('dd.n-product-review-item__text')]) for i in parse]

        rating_revs = [1 if float(i.text) > 3 else 0 for i in data.select('div.rating__value')]

        item['reviews'] = full_revs
        item['marks'] = rating_revs

        yield item

        next_review_page = next(iter(data.select('a.n-pager__button-next')), None)
        if next_review_page:
            yield scrapy.Request(self.domain + next_review_page.get('href'), callback=self.parse_review_page)









