# Virtual-Currency-API
암호화폐 정보들을 다루는 API

## How to use
### PyPI
~~~
pip install coinapi
~~~

~~~
from coinapi import CoinAPI
print(CoinAPI().get_by_page(1))
print(CoinAPI().get_by_marketcap_rank(108))
print(CoinAPI().get_by_name('Bitcoin'))
~~~
#### get_by_page(page)
page를 기반으로 코인 정보를 list로 불러옵니다. 시장가치 순위를 기준으로 100개씩 나뉩니다. rank, abbreviation, name, marketcap, price, circulating_supply, volume, change 데이터가 있습니다.
~~~
print(CoinAPI().get_by_page(1))
~~~
[{'rank': 1, 'abbreviation': 'BTC', 'name': 'Bitcoin', 'marketcap': '$70,844,339,907', 'price': '$4266.88', 'circulating_supply': '16,603,312 BTC', 'volume': '$1,102,490,000', 'change': '-1.06%'}, {'rank': 2, 'abbreviation': 'ETH', 'name': 'Ethereum', 'marketcap': '$27,903,567,340', 'price': '$293.89', 'circulating_supply': '94,946,263 ETH', 'volume': '$264,006,000', 'change': '1.16%'}, ...]

#### get_by_marketcap_rank(rank)
시장가치 순위를 기반으로 코인 정보를 dict로 불러옵니다.
~~~
print(CoinAPI().get_by_rank(197))
~~~
{'rank': 197, 'abbreviation': 'GAM', 'name': 'Gambit', 'marketcap': '$12,292,688', 'price': '$10.29', 'circulating_supply': '1,194,555 GAM', 'volume': '$184,562', 'change': '-19.16%'}

#### get_by_name(name)
이름으로 코인 정보를 dict로 불러옵니다.
~~~
print(CoinAPI().get_by_name('ripple))
~~~
{'rank': 3, 'abbreviation': 'XRP', 'name': 'Ripple', 'marketcap': '$7,800,441,130', 'price': '$0.203434', 'circulating_supply': '38,343,841,883 XRP', 'volume': '$41,334,100', 'change': '1.68%'}
