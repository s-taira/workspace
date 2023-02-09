
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from images.serializers import ImageSerializer
from .models import AiAnalysisLog
import json
import requests
from requests.exceptions import RequestException
import time


class ImageApi(ListCreateAPIView):
    queryset = AiAnalysisLog.objects.all()
    serializer_class = ImageSerializer

    def exam_post(self, image_path):
        '''
        example.comに画像分析リクエストを投げる

        パラメータ:image_path 分析対象のイメージパス
        戻り値：解析結果
        '''
        
        url = 'http://example.com'
        data = {
            'image_path': image_path
        }
        data_encode = json.dumps(data)

        response = requests.post(url, data=data_encode, timeout=1.5)
        response.raise_for_status()

        return json.loads(response.json)

    def post(self, request):
        '''
        画像分析を行い、結果をデータベースに保存する
        '''
        request_ts = int(time.time())

        # image_pathが指定されていない場合は400を返す
        r_body = request.data
        if 'image_path' not in r_body:
            return Response(
                '{"message":"not specified image_path param"}',
                status=status.HTTP_400_BAD_REQUEST)

        # 画像分析を実施
        try:
            json_dict = self.exam_post(r_body['image_path'])
        except RequestException:
            return Response('failed example.com POST request',
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        response_ts = int(time.time())

        serializer = ImageSerializer(
            data={
                "image_path": r_body['image_path'],
                "success": str(json_dict['success']).lower(),
                "message": json_dict['message'],
                "class_number": json_dict.get('estimated_data', {})
                                         .get('class'),
                "confidence": json_dict.get('estimated_data', {})
                                       .get('confidence'),
                'request_timestamp': request_ts,
                'response_timestamp': response_ts,
            })

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
