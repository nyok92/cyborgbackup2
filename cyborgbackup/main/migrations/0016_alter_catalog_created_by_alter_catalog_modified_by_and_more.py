# Generated by Django 4.1.7 on 2023-02-19 15:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0015_add_integrity_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='%s(class)s_created+',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='%s(class)s_modified+',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='client',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='%s(class)s_created+',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='client',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='%s(class)s_modified+',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='job',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='%s(class)s_created+',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='job',
            name='dependent_jobs',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='%(class)s_blocked_jobs+', to='main.job'),
        ),
        migrations.AlterField(
            model_name='job',
            name='master_job',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='%(class)s_master_job+', to='main.job'),
        ),
        migrations.AlterField(
            model_name='job',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='%s(class)s_modified+',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='policy',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='%s(class)s_created+',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='policy',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='%s(class)s_modified+',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='repository',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='%s(class)s_created+',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='repository',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='%s(class)s_modified+',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='%s(class)s_created+',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='%s(class)s_modified+',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='ActivityStream',
        ),
    ]
