from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from django.conf import settings
import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import StudentCourseEnrollment
from rest_framework import status
from django.core.mail import send_mail
from django.shortcuts import redirect
from .serializers import (
    TeacherSerializer,
    CategorySerializer,
    CourseSerializer,
    ChapterSerializer,
    StudentSerializer,
    StudentCourseEnrollSerializer,
    CourseRatingSerializer,
    TeacherDashboardSerializer,
    # StudentFavoriteCourseSerializer,
    StudentAssignmentSerializer,
    StudentDashboardSerializer,
    TeacherStudentChatSerializer,
)
from . import models
import stripe

from random import randint

# Teacher-related views


# Teacher list and detail views
class TeacherList(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]


# Teacher course-related views
class TeacherCourseList(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        teacher_id = self.kwargs["teacher_id"]
        teacher = models.Teacher.objects.get(pk=teacher_id)
        return models.Course.objects.filter(teacher=teacher)


class TeacherCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAuthenticated]


# Teacher dashboard view
class TeacherDashboard(generics.RetrieveAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherDashboardSerializer


@csrf_exempt
def teacher_login(request):
    email = request.POST["email"]
    password = request.POST["password"]
    try:
        teacherData = models.Teacher.objects.get(email=email, password=password)
    except models.Teacher.DoesNotExist:
        teacherData = None
    if teacherData:
        if not teacherData.verify_status:
            return JsonResponse({"bool": False, "msg": "Account is not verified!!"})
        else:
            if teacherData.login_via_otp:
                # Send OTP Email
                otp_digit = randint(100000, 999999)
                send_mail(
                    "Verify Account",
                    "Please verify your account",
                    "codedynasty001@gmail.com",
                    [teacherData.email],
                    fail_silently=False,
                    html_message=f"<p>Your OTP is </p><p>{otp_digit}</p>",
                )
                teacherData.otp_digit = otp_digit
                teacherData.save()
                return JsonResponse(
                    {"bool": True, "teacher_id": teacherData.id, "login_via_otp": True}
                )
            else:
                return JsonResponse(
                    {"bool": True, "teacher_id": teacherData.id, "login_via_otp": False}
                )
    else:
        return JsonResponse({"bool": False, "msg": "Invalid Email Or Password!!!!"})


@csrf_exempt
def teacher_change_password(request, teacher_id):
    password = request.POST["password"]
    try:
        teacherData = models.Teacher.objects.get(id=teacher_id)
    except models.Teacher.DoesNotExist:
        teacherData = None
    if teacherData:
        models.Teacher.objects.filter(id=teacher_id).update(password=password)
        return JsonResponse({"bool": True})
    else:
        return JsonResponse({"bool": False})


@csrf_exempt
def verify_teacher_via_otp(request, teacher_id):
    otp_digit = request.POST.get("otp_digit")
    verify = models.Teacher.objects.filter(id=teacher_id, otp_digit=otp_digit).first()
    if verify:
        models.Teacher.objects.filter(id=teacher_id, otp_digit=otp_digit).update(
            verify_status=True
        )
        return JsonResponse({"bool": True, "teacher_id": verify.id})
    else:
        return JsonResponse({"bool": False, "msg": "Please enter valid 6 digit"})


@csrf_exempt
def teacher_forgot_password(request):
    email = request.POST.get("email")
    verify = models.Teacher.objects.filter(email=email).first()
    if verify:
        link = f"https://www.ambestenacademy.com/teacher-change-forgotten-password/{verify.id}/"
        send_mail(
            "Verify Account",
            "Please verify your account",
            "codedynasty001@gmail.com",
            [email],
            fail_silently=False,
            html_message=f"<p>Click this {link} to change your password</p>",
        )
        return JsonResponse({"bool": True, "msg": "Please check your email"})
    else:
        return JsonResponse({"bool": False, "msg": "Invalid Email!!"})


@csrf_exempt
def teacher_change_password(request, teacher_id):
    password = request.POST.get("password")
    verify = models.Teacher.objects.filter(id=teacher_id).first()
    if verify:
        models.Teacher.objects.filter(id=teacher_id).update(password=password)
        return JsonResponse({"bool": True, "msg": "Password has been changed"})
    else:
        return JsonResponse({"bool": False, "msg": "Oops... Some Error Occured!"})


# Student-related views


# Student list and login views
class StudentList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
def student_login(request):
    """Handle student login requests"""
    email = request.POST["email"]
    password = request.POST["password"]
    try:
        studentData = models.Student.objects.get(email=email, password=password)
    except models.Student.DoesNotExist:
        studentData = None
    if studentData:
        return JsonResponse({"bool": True, "student_id": studentData.id})
    else:
        return JsonResponse({"bool": False})


@csrf_exempt
def verify_student_via_otp(request, student_id):
    otp_digit = request.POST.get("otp_digit")
    verify = models.Student.objects.filter(id=student_id, otp_digit=otp_digit).first()
    if verify:
        models.Student.objects.filter(id=student_id, otp_digit=otp_digit).update(
            verify_status=True
        )
        return JsonResponse({"bool": True, "student_id": verify.id})
    else:
        return JsonResponse({"bool": False})
    
@csrf_exempt
def student_forgot_password(request):
    email = request.POST.get("email")
    verify = models.Student.objects.filter(email=email).first()
    if verify:
        link = f"https://www.ambestenacademy.com/student-change-forgotten-password/{verify.id}/"
        send_mail(
            "Change Password",
            "Please change your award",
            "codedynasty001@gmail.com",
            [email],
            fail_silently=False,
            html_message=f"<p>Click this {link} to change your password</p>",
        )
        return JsonResponse({"bool": True, "msg": "Please check your email"})
    else:
        return JsonResponse({"bool": False, "msg": "Invalid Email!!"})



@csrf_exempt
def student_change_forgotten_password(request, student_id):
    password = request.POST.get("password")
    verify = models.Student.objects.filter(id=student_id).first()
    if verify:
        models.Student.objects.filter(id=student_id).update(password=password)
        return JsonResponse({"bool": True, "msg": "Password has been changed"})
    else:
        return JsonResponse({"bool": False, "msg": "Oops... Some Error Occured!"})
    
    
stripe.api_key = settings.STRIPE_SECRET_KEY  # Set your secret key here


class CreatePaymentSession(APIView):
    def post(self, request, *args, **kwargs):
        # Retrieve course ID and student ID from the request
        course_id = request.data.get("course_id")
        student_id = request.data.get("student_id")

        # Fetch course data (you can modify this as per your model structure)
        course = models.Course.objects.get(id=course_id)
        price = (
            course.price
        )  # Make sure you're referencing the instance, not the class.

        # Create a Stripe session
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": course.title,
                            "description": course.description,
                        },
                        "unit_amount": int(course.price * 100),  # Convert to cents
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=f"{settings.SITE_URL}/success?session_id={{CHECKOUT_SESSION_ID}}",  # Redirect on success
            cancel_url=f"{settings.SITE_URL}/cancel",  # Redirect on cancel
        )

        return Response({"session_id": session.id}, status=status.HTTP_200_OK)


