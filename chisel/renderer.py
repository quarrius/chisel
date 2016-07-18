#!/usr/bin/env python2
# -*- coding: utf-8 -*-

class AbstractRenderer(object):
    def _init_canvas(self):
        pass

    def render(self):
        pass

class IsometricChunkRenderer(AbstractRenderer):
    pass

class OverheadChunkRenderer(AbstractRenderer):
    pass

class OverheadHeightmap(OverheadChunkRenderer):
    pass

