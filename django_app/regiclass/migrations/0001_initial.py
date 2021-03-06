# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 09:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location1', models.CharField(max_length=20)),
                ('location2', models.CharField(max_length=20)),
                ('location_option', models.CharField(choices=[('direct', '협의후결정'), ('custom', '직접입력')], default='direct', max_length=6)),
                ('location_detail', models.CharField(blank=True, max_length=20, null=True)),
                ('location_etc_type', models.CharField(choices=[('yes', '예'), ('no', '아니오')], default='yes', max_length=3)),
                ('location_etc_text', models.CharField(blank=True, max_length=20, null=True)),
                ('class_weekday', models.CharField(choices=[('mon', '월'), ('tue', '화'), ('wed', '수'), ('thu', '목'), ('fri', '금'), ('sat', '토'), ('sun', '일')], default='mon', max_length=3)),
                ('class_time', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curriculum_photo', models.ImageField(blank=True, null=True, upload_to='class/images/%Y/%m/%d')),
                ('curriculum_desc', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=24)),
                ('class_day', models.CharField(max_length=8)),
                ('class_time', models.CharField(max_length=24)),
                ('level', models.CharField(blank=True, choices=[('beginner', '입문자'), ('intermediate', '초중급자'), ('advanced', '상급자')], max_length=12)),
                ('career', models.CharField(blank=True, max_length=36)),
                ('to_tutor', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('pay_method', models.CharField(blank=True, choices=[('credit', '신용카드'), ('bankbook', '무통장입금')], max_length=12)),
                ('remitter', models.CharField(blank=True, max_length=24)),
                ('due_date', models.CharField(blank=True, max_length=36, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('hbn', '헬스&뷰티'), ('lang', '외국어'), ('com', '컴퓨터'), ('mna', '음악 / 미술'), ('sports', '스포츠'), ('major', '전공 / 취업'), ('hobby', '이색취미')], max_length=10)),
                ('class_type', models.CharField(choices=[('onetoone', '1:1수업'), ('group', '그룹수업'), ('oneday', '원데이')], max_length=10)),
                ('min_member', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], max_length=1, null=True)),
                ('max_member', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], max_length=1, null=True)),
                ('cover_photo', models.ImageField(upload_to='class/cover/%Y/%m/%d')),
                ('tutor_intro', models.CharField(max_length=100)),
                ('class_intro', models.CharField(max_length=100)),
                ('target_intro', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
                ('basic_class_time', models.CharField(blank=True, max_length=10, null=True)),
                ('total_count', models.CharField(blank=True, max_length=10, null=True)),
                ('youtube_url1', models.CharField(blank=True, max_length=100, null=True)),
                ('youtube_url2', models.CharField(blank=True, max_length=100, null=True)),
                ('region_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('notice', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(choices=[('editing', '작성중'), ('activity', '활동중')], default='editing', max_length=10)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LecturePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_photo', models.ImageField(upload_to='class/images/%Y/%m/%d')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecture_photos', to='regiclass.Lecture')),
            ],
        ),
        migrations.CreateModel(
            name='LikeLecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regiclass.Lecture')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curriculum_rate', models.IntegerField(default=0)),
                ('delivery_rate', models.IntegerField(default=0)),
                ('preparation_rate', models.IntegerField(default=0)),
                ('kindness_rate', models.IntegerField(default=0)),
                ('punctually_rate', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='regiclass.Lecture')),
            ],
            options={
                'ordering': ['-modify_date'],
            },
        ),
        migrations.AddField(
            model_name='lecture',
            name='like_users',
            field=models.ManyToManyField(related_name='like_lecture', through='regiclass.LikeLecture', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lecture',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Tutor'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='lecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment_lecture', to='regiclass.Lecture'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='lecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curriculum', to='regiclass.Lecture'),
        ),
        migrations.AddField(
            model_name='classlocation',
            name='lecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='regiclass.Lecture'),
        ),
        migrations.AlterUniqueTogether(
            name='likelecture',
            unique_together=set([('user', 'lecture')]),
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together=set([('user', 'lecture')]),
        ),
    ]
