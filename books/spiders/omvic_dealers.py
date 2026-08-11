import scrapy


class OmvicDealersSpider(scrapy.Spider):
    name = "omvic_dealers"
    allowed_domains = ["omvic.ca"]

    start_urls = [
        "https://www.omvic.ca/dealer-search/?dealership_city=Toronto&search_type=dealership"
    ]

    def parse(self, response):
        self.logger.info("OMVIC page loaded: %s", response.url)

        yield {
            "page_title": response.css("title::text").get(),
            "url": response.url,
            "dealer_names_found": response.xpath(
                "//*[contains(@class,'dealer') or contains(@class,'result')]//text()"
            ).getall()[:20],
        }
