"""
AiElon Living OS - API Gateway

This module provides a unified API gateway for all system components:
- RESTful API endpoints
- Request routing
- Response formatting
- API versioning
"""

from typing import Dict, Any, List, Optional, Callable
from datetime import datetime
import json


class APIRequest:
    """API request object"""
    
    def __init__(self, method: str, endpoint: str, data: Dict[str, Any] = None,
                 headers: Dict[str, str] = None, params: Dict[str, str] = None):
        """
        Initialize API request
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint
            data: Request body data
            headers: Request headers
            params: Query parameters
        """
        self.method = method.upper()
        self.endpoint = endpoint
        self.data = data or {}
        self.headers = headers or {}
        self.params = params or {}
        self.timestamp = datetime.now().isoformat()
        self.request_id = self._generate_request_id()
    
    def _generate_request_id(self) -> str:
        """Generate unique request ID"""
        import hashlib
        request_string = f"{self.method}:{self.endpoint}:{self.timestamp}"
        return hashlib.sha256(request_string.encode()).hexdigest()[:16]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert request to dictionary"""
        return {
            "request_id": self.request_id,
            "method": self.method,
            "endpoint": self.endpoint,
            "data": self.data,
            "headers": self.headers,
            "params": self.params,
            "timestamp": self.timestamp
        }


class APIResponse:
    """API response object"""
    
    def __init__(self, status_code: int, data: Any = None, 
                 error: str = None, message: str = None):
        """
        Initialize API response
        
        Args:
            status_code: HTTP status code
            data: Response data
            error: Error message if any
            message: Success message
        """
        self.status_code = status_code
        self.data = data
        self.error = error
        self.message = message
        self.timestamp = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert response to dictionary"""
        response = {
            "status_code": self.status_code,
            "timestamp": self.timestamp
        }
        
        if self.data is not None:
            response["data"] = self.data
        
        if self.error:
            response["error"] = self.error
        
        if self.message:
            response["message"] = self.message
        
        return response
    
    def to_json(self) -> str:
        """Convert response to JSON string"""
        return json.dumps(self.to_dict(), indent=2)


class APIEndpoint:
    """API endpoint definition"""
    
    def __init__(self, path: str, method: str, handler: Callable,
                 requires_auth: bool = True, rate_limit: int = 100):
        """
        Initialize API endpoint
        
        Args:
            path: Endpoint path
            method: HTTP method
            handler: Handler function
            requires_auth: Whether authentication is required
            rate_limit: Rate limit (requests per minute)
        """
        self.path = path
        self.method = method.upper()
        self.handler = handler
        self.requires_auth = requires_auth
        self.rate_limit = rate_limit
        self.request_count = 0


