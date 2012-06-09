"""Unit Tests for the socialprofile module"""

# pylint: disable=R0904

import unittest
from urllib import urlencode
from urllib2 import Request, urlopen
from django.utils import simplejson

#class OauthGoogleTestCase(unittest.TestCase):
#    """Tests Google Oauth for extra values, you need to look in user_auth tables for an access_token"""
#    def testGetUserData(self):
#        """Test user data from Google oauth"""
#        access_token = 'GETAFRESHONE'
#
#        user_info_url = "https://www.googleapis.com/oauth2/v1/userinfo"
#
#        data = {'access_token': access_token, 'alt': 'json'}
#        params = urlencode (data)
#        request = Request(user_info_url + '?' + params, headers={'Authorization': params})
#        result =  simplejson.loads(urlopen(request).read())
#
#        print result
#
#        print result['family_name']

class SocialProfileUrlsTestCase(unittest.TestCase):
    def test_redirect_urls(self):
        def testLoginRequiredRedirect(self):
            response = self.c.get('/secure/', follow=True)
            self.assertRedirects(response, "http://testserver/select/?next=/secure/")
