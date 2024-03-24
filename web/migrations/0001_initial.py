# Generated by Django 4.2.6 on 2024-03-24 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollageInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collage', models.CharField(max_length=32, verbose_name='学院')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tid', models.CharField(max_length=64, verbose_name='项目编号')),
                ('title', models.CharField(max_length=32, verbose_name='项目名称')),
                ('owner', models.CharField(max_length=32, verbose_name='负责人')),
                ('file', models.FileField(max_length=128, upload_to='File/', verbose_name='相关文件')),
                ('collage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.collageinfo', verbose_name='学院')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(blank=True, max_length=32, null=True, verbose_name='账号')),
                ('password', models.CharField(blank=True, max_length=64, null=True, verbose_name='密码')),
                ('email', models.CharField(blank=True, max_length=32, null=True, verbose_name='邮箱')),
                ('username', models.CharField(max_length=16, verbose_name='姓名')),
                ('collage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.collageinfo', verbose_name='学院')),
                ('roles', models.ManyToManyField(blank=True, to='rbac.role', verbose_name='拥有的所有角色')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='跟进日期')),
                ('note', models.TextField(verbose_name='跟进内容')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.task', verbose_name='所跟进项目')),
            ],
        ),
    ]
