from django.db import models
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _, ugettext


try:
    from picklefield import PickledObjectField
except ImportError:
    raise ImproperlyConfigured("Couldn't find the the 3rd party app "
                               "django-picklefield which is required for "
                               "the constance database backend.")


class Constance(models.Model):
    key = models.CharField(_('key'), max_length=255, unique=True)
    value = PickledObjectField(_('value'))

    class Meta:
        verbose_name = _('constance')
        verbose_name_plural = _('constances')
        db_table = 'constance_config'

    def __unicode__(self):
        return u'{} ({})'.format(ugettext(settings.CONSTANCE_CONFIG[self.key][1]), self.key)