# Student course enrollment and status views
class StudentEnrolledCourseList(generics.ListCreateAPIView):
    queryset = models.StudentCourseEnrollment.objects.all()
    serializer_class = StudentCourseEnrollSerializer
    # permission_classes = [permissions.IsAuthenticated]


def fetch_enroll_status(request, student_id, course_id):
    """Check enrollment status for a student in a course"""
    student = models.Student.objects.filter(id=student_id).first()
    course = models.Course.objects.filter(id=course_id).first()
    enrollStatus = models.StudentCourseEnrollment.objects.filter(
        course=course, student=student
    ).count()

    if enrollStatus:
        return JsonResponse({"bool": True})
    else:
        return JsonResponse({"bool": False})


class EnrollStudentList(generics.ListAPIView):
    queryset = models.StudentCourseEnrollment.objects.all()
    serializer_class = StudentCourseEnrollSerializer

    def get_queryset(self):
        """Filter enrolled students by course, teacher, or student"""
        if "course_id" in self.kwargs:
            course_id = self.kwargs["course_id"]
            course = models.Course.objects.get(pk=course_id)
            return models.StudentCourseEnrollment.objects.filter(course=course)
        elif "teacher_id" in self.kwargs:
            teacher_id = self.kwargs["teacher_id"]
            teacher = models.Teacher.objects.get(pk=teacher_id)
            return models.StudentCourseEnrollment.objects.filter(
                course__teacher=teacher
            ).distinct()
        elif "student_id" in self.kwargs:
            student_id = self.kwargs["student_id"]
            student = models.Student.objects.get(pk=student_id)
            return models.StudentCourseEnrollment.objects.filter(
                student=student
            ).distinct()


