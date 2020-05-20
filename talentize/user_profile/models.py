from djongo import models


class CollegeCourse(models.Model):
    name = models.CharField(max_length=200, blank=True)


class Position(models.Model):
    year = models.CharField(max_length=10, blank=True)
    description = models.CharField(max_length=200, blank=True)


class School(models.Model):
    name = models.CharField(max_length=200, blank=True)
    board = models.CharField(max_length=200, blank=True)
    percentage = models.CharField(max_length=10, blank=True)


class College(models.Model):
    name = models.CharField(max_length=200,blank=True)
    cgpa_range = models.CharField(max_length=200, blank=True)
    dept = models.CharField(max_length=200, blank=True)
    core_courses = models.ArrayField(model_container=CollegeCourse, blank=True)
    additional_courses = models.ArrayField(model_container=CollegeCourse, blank=True)


class Project(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=400, blank=True)
    # prof / FTP / BTP,MTP / self
    project_type = models.CharField(max_length=10, blank=True)
    # prof_name / college_name / prof_name / null
    associated_info = models.CharField(max_length=20, blank=True)


class ResearchPaper(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=400, blank=True)
    journal = models.CharField(max_length=200, blank=True)
    num_of_people = models.IntegerField(blank=True)
    is_main = models.BooleanField(blank=True)
    name_of_main = models.CharField(max_length=200, blank=True)


class PrevIntern(models.Model):
    company = models.CharField(max_length=200, blank=True)
    job_title = models.CharField(max_length=200, blank=True)
    from_date = models.CharField(max_length=200, blank=True)
    to_date = models.CharField(max_length=200, blank=True)
    nature = models.CharField(max_length=10, blank=True)  # remote / direct


class PoR(models.Model):
    place = models.CharField(max_length=200, blank=True)  # name of soceity
    positions = models.ArrayField(model_container=Position, blank=True)


class OnlineCourse(models.Model):
    name = models.CharField(max_length=200, blank=True)
    company = models.CharField(max_length=200, blank=True)
    partner_insti = models.CharField(max_length=200, blank=True)


class Certification(models.Model):
    name = models.CharField(max_length=200, blank=True)
    year = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    issuing_auth =models.CharField(max_length=200, blank=True)

class Skill(models.Model):
    name = models.CharField(max_length=200, blank=True)


class Patent(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=600, blank=True)
    date = models.CharField(max_length=200, blank=True)

class Competition(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=600, blank=True)
    date = models.CharField(max_length=200, blank=True)
    issuing_auth = models.CharField(max_length=200, blank=True)

class Place(models.Model):
    name = models.CharField(max_length=200, blank=True)

class Preferences(models.Model):
    prefered_sectors = models.ArrayField(model_container=Place, blank=True)
    prefered_interns = models.ArrayField(model_container=Place, blank=True)
    prefered_jobs = models.ArrayField(model_container=Place, blank=True)

class Profile(models.Model):
    location = models.CharField(max_length=200, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    school = models.EmbeddedField(model_container=School, blank=True)
    college = models.EmbeddedField(model_container=College, blank=True)
    projects = models.ArrayField(model_container=Project, blank=True)
    research_papers = models.ArrayField(model_container=ResearchPaper, blank=True)
    patents = models.ArrayField(model_container=Patent, blank=True)
    prev_interns = models.ArrayField(model_container=PrevIntern, blank=True)
    por = models.ArrayField(model_container=PoR, blank=True)
    online_courses = models.ArrayField(model_container=OnlineCourse, blank=True)
    competitions = models.ArrayField(model_container=Competition, blank=True)
    certifications = models.ArrayField(model_container=Certification, blank=True)
    skills = models.ArrayField(model_container=Skill, blank=True)
