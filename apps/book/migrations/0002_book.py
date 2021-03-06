# Generated by Django 3.1 on 2021-03-21 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=32, verbose_name='书名')),
                ('publisher_state', models.IntegerField(choices=[(1, '发行中'), (2, '已发行')], verbose_name='出版社状态')),
                ('price', models.FloatField(default=69, verbose_name='价格')),
                ('remark', models.TextField(verbose_name='评论')),
                ('authors', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('publisher', models.ForeignKey(default=28, on_delete=django.db.models.deletion.DO_NOTHING, to='book.publisher', verbose_name='出版社')),
            ],
            options={
                'verbose_name': '图书',
                'verbose_name_plural': '图书',
            },
        ),
    ]
