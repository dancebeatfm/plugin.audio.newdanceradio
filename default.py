#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Copyright 2021 avg
#
#  This file is part of the newdanceradio xbmc plugin.
#
#  This plugin is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This plugin is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this plugin.  If not, see <http://www.gnu.org/licenses/>.


from os.path import join
from sys import argv
from time import gmtime, strftime, strptime
from urllib import quote_plus, urlopen
from urlparse import parse_qs, urlparse
from xml.dom.minidom import parseString
from xbmc import translatePath
import xbmcaddon
from xbmcaddon import Addon
from xbmcgui import Dialog, ListItem
from xbmcplugin import addDirectoryItem, endOfDirectory

NEWDANCERADIO_STREAM = 'http://stream.newdanceradio.ru/mp3_192'
my_addon = Addon('plugin.audio.newdanceradio')
class StreamPlayer:

    def __init__(self, url):
        self.url = url

    def addLink(self, name, url, image = '', info = {}, totalItems = 0):
        item = ListItem(name.encode('utf-8'), iconImage = image, thumbnailImage = image)
        item.setProperty('mimetype', 'audio/mpeg')
        item.setInfo('music', info)
        item.setArt({
            'thumb': my_addon.getAddonInfo('icon'),
            'icon': my_addon.getAddonInfo('icon'),
            'fanart': my_addon.getAddonInfo('fanart')
            })
        return addDirectoryItem(int(argv[1]), url, item, False, totalItems)

    def buildIndex(self):
        self.addLink('[COLOR orange][B]New Dance Radio[/B][/COLOR] [COLOR red] LIVE[/COLOR]', self.url, '', {
            'title': 'New Dance Radio',
        })

    def run(self, handle):
        endOfDirectory(int(handle))

if __name__ == '__main__':
    newdanceradio = StreamPlayer(NEWDANCERADIO_STREAM)
    newdanceradio.buildIndex()
    newdanceradio.run(argv[1])
