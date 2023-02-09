import requests
from django.test import TestCase, Client
from unittest import mock


# Create your tests here.
class SuccessPostTest(TestCase):

    def test_post_not_specified_image_path(self):
        """
        image_pathを指定せずにAPIをcall
        """
        response = Client().post('/api/images')
        self.assertEqual(response.status_code, 400)
        print(response.json())

    @mock.patch('images.apis.requests.post')
    def test_post_successed_analyze_image_(self, exam_patch):
        """
        example.comからsuccess:trueのレスポンスを取得した場合のテスト
        """
        # モックでの返却データ
        mock_res = requests.Response()
        mock_res.status_code = 200
        mock_res.json = '''
        {
           "success": true,
           "message": "success",
           "estimated_data": {
            "class": 3,
            "confidence": 0.8683
            }
        }
        '''
        exam_patch.return_value = mock_res

        image_path = 'a/b/c/d/e.png'
        data = {
            'image_path': image_path
        }

        response = Client().post('/api/images', data)
        print(response.json())
        self.assertEqual(response.status_code, 200)
        res_dict = response.json()
        self.assertIsInstance(res_dict['id'], int)
        self.assertEqual(res_dict['image_path'], image_path)
        self.assertEqual(res_dict['success'], 'true')
        self.assertEqual(res_dict['message'], 'success')
        self.assertEqual(res_dict['class_number'], 3)
        self.assertEqual(res_dict['confidence'], '0.8683')
        self.assertIsInstance(res_dict['request_timestamp'], int)
        self.assertIsInstance(res_dict['response_timestamp'], int)

    @mock.patch('images.apis.requests.post')
    def test_post_failed_analyze_image_(self, exam_patch):
        """
        example.comからsuccess:falseのレスポンスを取得した場合のテスト
        """
        mock_res = requests.Response()
        mock_res.status_code = 200
        mock_res.json = '''
        {
           "success": false,
           "message": "Error:E50012",
           "estimated_data": {}
        }
        '''
        exam_patch.return_value = mock_res

        image_path = 'a/b/c/d/e.png'
        data = {
            'image_path': image_path
        }

        response = Client().post('/api/images', data)
        print(response.json())
        self.assertEqual(response.status_code, 200)
        res_dict = response.json()
        self.assertIsInstance(res_dict['id'], int)
        self.assertEqual(res_dict['image_path'], image_path)
        self.assertEqual(res_dict['success'], 'false')
        self.assertEqual(res_dict['message'], 'Error:E50012')
        self.assertEqual(res_dict['class_number'], None)
        self.assertEqual(res_dict['confidence'], None)
        self.assertIsInstance(res_dict['request_timestamp'], int)
        self.assertEqual(len(str(res_dict['request_timestamp'])), 10)
        self.assertIsInstance(res_dict['response_timestamp'], int)
        self.assertEqual(len(str(res_dict['response_timestamp'])), 10)
