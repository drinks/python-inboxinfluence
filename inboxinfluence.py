""" Python library for interacting with the Influence Explorer Text API.

"""

__author__ = "Dan Drinkard <ddrinkard@sunlightfoundation.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2011 Sunlight Labs"
__license__ = "BSD"

import urllib, urllib2
try:
    import json
except ImportError:
    import simplejson as json

class InboxInfluenceError(Exception):
    """ Exception for API errors """

class InboxInfluence404(Exception):
    """ Not found exception for empty responses """

class InboxInfluenceResponse(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.__dict__)

class inboxinfluence(object):
    apikey = None

    @staticmethod
    def contextualize(text):
        if inboxinfluence.apikey is None:
            raise InboxInfluenceError('Missing Sunglight apikey. Get one at services.sunlightlabs.com')

        url = 'https://inbox.influenceexplorer.com/contextualize?apikey=%s&text=%s' % (inboxinfluence.apikey, urllib.quote(text))
        try:
            resp = json.loads(urllib2.urlopen(url).read())
            if not resp['entities']:
                raise InboxInfluence404('No matches for input')

            objs = []
            for entity in resp['entities']:
                objs.append(InboxInfluenceResponse(**entity))

            return objs

        except urllib2.HTTPError as e:
            raise InboxInfluenceError(e)
        except ValueError as e:
            raise InboxInfluenceError(e)
