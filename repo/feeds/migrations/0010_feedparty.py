# Generated by Django 3.1.5 on 2023-02-05 09:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_accountparty_party'),
        ('feeds', '0009_auto_20230204_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedParty',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='피드 파티 중개 테이블 pk')),
                ('state', models.CharField(blank=True, choices=[('subscribe', '구독'), ('unsubscribe', '구독취소')], default='subscribe', max_length=12, null=True)),
                ('feed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='feed_party', to='feeds.feed')),
                ('party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='feed_party', to='accounts.party')),
            ],
            options={
                'verbose_name': '4.3.2 피드, 파티 관계 정보',
                'verbose_name_plural': '4.3.2 피드, 파티 관계 정보',
                'unique_together': {('feed', 'party')},
            },
        ),
    ]
