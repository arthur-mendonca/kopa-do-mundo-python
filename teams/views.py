from rest_framework.views import APIView, status, Request
from rest_framework.response import Response
from django.forms.models import model_to_dict
from exceptions import *

from .models import Team
from utils import data_processing


class TeamView(APIView):
    def get(self, request):
        teams = Team.objects.all()

        return Response([model_to_dict(team) for team in teams], 200)

    def post(self, request):
        data = request.data
        try:
            data_processing(team_info=data)
            team = Team.objects.create(**data)
            team_dict = model_to_dict(team)
            return Response(team_dict, status=status.HTTP_201_CREATED)
        except (NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError) as err:
            return Response({"error": str(err)}, status=status.HTTP_400_BAD_REQUEST)


class TeamDetailView(APIView):
    def get(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
            team_dict = model_to_dict(team)
            return Response(team_dict, status=status.HTTP_200_OK)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def patch(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
            data = request.data
            data_processing(team_info=data)

            for key, value in data.items():
                setattr(team, key, value)
            team.save()

            team_dict = model_to_dict(team)
            return Response(team_dict, status=status.HTTP_200_OK)

        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
            team.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND
            )
