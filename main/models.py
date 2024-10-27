from django.db import models
from django.core import serializers
# Teacher Model
class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    # detail=models.TextField(null=True)
    email= models.CharField(max_length=100)
    password=models.CharField(max_length=100, blank=True, null=True)
    qualification=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=20)
    profile_img = models.ImageField(upload_to="teacher_profile_imgs/", null=True)
    skills=models.TextField()
    
    class Meta:
       verbose_name_plural="1. Teachers"
       
    # Total Teacher Courses
    def total_teacher_courses(self):
        total_courses = Course.objects.filter(teacher=self).count()
        return total_courses

# Total Teacher Chapters
    def total_teacher_chapters(self):
        total_chapters = Chapter.objects.filter(course__teacher=self).count()
        return total_chapters

# Total Teacher Students
    def total_teacher_students(self):
        total_students = StudentCourseEnrollment.objects.filter(course__teacher=self).count()
        return total_students

# Course Category
class CourseCategory(models.Model):
    title = models.CharField(max_length=100)
    description= models.TextField()
    
    class Meta:
       verbose_name_plural="2. Course Categories"
    def __str__(self):
        return self.title
# Course Model
# Course Model
class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="teacher_courses")
    title = models.CharField(max_length=150)
    description = models.TextField()
    featured_img = models.ImageField(upload_to="course_imgs/", null=True)
    languages = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "3. Courses"

    def related_videos(self):
        if self.languages:
            related_videos = Course.objects.filter(languages__icontains=self.languages)
        else:
            related_videos = Course.objects.none()  # or handle the logic in another way

        return serializers.serialize('json', related_videos)
    def __str__(self):
         return self.title
     
    def total_enrolled_students(self):
        total_enrolled_students = StudentCourseEnrollment.objects.filter(course=self).count()
        return total_enrolled_students
     
    def course_rating(self):
        course_rating = CourseRating.objects.filter(course=self).aggregate(avg_rating=models.Avg("rating"))
        return course_rating["avg_rating"]

# Chapter Model
class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name = "course_chapters")
    title = models.CharField(max_length=150)
    description = models.TextField()
    video = models.FileField(upload_to='chapter_videos/', null=True)
    remarks = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "4. Chapters"

    
# Student Model
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    username=models.CharField(max_length=200)
    interested_categories=models.TextField()
    
    def __str__(self):
         return self.full_name
    class Meta:
       verbose_name_plural="5. Students"

# Student Course Enrollment
class StudentCourseEnrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrolled_courses')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrolled_student')
    enrolled_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "6. Enrolled Courses"
    def __str__(self):
         return f"{self.course}-{self.student}"

# Course Rating and Reviews
class CourseRating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rating = models.PositiveBigIntegerField(default=0)
    reviews = models.TextField(null=True)
    review_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course}-{self.student}-{self.rating}"

# Student Favorite Course
class StudentFavoriteCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "7. Student Favorite Courses"

    def __str__(self):
        return f"{self.course} - {self.student}"
# Student Assignment
# class StudentAssignment(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     detail = models.TextField(null=True)
#     add_time = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{title}"
    
#     class Meta:
#         verbose_name_plural = "9. Student Assignment"