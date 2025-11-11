"""
Unit Tests for API Gateway
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from api.api_gateway import APIRequest, APIResponse, APIEndpoint, APIGateway


class TestAPIRequest(unittest.TestCase):
    """Test cases for APIRequest"""
    
    def test_request_creation(self):
        """Test API request creation"""
        request = APIRequest("GET", "/test", {"param": "value"})
        
        self.assertEqual(request.method, "GET")
        self.assertEqual(request.endpoint, "/test")
        self.assertIsNotNone(request.request_id)
    
    def test_request_to_dict(self):
        """Test request to dictionary conversion"""
        request = APIRequest("POST", "/api/test", {"data": "value"})
        request_dict = request.to_dict()
        
        self.assertIn("request_id", request_dict)
        self.assertIn("method", request_dict)
        self.assertIn("endpoint", request_dict)


class TestAPIResponse(unittest.TestCase):
    """Test cases for APIResponse"""
    
    def test_response_creation(self):
        """Test API response creation"""
        response = APIResponse(200, {"result": "success"})
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["result"], "success")
    
    def test_response_to_dict(self):
        """Test response to dictionary conversion"""
        response = APIResponse(200, {"result": "success"}, message="OK")
        response_dict = response.to_dict()
        
        self.assertIn("status_code", response_dict)
        self.assertIn("data", response_dict)
        self.assertIn("message", response_dict)
    
    def test_response_to_json(self):
        """Test response to JSON conversion"""
        response = APIResponse(200, {"result": "success"})
        json_str = response.to_json()
        
        self.assertIsInstance(json_str, str)
        self.assertIn("status_code", json_str)


class TestAPIGateway(unittest.TestCase):
    """Test cases for APIGateway"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.gateway = APIGateway()
        self.gateway.initialize()
    
    def test_initialization(self):
        """Test gateway initialization"""
        # Should have core endpoints registered
        endpoints = self.gateway.get_endpoints()
        self.assertGreater(len(endpoints), 0)
    
    def test_register_endpoint(self):
        """Test registering endpoint"""
        def test_handler(request):
            return APIResponse(200, {"test": "data"})
        
        self.gateway.register_endpoint("/test", "GET", test_handler)
        
        self.assertIn("/test", self.gateway.endpoints)
        self.assertIn("GET", self.gateway.endpoints["/test"])
    
    def test_handle_request_success(self):
        """Test handling successful request"""
        request = APIRequest("GET", "/system/status")
        response = self.gateway.handle_request(request)
        
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data)
    
    def test_handle_request_not_found(self):
        """Test handling request to non-existent endpoint"""
        request = APIRequest("GET", "/nonexistent")
        response = self.gateway.handle_request(request)
        
        self.assertEqual(response.status_code, 404)
        self.assertIsNotNone(response.error)
    
    def test_handle_request_method_not_allowed(self):
        """Test handling request with wrong method"""
        request = APIRequest("POST", "/system/status")
        response = self.gateway.handle_request(request)
        
        self.assertEqual(response.status_code, 405)
    
    def test_middleware(self):
        """Test middleware functionality"""
        middleware_called = []
        
        def test_middleware(request):
            middleware_called.append(True)
            return None
        
        self.gateway.add_middleware(test_middleware)
        
        request = APIRequest("GET", "/system/status")
        self.gateway.handle_request(request)
        
        self.assertTrue(middleware_called[0])
    
    def test_request_logging(self):
        """Test request logging"""
        initial_count = len(self.gateway.request_log)
        
        request = APIRequest("GET", "/system/status")
        self.gateway.handle_request(request)
        
        self.assertEqual(len(self.gateway.request_log), initial_count + 1)
    
    def test_get_endpoints(self):
        """Test getting endpoint list"""
        endpoints = self.gateway.get_endpoints()
        
        self.assertIsInstance(endpoints, list)
        self.assertGreater(len(endpoints), 0)
        
        # Check endpoint structure
        endpoint = endpoints[0]
        self.assertIn("path", endpoint)
        self.assertIn("method", endpoint)
        self.assertIn("requires_auth", endpoint)
    
    def test_statistics(self):
        """Test getting statistics"""
        stats = self.gateway.get_statistics()
        
        self.assertIn("total_endpoints", stats)
        self.assertIn("total_requests", stats)
        self.assertIn("api_version", stats)
    
    def test_system_status_endpoint(self):
        """Test system status endpoint"""
        request = APIRequest("GET", "/system/status")
        response = self.gateway.handle_request(request)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn("status", response.data)
        self.assertIn("version", response.data)
    
    def test_health_check_endpoint(self):
        """Test health check endpoint"""
        request = APIRequest("GET", "/system/health")
        response = self.gateway.handle_request(request)
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["healthy"])


if __name__ == '__main__':
    unittest.main()
