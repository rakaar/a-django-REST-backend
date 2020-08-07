# Generated by Django 2.2.12 on 2020-08-07 15:14

from django.db import migrations, models
import djongo.models.fields
import user_profile.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('institute', models.CharField(blank=True, max_length=250)),
                ('prof', models.CharField(blank=True, max_length=250)),
                ('prof_google_scholar_link', models.CharField(blank=True, max_length=250)),
                ('from_date', models.CharField(blank=True, max_length=200)),
                ('to_date', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='AcademicResearchPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('institute', models.CharField(blank=True, max_length=250)),
                ('prof', models.CharField(blank=True, max_length=250)),
                ('prof_google_scholar_link', models.CharField(blank=True, max_length=250)),
                ('from_date', models.CharField(blank=True, max_length=200)),
                ('to_date', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('is_main', models.BooleanField(blank=True)),
                ('num_of_people', models.IntegerField(blank=True)),
                ('publication_name', models.CharField(blank=True, max_length=200)),
                ('publication_link', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('issue_date', models.CharField(blank=True, max_length=200)),
                ('valid_till', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('issuing_auth', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank=True, max_length=200)),
                ('course_type', models.CharField(blank=True, max_length=200)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('dept', models.CharField(blank=True, max_length=200)),
                ('is_cgpa', models.BooleanField(blank=True)),
                ('cg_or_percentage', models.CharField(blank=True, max_length=200)),
                ('from_date', models.CharField(blank=True, max_length=200)),
                ('to_date', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('academic_courses', djongo.models.fields.ArrayField(blank=True, model_container=user_profile.models.CollegeCourse)),
            ],
        ),
        migrations.CreateModel(
            name='CollegeCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('level', models.CharField(blank=True, max_length=200)),
                ('rank', models.CharField(blank=True, max_length=200)),
                ('date', models.CharField(blank=True, max_length=200)),
                ('issuing_auth', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OnlineCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('company', models.CharField(blank=True, max_length=200)),
                ('partner_insti', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('date', models.CharField(blank=True, max_length=200)),
                ('link', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PoR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=200)),
                ('positions', djongo.models.fields.ArrayField(blank=True, model_container=user_profile.models.Position)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_held', models.CharField(blank=True, max_length=200)),
                ('year_in_college', models.IntegerField(blank=True)),
                ('duration', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefered_sectors', djongo.models.fields.ArrayField(blank=True, model_container=user_profile.models.Place)),
                ('prefered_interns', djongo.models.fields.ArrayField(blank=True, model_container=user_profile.models.Place)),
                ('prefered_jobs', djongo.models.fields.ArrayField(blank=True, model_container=user_profile.models.Place)),
            ],
        ),
        migrations.CreateModel(
            name='PrevIntern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=200)),
                ('job_title', models.CharField(blank=True, max_length=200)),
                ('from_date', models.CharField(blank=True, max_length=200)),
                ('to_date', models.CharField(blank=True, max_length=200)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('year_in_college', models.IntegerField(blank=True)),
                ('description', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=200)),
                ('bio', models.CharField(blank=True, max_length=500)),
                ('about', models.CharField(blank=True, max_length=500)),
                ('school', djongo.models.fields.EmbeddedField(blank=True, model_container=user_profile.models.SchoolEdu, null=True)),
                ('twelth', djongo.models.fields.EmbeddedField(blank=True, model_container=user_profile.models.TwelthEdu, null=True)),
                ('colleges', djongo.models.fields.ArrayField(blank=True, model_container=user_profile.models.College)),
                ('self_projects', djongo.models.fields.ArrayField(blank=True, model_container=user_profile.models.SelfProject)),
                ('academic_projects', djongo.models.fields.ArrayField(blank=True, model_container=user_profile.models.AcademicProject)),
                ('self_research_papers', djongo.models.fields.ArrayField(blank=True, model_container=user_profile.models.SelfResearchPaper)),
                ('academic_research_papers', djongo.models.fields.ArrayField(blank=True, model_container=user_profile.models.AcademicResearchPaper)),
                ('patents', djongo.models.fields.ArrayField(blank=True, model_container=user_profile.models.Patent)),
                ('prev_interns', djongo.models.fields.ArrayField(blank=True, model_container=user_profile.models.PrevIntern)),
                ('work_experience', djongo.models.fields.ArrayField(blank=True, model_container=user_profile.models.WorkExperience)),
                ('por', djongo.models.fields.ArrayField(blank=True, model_container=user_profile.models.PoR)),
                ('online_courses', djongo.models.fields.ArrayField(blank=True, model_container=user_profile.models.OnlineCourse)),
                ('competitions', djongo.models.fields.ArrayField(blank=True, model_container=user_profile.models.Competition)),
                ('certifications', djongo.models.fields.ArrayField(blank=True, model_container=user_profile.models.Certification)),
                ('skills', djongo.models.fields.ArrayField(blank=True, model_container=user_profile.models.Skill)),
                ('preferences', djongo.models.fields.ArrayField(blank=True, default=None, model_container=user_profile.models.Preferences)),
                ('pro_pic', models.ImageField(blank=True, null=True, upload_to=user_profile.models.upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolEdu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank=True, max_length=200)),
                ('school', models.CharField(blank=True, max_length=200)),
                ('board', models.CharField(blank=True, max_length=200)),
                ('start_date', models.CharField(blank=True, max_length=200)),
                ('end_date', models.CharField(blank=True, max_length=200)),
                ('is_cgpa', models.BooleanField(blank=True)),
                ('cg_or_percentage', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SelfProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('from_date', models.CharField(blank=True, max_length=200)),
                ('to_date', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='SelfResearchPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('from_date', models.CharField(blank=True, max_length=200)),
                ('to_date', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('is_main', models.BooleanField(blank=True)),
                ('num_of_people', models.IntegerField(blank=True)),
                ('publication_name', models.CharField(blank=True, max_length=200)),
                ('publication_link', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TwelthEdu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank=True, max_length=200)),
                ('school', models.CharField(blank=True, max_length=200)),
                ('board', models.CharField(blank=True, max_length=200)),
                ('start_date', models.CharField(blank=True, max_length=200)),
                ('end_date', models.CharField(blank=True, max_length=200)),
                ('is_cgpa', models.BooleanField(blank=True)),
                ('cg_or_percentage', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=200)),
                ('job_title', models.CharField(blank=True, max_length=200)),
                ('from_date', models.CharField(blank=True, max_length=200)),
                ('to_date', models.CharField(blank=True, max_length=200)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=1000)),
            ],
        ),
    ]
