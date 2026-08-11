import scrapy


class OmvicDealersSpider(scrapy.Spider):
    name = "omvic_dealers"
    allowed_domains = ["omvic.ca"]

    def start_requests(self):
        url = (
            "https://www.omvic.ca/dealer-search/"
            "?dealership_city=Toronto&search_type=dealership"
        )

        yield scrapy.Request(
            url,
            callback=self.parse,
            meta={
                "zyte_api_automap": {
                    "browserHtml": True,
                }
            },
        )

    def parse(self, response):
        text = response.xpath(
            "//body//text()[normalize-space()]"
        ).getall()

        clean_text = [
            x.strip()
            for x in text
            if x.strip()
        ]

        yield {
            "page_title": response.css("title::text").get(),
            "url": response.url,
            "sample_page_text": clean_text[-200:],
        }
