from rest_framework import mixins, status
from rest_framework import generics
from rest_framework.response import Response

from main.serializers import CandidateSerializer
from rectools.models import Candidate


class CandidateList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CandidateDetail(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, pk, *args, **kwargs):
        candidate = Candidate.objects.get(pk=pk)
        serializer = CandidateSerializer(candidate, data=request.data)

        if serializer.is_valid():
            # TODO check Skills (and to add a new one if necessary)
            print([skill.skill_name for skill in candidate.skills.all()])

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
