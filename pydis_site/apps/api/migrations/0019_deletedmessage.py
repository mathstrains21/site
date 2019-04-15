# Generated by Django 2.1.1 on 2018-11-18 20:26

import pydis_site.apps.api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_messagedeletioncontext'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedMessage',
            fields=[
                ('id', models.BigIntegerField(help_text='The message ID as taken from Discord.', primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(limit_value=0, message='Message IDs cannot be negative.')])),
                ('channel_id', models.BigIntegerField(help_text='The channel ID that this message was sent in, taken from Discord.', validators=[django.core.validators.MinValueValidator(limit_value=0, message='Channel IDs cannot be negative.')])),
                ('content', models.CharField(help_text='The content of this message, taken from Discord.', max_length=2000)),
                ('embeds', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(validators=[pydis_site.apps.api.models.bot.tag.validate_tag_embed]), help_text='Embeds attached to this message.', size=None)),
                ('author', models.ForeignKey(help_text='The author of this message.', on_delete=django.db.models.deletion.CASCADE, to='api.User')),
                ('deletion_context', models.ForeignKey(help_text='The deletion context this message is part of.', on_delete=django.db.models.deletion.CASCADE, to='api.MessageDeletionContext')),
            ],
            options={
                'abstract': False,
            },
            bases=(pydis_site.apps.api.models.ModelReprMixin, models.Model),
        ),
    ]
