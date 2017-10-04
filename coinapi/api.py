from urllib.request import urlopen
from bs4 import BeautifulSoup


class CoinAPI:
    def __init__(self):
        self._base_url = 'https://coinmarketcap.com/{0}{1}'
        # 페이지, 화폐단위(각각 1페이지와 USD는 생략)
        self._tag = ''
        # 화폐단위 태그(기본값 USD 생략)

        # resp = urlopen(self._base_url.format(''))
        # soup = BeautifulSoup(resp, 'html.parser')
        # stat count 부분 selenium으로 처리해야 함

    def change_currency_unit(self, currency_unit):
        """
        Changes currency unit

        :param currency_unit: Currency unit to change ex) USD, KRW, BTC, ...
        :type currency_unit: str

        :return: None
        :rtype: None
        """
        self._tag = currency_unit if currency_unit.upper() != 'USD' else ''

    def get_by_page(self, page=1):
        """
        Returns coin data based page. 100 coins per page.

        :param page: Page to inquire
        :type page: int

        :return: Coin data list
        :rtype: list
        """
        target_url = self._base_url.format('', self._tag) if page == 1 else self._base_url.format(page, self._tag)

        resp = urlopen(target_url)
        soup = BeautifulSoup(resp, 'html.parser')

        # Parsing
        coin_table = soup.find(class_='table', id='currencies').tbody
        # Table

        coins = list()
        # Coin list to return
        for coin_item in coin_table.find_all('tr'):
            # Find items
            coin_td = coin_item.find_all('td')
            coin_dict = dict()

            coin_dict['rank'] = int(coin_td[0].text.strip())
            coin_dict['abbreviation'] = coin_td[1].text.strip().split('\n')[0]
            coin_dict['name'] = coin_td[1].text.strip().split('\n')[1]
            coin_dict['marketcap'] = coin_td[2].text.strip()
            coin_dict['price'] = coin_td[3].text.strip()
            coin_dict['circulating_supply'] = '{0} {1}'.format(coin_td[4].text.strip().split('\n')[0], coin_dict['abbreviation'])
            coin_dict['volume'] = coin_td[5].text.strip()
            coin_dict['change'] = coin_td[6].text.strip()

            coins.append(coin_dict)

        return coins

    def get_by_marketcap_rank(self, rank):
        """
        Returns coin data based market cap rank.

        :param rank: rank to inquire
        :type rank: int

        :return: Coin data dict
        :rtype: dict
        """
        page = int(rank / 100 + 1)
        return [item for item in self.get_by_page(page) if item['rank'] == rank][0]

    def get_by_name(self, name):
        """
        Returns coin data based name.

        :param name: name to inquire
        :type name: str

        :return: Coin data dict
        :rtype: dict
        """
        for page in range(1, 12):
            items = self.get_by_page(page)
            for item in items:
                if item['name'].upper() == name.upper():
                    return item


if __name__ == '__main__':
    print(CoinAPI().get_by_name('gambit'))
