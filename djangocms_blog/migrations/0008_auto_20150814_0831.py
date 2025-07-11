from django.db import migrations

import djangocms_blog.models


class Migration(migrations.Migration):
    dependencies = [
        ("djangocms_blog", "0007_auto_20150719_0933"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posttranslation",
            name="abstract",
            field=djangocms_blog.models.HTMLField(default=b"", verbose_name="abstract", blank=True),
            preserve_default=True,
        ),
    ]
