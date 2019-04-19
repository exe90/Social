#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

@author exe90


"""
from django.urls import path
from .views import BasePageView

urlpatterns = [
    path('', BasePageView.as_view())
]