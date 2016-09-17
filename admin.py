from django.contrib import admin

from clubm8core import models

admin.site.register([
    models.Tag,
    models.Event,
    models.Occurrence,
    models.SpecialOccurrence,
    models.Plan,
    models.Slot,
])
