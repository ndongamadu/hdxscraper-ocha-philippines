import logging


from hdx.hdx_configuration import Configuration
from os.path import join

from hdx.facades.simple import facade


logger = logging.getLogger(__name__)


def main():
    print('nothing do to yet')


if __name__ == '__main__':
    facade(main, hdx_site='demo',
           user_agent='HDXINTERNAL OCHA-Philippines scraper')
