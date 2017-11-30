from rest_framework import generics
from django.db.models import Q
from pivot_v2.models import Major, GPA, Course
from pivot_v2.serializers import MajorInfoSerializer, MajorSerializer,\
                                 MajorCourseSerializer, MajorGPASerializer


# DATA INCLINED VIEW
class MajorView(generics.ListAPIView):
    """
    A class based view for fetching complete Major information with
    Course and GPA as part of the response
    """
    serializer_class = MajorSerializer

    def get_queryset(self):
        year = get_requested_year(self.request.query_params)
        queryset = Major.objects.filter(
            Q(major_gpas__year=year) |
            Q(major_courses__year=year)
        )
        queryset = self.serializer_class().setup_eager_loading(queryset, year)
        return queryset


# PERFORMANCE INCLINED VIEWS
class MajorInfoView(generics.ListAPIView):
    """
    A class based view for fetching basic Major information
    """
    serializer_class = MajorInfoSerializer

    def get_queryset(self):
        year = get_requested_year(self.request.query_params)
        queryset = Major.objects.filter(
            Q(major_gpas__year=year) |
            Q(major_courses__year=year)
        )
        return queryset


class MajorGPAView(generics.ListAPIView):
    """
    A class based view for fetching complete Major information with
    GPA as part of the response
    """
    serializer_class = MajorGPASerializer

    def get_queryset(self):
        year = get_requested_year(self.request.query_params)
        queryset = Major.objects.filter(
            Q(major_gpas__year=year)
        )
        queryset = self.serializer_class().setup_eager_loading(queryset, year)
        return queryset


class MajorCourseView(generics.ListAPIView):
    """
    A class based view for fetching complete Major information with
    Course as part of the response
    """
    serializer_class = MajorCourseSerializer

    def get_queryset(self):
        year = get_requested_year(self.request.query_params)
        queryset = Major.objects.filter(
            Q(major_courses__year=year)
        )
        queryset = self.serializer_class().setup_eager_loading(queryset, year)
        return queryset


# UTILITY METHODS
def get_requested_year(params):
    if "year" not in params:
        raise Exception("No year in query_params")

    return params.get("year")
