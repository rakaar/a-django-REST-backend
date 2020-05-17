from djongo import models


class CollegeCourse(models.Model):
    name = models.CharField(max_length=200)


class Position(models.Model):
    year = models.CharField(max_length=10)
    description = models.CharField(max_length=200)


class School(models.Model):
    name = models.CharField(max_length=200)
    board = models.CharField(max_length=200)
    percentage = models.CharField(max_length=10)


class College(models.Model):
    name = models.CharField(max_length=200)
    cgpa_range = models.CharField(max_length=200)
    dept = models.CharField(max_length=200)
    core_courses = models.ArrayField(model_container=CollegeCourse)
    additional_courses = models.ArrayField(model_container=CollegeCourse)


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    # prof / FTP / BTP,MTP / self
    project_type = models.CharField(max_length=10)
    # prof_name / college_name / prof_name / null
    associated_info = models.CharField(max_length=20, blank=True)


class ResearchPaper(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    journal = models.CharField(max_length=200)
    num_of_people = models.IntegerField()
    is_main = models.BooleanField()
    name_of_main = models.CharField(max_length=200, blank=True)


class PrevIntern(models.Model):
    company = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    from_date = models.CharField(max_length=200)
    to_date = models.CharField(max_length=200)
    nature = models.CharField(max_length=10)  # remote / direct


class PoR(models.Model):
    place = models.CharField(max_length=200)  # name of soceity
    positions = models.ArrayField(model_container=Position)


class OnlineCourse(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True)
    partner_insti = models.CharField(max_length=200, blank=True)


class Certification(models.Model):
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


class Skill(models.Model):
    name = models.CharField(max_length=200)


class Patent(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    date = models.CharField(max_length=200)

class Competition(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    date = models.CharField(max_length=200)


class Profile(models.Model):
    location = models.CharField(max_length=200)
    school = models.EmbeddedField(model_container=School)
    college = models.EmbeddedField(model_container=College)
    projects = models.ArrayField(model_container=Project)
    research_papers = models.ArrayField(model_container=ResearchPaper)
    patents = models.ArrayField(model_container=Patent)
    prev_interns = models.ArrayField(model_container=PrevIntern)
    por = models.ArrayField(model_container=PoR)
    online_courses = models.ArrayField(model_container=OnlineCourse)
    competitions = models.ArrayField(model_container=Competition)
    certifications = models.ArrayField(model_container=Certification)
    skills = models.ArrayField(model_container=Skill)