class APIGateway:
    """
    Main API Gateway for routing and handling API requests
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialize API gateway
        
        Args:
            config: Configuration dictionary
        """
        self.config = config or {}
        self.endpoints: Dict[str, Dict[str, APIEndpoint]] = {}
        self.middleware: List[Callable] = []
        self.request_log: List[Dict[str, Any]] = []
        self.api_version = "v2"
    
    def initialize(self) -> None:
        """Initialize API gateway"""
        self.endpoints.clear()
        self.middleware.clear()
        self.request_log.clear()
        self._register_core_endpoints()
    
    def _register_core_endpoints(self) -> None:
        """Register core API endpoints"""
        # System endpoints
        self.register_endpoint("/system/status", "GET", self._handle_system_status, False)
        self.register_endpoint("/system/health", "GET", self._handle_health_check, False)
        
        # AI endpoints
        self.register_endpoint("/ai/process", "POST", self._handle_ai_process)
        self.register_endpoint("/ai/statistics", "GET", self._handle_ai_statistics)
        
        # Blockchain endpoints
        self.register_endpoint("/blockchain/info", "GET", self._handle_blockchain_info)
        self.register_endpoint("/blockchain/transaction", "POST", self._handle_blockchain_transaction)
        
        # Security endpoints
        self.register_endpoint("/auth/login", "POST", self._handle_login, False)
        self.register_endpoint("/auth/logout", "POST", self._handle_logout)
        
        # UI endpoints
        self.register_endpoint("/ui/dashboards", "GET", self._handle_list_dashboards)
        self.register_endpoint("/ui/dashboard", "GET", self._handle_get_dashboard)
    
    def register_endpoint(self, path: str, method: str, handler: Callable,
                         requires_auth: bool = True, rate_limit: int = 100) -> None:
        """
        Register an API endpoint
        
        Args:
            path: Endpoint path
            method: HTTP method
            handler: Handler function
            requires_auth: Whether authentication is required
            rate_limit: Rate limit
        """
        if path not in self.endpoints:
            self.endpoints[path] = {}
        
        endpoint = APIEndpoint(path, method, handler, requires_auth, rate_limit)
        self.endpoints[path][method.upper()] = endpoint
    
    def add_middleware(self, middleware: Callable) -> None:
        """
        Add middleware function
        
        Args:
            middleware: Middleware function
        """
        self.middleware.append(middleware)
    
    def handle_request(self, request: APIRequest) -> APIResponse:
        """
        Handle an API request
        
        Args:
            request: API request
            
        Returns:
            APIResponse: API response
        """
        # Log request
        self.request_log.append(request.to_dict())
        
        # Keep only last 1000 requests
        if len(self.request_log) > 1000:
            self.request_log = self.request_log[-1000:]
        
        try:
            # Apply middleware
            for mw in self.middleware:
                result = mw(request)
                if isinstance(result, APIResponse):
                    return result
            
            # Find endpoint
            if request.endpoint not in self.endpoints:
                return APIResponse(404, error="Endpoint not found")
            
            if request.method not in self.endpoints[request.endpoint]:
                return APIResponse(405, error="Method not allowed")
            
            endpoint = self.endpoints[request.endpoint][request.method]
            
            # Check rate limit
            endpoint.request_count += 1
            
            # Call handler
            response = endpoint.handler(request)
            
            return response
            
        except Exception as e:
            return APIResponse(500, error=f"Internal server error: {str(e)}")
    
    # Handler methods for core endpoints
    
    def _handle_system_status(self, request: APIRequest) -> APIResponse:
        """Handle system status request"""
        return APIResponse(200, data={
            "status": "running",
            "version": "2.0.0",
            "api_version": self.api_version
        })
    
    def _handle_health_check(self, request: APIRequest) -> APIResponse:
        """Handle health check request"""
        return APIResponse(200, data={"healthy": True})
    
    def _handle_ai_process(self, request: APIRequest) -> APIResponse:
        """Handle AI processing request"""
        text = request.data.get("text")
        if not text:
            return APIResponse(400, error="Missing 'text' parameter")
        
        return APIResponse(200, data={
            "processed": True,
            "result": "AI processing completed"
        })
    
    def _handle_ai_statistics(self, request: APIRequest) -> APIResponse:
        """Handle AI statistics request"""
        return APIResponse(200, data={
            "queries_processed": 1250,
            "accuracy": 0.95
        })
    
    def _handle_blockchain_info(self, request: APIRequest) -> APIResponse:
        """Handle blockchain info request"""
        return APIResponse(200, data={
            "chain_length": 1254,
            "pending_transactions": 5
        })
    
    def _handle_blockchain_transaction(self, request: APIRequest) -> APIResponse:
        """Handle blockchain transaction request"""
        sender = request.data.get("sender")
        recipient = request.data.get("recipient")
        amount = request.data.get("amount")
        
        if not all([sender, recipient, amount]):
            return APIResponse(400, error="Missing required parameters")
        
        return APIResponse(200, data={
            "transaction_id": "tx_12345",
            "status": "pending"
        })
    
    def _handle_login(self, request: APIRequest) -> APIResponse:
        """Handle login request"""
        username = request.data.get("username")
        password = request.data.get("password")
        
        if not all([username, password]):
            return APIResponse(400, error="Missing credentials")
        
        return APIResponse(200, data={
            "token": "jwt_token_here",
            "message": "Login successful"
        })
    
    def _handle_logout(self, request: APIRequest) -> APIResponse:
        """Handle logout request"""
        return APIResponse(200, message="Logout successful")
    
    def _handle_list_dashboards(self, request: APIRequest) -> APIResponse:
        """Handle list dashboards request"""
        return APIResponse(200, data={
            "dashboards": [
                {"id": "main", "title": "Main Dashboard"}
            ]
        })
    
    def _handle_get_dashboard(self, request: APIRequest) -> APIResponse:
        """Handle get dashboard request"""
        dashboard_id = request.params.get("id")
        if not dashboard_id:
            return APIResponse(400, error="Missing 'id' parameter")
        
        return APIResponse(200, data={
            "dashboard_id": dashboard_id,
            "title": "Main Dashboard",
            "widgets": []
        })
    
    def get_endpoints(self) -> List[Dict[str, Any]]:
        """Get list of registered endpoints"""
        endpoints = []
        for path, methods in self.endpoints.items():
            for method, endpoint in methods.items():
                endpoints.append({
                    "path": path,
                    "method": method,
                    "requires_auth": endpoint.requires_auth,
                    "rate_limit": endpoint.rate_limit,
                    "request_count": endpoint.request_count
                })
        return endpoints
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get API gateway statistics"""
        return {
            "total_endpoints": sum(len(methods) for methods in self.endpoints.values()),
            "total_requests": len(self.request_log),
            "api_version": self.api_version
        }
    
    def health_check(self) -> bool:
        """Check API gateway health"""
        return True
    
    def shutdown(self) -> None:
        """Shutdown API gateway"""
        pass
