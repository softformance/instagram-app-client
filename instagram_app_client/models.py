# -*- coding: utf-8 -*-
from future.utils import python_2_unicode_compatible
from solo.models import SingletonModel
from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = [
    'GlobalInstagramFeedSetings',
]

@python_2_unicode_compatible
class GlobalInstagramFeedSetings(SingletonModel):
    """
    Global instagram feed settings singleton.
    """
    stream_enabled = models.BooleanFiled(
        verbose_name=_(u'Enable instagram feed'),
        help_text=_('Enable/disable instagram feed site-wide'),
        default=True,
    )
    stream_url = models.URLField(
        verbose_name=_(u'Instagram feed URL'),
        default='http://stream.dillysocks.com/',
    )

    def __str__(self):
        return _(u'Global Instagram Feed Settings')
