from django.db.models import Prefetch
from rest_framework import serializers
from pivot_v2.models import Major, GPA, Course


# UTILITY SERIALIZERS
class GPASerializer(serializers.ModelSerializer):
    class Meta:
        model = GPA
        fields = ('iqr_min', 'q1', 'median', 'q3', 'iqr_max', 'year')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('dept_abbr', 'course_number', 'student_count',
                  'students_in_major', 'popularity_rank', 'course_full_name',
                  'percentiles', 'year')


# DATA INCLINED SERIALIZER
class MajorSerializer(serializers.ModelSerializer):
    major_gpas = GPASerializer(many=True, read_only=True)
    major_courses = CourseSerializer(many=True, read_only=True)

    def setup_eager_loading(self, queryset, year):
        gpa_subset = GPA.objects.filter(year=year)
        course_subset = Course.objects.filter(year=year)
        queryset = queryset.prefetch_related(
            Prefetch('major_gpas', queryset=gpa_subset),
            Prefetch('major_courses', queryset=course_subset)
        )
        return queryset

    class Meta:
        model = Major
        fields = ('id', 'major_abbr', 'pathway', 'campus',
                  'college', 'major_full_name', 'url', 'status',
                  'major_gpas', 'major_courses')


# PERFORMANCE INCLINED SERIALIZERS
class MajorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ('id', 'major_abbr', 'pathway', 'campus',
                  'college', 'major_full_name', 'url', 'status')


class MajorGPASerializer(serializers.ModelSerializer):
    major_gpas = GPASerializer(many=True, read_only=True)

    def setup_eager_loading(self, queryset, year):
        gpa_subset = GPA.objects.filter(year=year)
        queryset = queryset.prefetch_related(
            Prefetch('major_gpas', queryset=gpa_subset)
        )
        return queryset

    class Meta:
        model = Major
        fields = ('id', 'major_abbr', 'pathway', 'campus',
                  'college', 'major_full_name', 'url', 'status',
                  'major_gpas')


class MajorCourseSerializer(serializers.ModelSerializer):
    major_courses = CourseSerializer(many=True, read_only=True)

    def setup_eager_loading(self, queryset, year):
        course_subset = Course.objects.filter(year=year)
        queryset = queryset.prefetch_related(
            Prefetch('major_courses', queryset=course_subset)
        )
        return queryset

    class Meta:
        model = Major
        fields = ('id', 'major_abbr', 'pathway', 'campus',
                  'college', 'major_full_name', 'url', 'status',
                  'major_courses')
