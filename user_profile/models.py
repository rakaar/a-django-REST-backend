from djongo import models


class CollegeCourse(models.Model):
    name = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=1000, blank=True)


class Position(models.Model):
    position_held = models.CharField(max_length=200, blank=True)
    year_in_college = models.IntegerField(blank=True)
    duration = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=1000, blank=True)

class TwelthEdu(models.Model):
    course_name = models.CharField(max_length=200, blank=True)
    school = models.CharField(max_length=200, blank=True)
    board = models.CharField(max_length=200, blank=True)
    start_date = models.CharField(max_length=200, blank=True)
    end_date = models.CharField(max_length=200, blank=True)
    is_cgpa= models.BooleanField(blank=True)
    cg_or_percentage = models.CharField(max_length=200, blank=True)

class SchoolEdu(models.Model):
    course_name = models.CharField(max_length=200, blank=True)
    school = models.CharField(max_length=200, blank=True)
    board = models.CharField(max_length=200, blank=True)
    start_date = models.CharField(max_length=200, blank=True)
    end_date = models.CharField(max_length=200, blank=True)
    is_cgpa= models.BooleanField(blank=True)
    cg_or_percentage = models.CharField(max_length=200, blank=True)


class College(models.Model):
    course_name = models.CharField(max_length=200, blank=True)
    course_type = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200,blank=True)
    dept = models.CharField(max_length=200, blank=True)
    is_cgpa= models.BooleanField(blank=True)
    cg_or_percentage = models.CharField(max_length=200, blank=True)
    from_date = models.CharField(max_length=200, blank=True)
    to_date = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=1000, blank=True) 
    academic_courses = models.ArrayField(model_container=CollegeCourse, blank=True)
    
class SelfProject(models.Model):
    title = models.CharField(max_length=200, blank=True)
    from_date = models.CharField(max_length=200, blank=True)
    to_date = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=1000, blank=True)

class AcademicProject(models.Model):
    title = models.CharField(max_length=200, blank=True)
    institute = models.CharField(max_length=250, blank=True)
    prof = models.CharField(max_length=250, blank=True)
    prof_google_scholar_link = models.CharField(max_length=250, blank=True)
    from_date = models.CharField(max_length=200, blank=True)
    to_date = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=1000, blank=True)

class SelfResearchPaper(models.Model):
    title = models.CharField(max_length=200, blank=True)
    from_date = models.CharField(max_length=200, blank=True)
    to_date = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    is_main = models.BooleanField(blank=True)
    num_of_people = models.IntegerField(blank=True)
    publication_name = models.CharField(max_length=200, blank=True)
    publication_link = models.CharField(max_length=250, blank=True)

class AcademicResearchPaper(models.Model):
    title = models.CharField(max_length=200, blank=True)
    institute = models.CharField(max_length=250, blank=True)
    prof = models.CharField(max_length=250, blank=True)
    prof_google_scholar_link = models.CharField(max_length=250, blank=True)
    from_date = models.CharField(max_length=200, blank=True)
    to_date = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    is_main = models.BooleanField(blank=True)
    num_of_people = models.IntegerField(blank=True)
    publication_name = models.CharField(max_length=200, blank=True)
    publication_link = models.CharField(max_length=250, blank=True)

class PrevIntern(models.Model):
    company = models.CharField(max_length=200, blank=True)
    job_title = models.CharField(max_length=200, blank=True)
    from_date = models.CharField(max_length=200, blank=True)
    to_date = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True) 
    year_in_college = models.IntegerField(blank=True)
    description = models.CharField(max_length=1000, blank=True)

class WorkExperience(models.Model):
    company = models.CharField(max_length=200, blank=True)
    job_title = models.CharField(max_length=200, blank=True)
    from_date = models.CharField(max_length=200, blank=True)
    to_date = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=1000, blank=True)

class PoR(models.Model): 
    place = models.CharField(max_length=200, blank=True) 
    positions = models.ArrayField(model_container=Position, blank=True)

class OnlineCourse(models.Model):
    name = models.CharField(max_length=200, blank=True)
    company = models.CharField(max_length=200, blank=True)
    partner_insti = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=1000, blank=True)

class Certification(models.Model):
    name = models.CharField(max_length=200, blank=True) 
    issue_date = models.CharField(max_length=200, blank=True)
    valid_till = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    issuing_auth = models.CharField(max_length=200, blank=True)

class Skill(models.Model):
    name = models.CharField(max_length=200, blank=True)

class Patent(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    date = models.CharField(max_length=200, blank=True)
    link = models.CharField(max_length=300, blank=True)

class Competition(models.Model): 
    title = models.CharField(max_length=200, blank=True)
    level = models.CharField(max_length=200, blank=True)
    rank = models.CharField(max_length=200, blank=True)
    date = models.CharField(max_length=200, blank=True)
    issuing_auth = models.CharField(max_length=200, blank=True)

class Place(models.Model):
    name = models.CharField(max_length=200, blank=True)

class Preferences(models.Model): 
    prefered_sectors = models.ArrayField(model_container=Place, blank=True)
    prefered_interns = models.ArrayField(model_container=Place, blank=True)
    prefered_jobs = models.ArrayField(model_container=Place, blank=True)

def upload_path(instance, filename):
    return '/'.join(['pro_pic', filename])

class Profile(models.Model):
    location = models.CharField(max_length=200, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    about = models.CharField(max_length=500, blank=True)
    school = models.EmbeddedField(model_container=SchoolEdu, blank=True)
    twelth = models.EmbeddedField(model_container=TwelthEdu, blank=True)
    colleges = models.ArrayField(model_container=College, blank=True)
    self_projects = models.ArrayField(model_container=SelfProject, blank=True)
    academic_projects = models.ArrayField(model_container=AcademicProject, blank=True)
    self_research_papers = models.ArrayField(model_container=SelfResearchPaper, blank=True)
    academic_research_papers = models.ArrayField(model_container=AcademicResearchPaper, blank=True)
    patents = models.ArrayField(model_container=Patent, blank=True)
    prev_interns = models.ArrayField(model_container=PrevIntern, blank=True)
    work_experience = models.ArrayField(model_container=WorkExperience, blank=True)
    por = models.ArrayField(model_container=PoR, blank=True)
    online_courses = models.ArrayField(model_container=OnlineCourse, blank=True)
    competitions = models.ArrayField(model_container=Competition, blank=True)
    certifications = models.ArrayField(model_container=Certification, blank=True)
    skills = models.ArrayField(model_container=Skill, blank=True)
    preferences = models.ArrayField(model_container=Preferences, blank=True, default=None)
    pro_pic = models.ImageField(blank=True, null=True, upload_to=upload_path)