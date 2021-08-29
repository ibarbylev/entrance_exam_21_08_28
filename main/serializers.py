from rest_framework import serializers, mixins, generics

from rectools.models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    skills = serializers.StringRelatedField(many=True, read_only=False)  # make field many-to-many as list of items

    class Meta:
        model = Candidate
        fields = ['first_name', 'last_name', 'email', 'bio', 'skills']
        # exclude = ['id']

        # depth = 1
        # On the previous line, I make the many-to-many field a list of items, not a list of IDs
        # (but then I found the variant: <skills = serializers.StringRelatedField(many=True)>)
