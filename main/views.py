from django.shortcuts import render

from rest_framework import views as rest_views, status
from rest_framework.response import Response

from main.serializers import CandidateSerializer
from rectools.models import Candidate


class CandidateListAPIView(rest_views.APIView):
    def get(self, request):
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CandidateSerializer(data=request.data)

        if serializer.is_valid():
            # TODO look for a free recruiter and (may be) to create a new recruiter
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CandidateDetailsAPIView(rest_views.APIView):
    def get(self, request, pk):
        candidate = Candidate.objects.get(pk=pk)
        serializer = CandidateSerializer(candidate, many=False)
        return Response(serializer.data)


