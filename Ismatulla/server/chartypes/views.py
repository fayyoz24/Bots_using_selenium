# Create your views here.
from rest_framework.views import APIView
import json
from rest_framework.response import Response
from .serializers import CharacterSerializer, QuestionSerializer
from .disctypes import reversed_dict_most
from .utils import disc_map

from .dict_16_chars.analyst import analyst
from .dict_16_chars.Architect import Architect
from .dict_16_chars.captain import captain
from .dict_16_chars.counselor import counselor
from .dict_16_chars.Driver import driver
from .dict_16_chars.editor import editor
from .dict_16_chars.encourager import encourager
from .dict_16_chars.harmonizer import Harmoniser
from .dict_16_chars.influencer import influencer
from .dict_16_chars.initiator import initiator
from .dict_16_chars.motivator import motivator
from .dict_16_chars.planner import planner
from .dict_16_chars.questioner import questioner
from .dict_16_chars.sceptic import sceptic
from .dict_16_chars.stabilizer import stabilizer
from .dict_16_chars.supporter import supporter
# Create your views here.
dict_emotion={
'Driver (Di)':driver,
'Supporter (S)':supporter,
'Skeptic (Cd)': sceptic,
'Initiator (DI)':initiator,
'Captain (D)':captain,
'Influencer (Id)':influencer,
'Motivator (I)':motivator,
'Analyst (C)':analyst,
'Encourager (Is)':encourager,
'Questioner (CD)':questioner,
'Harmonizer (IS)' : Harmoniser,
'Planner (Sc)':planner,
'Editor (Cs)':editor,
'Architect (Dc)':Architect,
'Counselor (Si)':counselor,
'Stabilizer (SC)':stabilizer,
}

class QuestionTestView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            sum_chars = serializer.validated_data['sum_chars']
            res = int(sum_chars)  
            character = next((value for key, value in disc_map.items() if res in key), 'Counselor (Si)')
            data=dict_emotion[character]
            with open('./chartypes/data.json', 'r') as file:
                vacancies = json.load(file)
            response_data = {'result': character, "data":data, "vacancies":vacancies}
            return Response(response_data)
        return Response(serializer.errors, status=400)
    
class CharacterView(APIView):
    def post(self, request, *args, **kwargs):

        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            character = serializer.validated_data['character']
            data=dict_emotion[character]
            response_data = {'result': character, "data":data}
            return Response(response_data)
        return Response(serializer.errors, status=400)