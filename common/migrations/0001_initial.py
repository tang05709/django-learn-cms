# Generated by Django 3.0.3 on 2020-03-19 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=255, verbose_name='广告位名称')),
                ('status', models.SmallIntegerField(choices=[[0, '正常'], [9, '禁用']], db_index=True, default=0, verbose_name='状态')),
            ],
            options={
                'db_table': 'adv_position',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('original_name', models.CharField(max_length=255, verbose_name='原始名称')),
                ('name', models.CharField(max_length=255, verbose_name='新名称')),
                ('url', models.CharField(max_length=255, verbose_name='图片存放地址')),
                ('status', models.SmallIntegerField(choices=[[0, '正常'], [9, '禁用']], db_index=True, verbose_name='状态')),
            ],
            options={
                'db_table': 'attachment',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=255, verbose_name='栏目名称')),
                ('module', models.CharField(choices=[['posts', '单页面'], ['article', '文章'], ['product', '产品']], max_length=255, verbose_name='栏目类型')),
                ('seo_path', models.CharField(blank=True, max_length=20, null=True, verbose_name='seo url')),
                ('seo_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='seo标题')),
                ('seo_keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name='seo关键字')),
                ('seo_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='seo描述')),
                ('sort', models.IntegerField(default=0, verbose_name='排序')),
                ('status', models.SmallIntegerField(choices=[[0, '正常'], [9, '禁用']], db_index=True, default=0, verbose_name='状态')),
                ('content', models.TextField(blank=True, null=True, verbose_name='详情')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='common.Category', verbose_name='父级')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('ckey', models.CharField(db_index=True, help_text='必须是英文', max_length=255, verbose_name='配置名称')),
                ('cvalue', models.CharField(max_length=255, verbose_name='配置值')),
            ],
            options={
                'db_table': 'config',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('source', models.CharField(blank=True, max_length=255, null=True, verbose_name='来源')),
                ('ip', models.CharField(blank=True, max_length=50, null=True, verbose_name='ip')),
                ('status', models.SmallIntegerField(choices=[[0, '正常'], [9, '禁用']], db_index=True, default=0, verbose_name='状态')),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('status', models.SmallIntegerField(choices=[[0, '正常'], [1, '推荐'], [2, '置顶'], [9, '禁用']], db_index=True, default=0, verbose_name='状态')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='价格')),
                ('seo_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='seo标题')),
                ('seo_keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name='seo关键字')),
                ('seo_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='seo描述')),
                ('click', models.IntegerField(default=0, verbose_name='点击量')),
                ('sort', models.IntegerField(default=0, verbose_name='排序')),
                ('content', models.TextField(blank=True, null=True, verbose_name='详情')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='common.Category', verbose_name='栏目')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='common.Attachment', verbose_name='图片')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='common.Product', verbose_name='产品')),
            ],
            options={
                'db_table': 'product_photo',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='photos',
            field=models.ManyToManyField(blank=True, related_name='photos', through='common.ProductPhoto', to='common.Attachment', verbose_name='画册'),
        ),
        migrations.CreateModel(
            name='FriendLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
                ('url', models.URLField(help_text='格式： https://www.example.com', max_length=255, verbose_name='Url')),
                ('sort', models.IntegerField(default=0, verbose_name='排序')),
                ('status', models.SmallIntegerField(choices=[[0, '正常'], [9, '禁用']], db_index=True, default=0, verbose_name='状态')),
                ('logo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='common.Attachment', verbose_name='Logo')),
            ],
            options={
                'db_table': 'friend_link',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('url', models.CharField(blank=True, max_length=255, null=True, verbose_name='外部连接')),
                ('status', models.SmallIntegerField(choices=[[0, '正常'], [1, '推荐'], [2, '置顶'], [9, '禁用']], db_index=True, default=0, verbose_name='状态')),
                ('seo_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='seo标题')),
                ('seo_keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name='seo关键字')),
                ('seo_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='seo描述')),
                ('click', models.IntegerField(default=0, verbose_name='点击量')),
                ('sort', models.IntegerField(default=0, verbose_name='排序')),
                ('content', models.TextField(blank=True, null=True, verbose_name='详情')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='common.Category', verbose_name='栏目')),
                ('image', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='common.Attachment', verbose_name='图片')),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Adv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=255, verbose_name='广告名称')),
                ('url', models.CharField(max_length=255, verbose_name='广告连接')),
                ('status', models.SmallIntegerField(choices=[[0, '正常'], [9, '禁用']], db_index=True, default=0, verbose_name='状态')),
                ('sort', models.IntegerField(default=0, verbose_name='排序')),
                ('describe', models.CharField(blank=True, max_length=255, null=True, verbose_name='广告描述')),
                ('adv_position', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='common.AdvPosition', verbose_name='广告位')),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='common.Attachment', verbose_name='图片')),
            ],
            options={
                'db_table': 'adv',
                'abstract': False,
            },
        ),
    ]
