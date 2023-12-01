from woocommerce import API

wcapi = API(
    # url="https://pansen.pl/wp-json/wc/v3/products",
    url="https://pansen.pl/",
    consumer_key="ck_dd7d33a3f2b409aef01bfd03839a24685f3bca3e",
    consumer_secret="cs_bf2e809afe8597fd1d3cfa2b54b8153f1b5cbb35",
    version="wc/v3"
)

for _ in range(3):
    # Your code here
    # print("This is loop iteration", _ + 1)


    data = {
        "name": "Olimp Creatine",
        "type": "simple",
        "regular_price": "129.99",
        "EAN": "43632583569547",
        "description": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.",
        "short_description": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.",
        "categories": [
            {
                "id": 9
            },
            {
                "id": 14
            }
        ],
        "images": [
            {
                "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_2_front.jpg"
            },
            {
                "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_2_back.jpg"
            }
        ]
    }

    print(wcapi.post("products", data).json())