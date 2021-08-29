from django.shortcuts import render

from rest_framework import views as rest_views, status
from rest_framework.response import Response

from main.serializers import CandidateSerializer
from rectools.models import Candidate, Skills


class CandidateListAPIView(rest_views.APIView):
    def get(self, request):
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CandidateSerializer(data=request.data)

        if serializer.is_valid():
            # TODO look for a free recruiter and (may be) to create a new recruiter
            # TODO check Skills (and to add a new one if necessary)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CandidateDetailsAPIView(rest_views.APIView):
    def get(self, request, pk):
        candidate = Candidate.objects.get(pk=pk)
        serializer = CandidateSerializer(candidate, many=False)
        return Response(serializer.data)

    def delete(self, request, pk):
        candidate = Candidate.objects.get(pk=pk)
        candidate.delete()
        return Response(status=status.HTTP_200_OK)

    def put(self, request, pk):
        candidate = Candidate.objects.get(pk=pk)
        serializer = CandidateSerializer(candidate, data=request.data)

        if serializer.is_valid():
            # TODO check Skills (and to add a new one if necessary)
            print([skill.skill_name for skill in candidate.skills.all()])

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