# Student course rating and favorite views
class CourseRatingList(generics.ListCreateAPIView):
    serializer_class = CourseRatingSerializer

    def get_queryset(self):
        """Get ratings for a specific course"""
        course_id = self.kwargs["course_id"]
        course = models.Course.objects.get(pk=course_id)
        return models.CourseRating.objects.filter(course=course)


def fetch_rating_status(request, student_id, course_id):
    """Check if a student has rated a course"""
    student = models.Student.objects.filter(id=student_id).first()
    course = models.Course.objects.filter(id=course_id).first()
    ratingStatus = models.CourseRating.objects.filter(
        course=course, student=student
    ).count()

    if ratingStatus:
        return JsonResponse({"bool": True})
    else:
        return JsonResponse({"bool": False})


# class StudentFavoriteCourseList(generics.ListCreateAPIView):
#     queryset = models.StudentFavoriteCourse.objects.all()
#     serializer_class = StudentFavoriteCourseSerializer

# def fetch_favorite_status(request, student_id, course_id):
#     """Check if a course is in a student's favorites"""
#     student = models.Student.objects.filter(id=student_id).first()
#     course = models.Course.objects.filter(id=course_id).first()

#     if not student or not course:
#         return JsonResponse({"bool": False})

#     favorite_status = models.StudentFavoriteCourse.objects.filter(course=course, student=student).first()

#     if favorite_status and favorite_status.status:
#         return JsonResponse({"bool": True})
#     else:
#         return JsonResponse({"bool": False})

# def remove_favorite_course(request, course_id, student_id):
#     """Remove a course from student's favorites"""
#     student = models.Student.objects.filter(id=student_id).first()
#     course = models.Course.objects.filter(id=course_id).first()
#     favoriteStatus = models.StudentFavoriteCourse.objects.filter(course=course, student=student).delete()
#     if favoriteStatus:
#         return JsonResponse({"bool": True})
#     else:
#         return JsonResponse({"bool": False})


# Student dashboard view
class StudentDashboard(generics.RetrieveAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentDashboardSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [permissions.IsAuthenticated]


# Assignment views (student and teacher specific)
class AssignmentList(generics.ListCreateAPIView):
    queryset = models.StudentAssignment.objects.all()
    serializer_class = StudentAssignmentSerializer

    def get_queryset(self):
        """Filter assignments by student and teacher"""
        student_id = self.kwargs["student_id"]
        teacher_id = self.kwargs["teacher_id"]
        student = models.Student.objects.get(pk=student_id)
        teacher = models.Teacher.objects.get(pk=teacher_id)
        return models.StudentAssignment.objects.filter(student=student, teacher=teacher)


class MyAssignmentList(generics.ListCreateAPIView):
    queryset = models.StudentAssignment.objects.all()
    serializer_class = StudentAssignmentSerializer

    def get_queryset(self):
        student_id = self.kwargs["student_id"]
        student = models.Student.objects.get(pk=student_id)
        return models.StudentAssignment.objects.filter(student=student)


class UpdateAssignment(generics.RetrieveUpdateAPIView):
    queryset = models.StudentAssignment.objects.all()
    serializer_class = StudentAssignmentSerializer


@csrf_exempt
def student_change_password(request, student_id):
    password = request.POST["password"]
    try:
        studentData = models.Student.objects.get(id=student_id)
    except models.Student.DoesNotExist:
        studentData = None
    if studentData:
        models.Student.objects.filter(id=student_id).update(password=password)
        return JsonResponse({"bool": True})
    else:
        return JsonResponse({"bool": False})


# Course-related views


class CategoryList(generics.ListCreateAPIView):
    queryset = models.CourseCategory.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]


class CourseList(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        """Return a limited number of courses if 'result' is specified in the GET parameters"""
        qs = super().get_queryset()  # Get the default queryset
        if "result" in self.request.GET:
            limit = int(self.request.GET["result"])
            qs = models.Course.objects.all().order_by("-id")[:limit]
        return qs


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()  # Assuming you have a Course model
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAuthenticated]  # Uncomment to enforce authentication


# Chapter views


class ChapterList(generics.ListCreateAPIView):
    queryset = models.Chapter.objects.all()
    serializer_class = ChapterSerializer


class CourseChapterList(generics.ListAPIView):
    serializer_class = ChapterSerializer

    def get_queryset(self):
        """Get all chapters for a specific course"""
        course_id = self.kwargs["course_id"]
        course = models.Course.objects.get(pk=course_id)
        return models.Chapter.objects.filter(course=course)


class ChapterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Chapter.objects.all()
    serializer_class = ChapterSerializer
    # permission_classes = [permissions.IsAuthenticated]  # Uncomment to enforce authentication


@csrf_exempt
def save_teacher_student_msg(request, teacher_id, student_id):
    teacher = models.Teacher.objects.get(id=teacher_id)
    student = models.Student.objects.get(id=student_id)
    msg_text = request.POST.get("msg_text")
    msg_from = request.POST.get("msg_from")

    msgRes = models.TeacherStudentChat.objects.create(
        teacher=teacher,
        student=student,
        msg_text=msg_text,
        msg_from=msg_from,
    )

    if msgRes:
        return JsonResponse({"bool": True, "msg": "Message has been sent"})
    else:
        return JsonResponse({"bool": False, "msg": "Oops... Some Error Occurred!!"})


class MessageList(generics.ListAPIView):
    queryset = models.TeacherStudentChat.objects.all()
    serializer_class = TeacherStudentChatSerializer

    def get_queryset(self):
        teacher_id = self.kwargs["teacher_id"]
        student_id = self.kwargs["student_id"]
        teacher = models.Teacher.objects.get(pk=teacher_id)
        student = models.Student.objects.get(pk=student_id)
        return models.TeacherStudentChat.objects.filter(
            teacher=teacher, student=student
        ).exclude(msg_text="")


@csrf_exempt
def save_teacher_student_group_msg(request, teacher_id):
    teacher = models.Teacher.objects.get(id=teacher_id)
    msg_text = request.POST.get("msg_text")
    msg_from = request.POST.get("msg_from")

    enrolledList = models.StudentCourseEnrollment.objects.filter(
        course__teacher=teacher
    ).distinct()
    for enrolled in enrolledList:
        msgRes = models.TeacherStudentChat.objects.create(
            teacher=teacher,
            student=enrolled.student,
            msg_text=msg_text,
            msg_from=msg_from,
        )

    if msgRes:
        return JsonResponse({"bool": "True", "msg": "Message has been sent"})
    else:
        return JsonResponse({"bool": "False", "msg": "Oops... Some Error Occured!!"})


class MyTeacherList(generics.ListAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        if "student_id" in self.kwargs:
            student_id = self.kwargs["student_id"]
            sql = "SELECT * FROM main_course as c, main_studentcourseenrollment as e, main_teacher as t WHERE c.teacher_id=t.id AND e.course_id=c.id AND e.student_id=%s GROUP BY c.teacher_id"
            qs = models.Course.objects.raw(sql, [student_id])
            print(qs)
            return qs


@csrf_exempt
def save_teacher_student_group_msg_from_student(request, student_id):
    student = models.Student.objects.get(id=student_id)
    msg_text = request.POST.get("msg_text")
    msg_from = request.POST.get("msg_from")

    sql = """SELECT * FROM main_course as c, main_studentcoursenrollment as e, main_teacher as t WHERE c.teacher_id=t.id 
    AND e.student_id={student_id} GROUP BY c.teacher_id""".format(
        student_id=student.id
    )
    qs = models.Course.objects.raw(sql)

    myCourses = qs
    for course in myCourses:
        msgRes = models.TeacherStudentChat.objects.create(
            teacher=course.teacher,
            student=student,
            msg_text=msg_text,
            msg_from=msg_from,
        )

    if msgRes:
        return JsonResponse({"bool": "True", "msg": "Message has been send"})
    else:
        return JsonResponse({"bool": "False", "msg": "Oops... Some Error Occured!!"})


# stripe.api_key = settings.STRIPE_SECRET_KEY

# @csrf_exempt
# def create_checkout_session(request, course_id):
#     stripe.api_key = settings.STRIPE_SECRET_KEY

#     # Fetch course details from your database
#     course = models.Course.objects.get(id=course_id)  # Replace with your model logic
#     course_price = int(course.price * 100)  # Convert price to cents

#     session = stripe.checkout.Session.create(
#         payment_method_types=["card"],
#         line_items=[
#             {
#                 "price_data": {
#                     "currency": "usd",
#                     "product_data": {"name": course.title},
#                     "unit_amount": course_price,
#                 },
#                 "quantity": 1,
#             },
#         ],
#         mode="payment",
#         success_url="http://127.0.0.1:3000/payment-success?session_id={CHECKOUT_SESSION_ID}",
#         cancel_url="http://127.0.0.1:3000/payment-cancel",
#     )
#     return JsonResponse({"id": session.id})
