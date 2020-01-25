#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""
Define WiFi Profile.
"""

from .const import *


class Profile(object):
    def __init__(self):
        self.id = 0
        self.auth = AUTH_ALG_OPEN
        self.akm = [AKM_TYPE_NONE]
        self.cipher = CIPHER_TYPE_NONE
        self.ssid = None
        self.bssid = None
        self.key = None

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self)

    def __str__(self):
        return '%s object (%s)' % (self.__class__.__name__, self.ssid)

    def process_akm(self):
        if len(self.akm) > 1:
            self.akm = self.akm[-1:]

    def __eq__(self, profile):
        if profile.ssid:
            if profile.ssid != self.ssid:
                return False

        if profile.bssid:
            if profile.bssid != self.bssid:
                return False

        if profile.auth:
            if profile.auth != self.auth:
                return False

        if profile.cipher:
            if profile.cipher != self.cipher:
                return False

        if profile.akm:
            if set(profile.akm).isdisjoint(set(self.akm)):
                return False

        return True
