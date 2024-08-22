import scrapy


class NoberoSpider(scrapy.Spider):
    name = "nobero_spider"
    allowed_domains = ["nobero.com"]
    start_urls = ["https://nobero.com/pages/men"]

    def parse(self, response):
        """Parse the main Men's page and extract all category links."""
        categories = self.extract_categories(response)
        for category_url, category_name in categories.items():
            yield response.follow(
                category_url,
                callback=self.parse_category,
                meta={"category_name": category_name},
            )

    def extract_categories(self, response):
        """Extract category URLs and their corresponding names from the URL."""
        category_links = response.css("div.custom-page-season-grid-item a::attr(href)").getall()
        categories = {
            link: self.extract_category_name(link)
            for link in category_links
        }
        return categories

    def extract_category_name(self, url):
        """Extract the category name from the URL."""
        return url.split("/")[-1].replace('-', ' ').capitalize()

    def parse_category(self, response):
        """Parse each category page and extract all product links."""
        category_name = response.meta["category_name"]
        product_links = self.extract_products(response)
        for product_url in product_links:
            yield response.follow(
                product_url,
                callback=self.parse_product,
                meta={"category_name": category_name},
            )

    def extract_products(self, response):
        """Extract product URLs from a category page."""
        return response.css("section.product-card-container a::attr(href)").getall()

    def parse_product(self, response):
        """Parse the product details page and extract product information."""
        category_name = response.meta["category_name"]
        item = {
            "category": category_name,
            "url": response.url,
            "title": self.extract_title(response),
            "last_7_day_sale": self.extract_last_7_day_sale(response),
            "available_skus": self.extract_skus(response),
            "fit": self.extract_fit(response),
            "fabric": self.extract_fabric(response),
            "neck": self.extract_neck(response),
            "sleeve": self.extract_sleeve(response),
            "pattern": self.extract_pattern(response),
            "length": self.extract_length(response),
            "description": self.extract_description(response),
            "image_url": self.extract_image_url(response),
        }
        yield item

    def extract_title(self, response):
        return response.css("h1.capitalize::text").get().strip()

    def extract_last_7_day_sale(self, response):
        return response.css("div.product_bought_count span::text").re_first(r"\d+")

    def extract_skus(self, response):
        colors = response.css("span#selected-color-title::text").getall()
        sizes = response.css("label.size-select::text").getall()
        skus = [
            {"color": color.strip(), "size": [size.strip() for size in sizes]}
            for color in colors
        ]
        return skus

    def extract_fit(self, response):
        return response.css("div.product-metafields-values:nth-child(1) p::text").get()

    def extract_fabric(self, response):
        return response.css("div.product-metafields-values:nth-child(2) p::text").get()

    def extract_neck(self, response):
        return response.css("div.product-metafields-values:nth-child(3) p::text").get()

    def extract_sleeve(self, response):
        return response.css("div.product-metafields-values:nth-child(4) p::text").get()

    def extract_pattern(self, response):
        return response.css("div.product-metafields-values:nth-child(5) p::text").get()

    def extract_length(self, response):
        return response.css("div.product-metafields-values:nth-child(6) p::text").get()

    def extract_description(self, response):
        description = response.css("div#description_content p::text").getall()
        return " ".join(description).strip()

    def extract_image_url(self, response):
         """Extract the main image URL from the product page."""
         return response.css("figure#image-container img::attr(src)").get()
