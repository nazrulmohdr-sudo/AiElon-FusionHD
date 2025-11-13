# AiElon Living OS - Developer Guide

## Introduction

This guide provides detailed information for developers who want to contribute to, extend, or integrate with AiElon Living OS.

## Development Environment Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git
- Text editor or IDE (VS Code, PyCharm, etc.)

### Initial Setup

```bash
# Clone the repository
git clone https://github.com/nazrulmohdr-sudo/AiElon-FusionHD.git
cd AiElon-FusionHD

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest pytest-cov black flake8 mypy
```

### Project Structure

```
AiElon-FusionHD/
├── src/                    # Source code
│   ├── core/              # Core system
│   ├── ai/                # AI engine
│   ├── blockchain/        # Blockchain
│   ├── security/          # Security
│   ├── ui/                # User interface
│   ├── plugins/           # Plugin system
│   ├── api/               # API gateway
│   └── utils/             # Utilities
├── tests/                  # Test suite
│   ├── unit/              # Unit tests
│   ├── integration/       # Integration tests
│   └── security/          # Security tests
├── docs/                   # Documentation
├── example.py             # Usage example
├── requirements.txt       # Dependencies
└── README.md              # Project README
```

## Development Workflow

### 1. Making Changes

Always work on a feature branch:

```bash
git checkout -b feature/your-feature-name
```

### 2. Code Style

We follow PEP 8 guidelines. Format your code with Black:

```bash
# Format code
black src/

# Check style
flake8 src/

# Type checking
mypy src/
```

### 3. Writing Tests

All new features must include tests. We aim for 95%+ code coverage.

#### Unit Test Example

```python
import unittest
from your_module import YourClass

class TestYourClass(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.instance = YourClass()
    
    def test_feature(self):
        """Test a specific feature"""
        result = self.instance.method()
        self.assertEqual(result, expected_value)
    
    def tearDown(self):
        """Clean up after tests"""
        pass
```

#### Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/unit/test_system.py -v

# Run with coverage
python -m pytest tests/ --cov=src --cov-report=html

# View coverage report
open htmlcov/index.html  # On Mac/Linux
start htmlcov/index.html  # On Windows
```

### 4. Documentation

Document all public APIs, classes, and functions:

```python
def function_name(param1: str, param2: int) -> bool:
    """
    Brief description of the function.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        bool: Description of return value
    
    Raises:
        ValueError: When invalid input is provided
    
    Examples:
        >>> function_name("test", 42)
        True
    """
    pass
```

### 5. Commit Messages

Follow conventional commit format:

```
type(scope): brief description

Detailed description if needed

Breaking changes if any
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Test additions/changes
- `refactor`: Code refactoring
- `style`: Code style changes
- `perf`: Performance improvements

Example:
```
feat(blockchain): add smart contract support

Implemented basic smart contract execution and storage.
Includes validation and gas limit mechanisms.
```

### 6. Pull Requests

1. Ensure all tests pass
2. Update documentation
3. Add test coverage for new features
4. Create descriptive PR title and description
5. Link related issues

## Module Development

### Creating a New Module

1. Create module directory in `src/`:

```bash
mkdir src/your_module
touch src/your_module/__init__.py
touch src/your_module/your_module.py
```

2. Implement module with standard interface:

```python
"""
Your Module - Description

This module provides...
"""

from typing import Dict, Any

class YourModule:
    """Main class for your module"""
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialize module
        
        Args:
            config: Configuration dictionary
        """
        self.config = config or {}
    
    def initialize(self) -> None:
        """Initialize the module"""
        pass
    
    def health_check(self) -> bool:
        """
        Check module health
        
        Returns:
            bool: True if healthy
        """
        return True
    
    def shutdown(self) -> None:
        """Shutdown the module"""
        pass
```

3. Create tests in `tests/unit/`:

```python
import unittest
from your_module.your_module import YourModule

class TestYourModule(unittest.TestCase):
    def setUp(self):
        self.module = YourModule()
    
    def test_initialization(self):
        self.assertIsNotNone(self.module)
```

4. Register module with system:

```python
from core.system import AiElonLivingOS
from your_module.your_module import YourModule

system = AiElonLivingOS()
your_module = YourModule()
system.register_module("your_module", your_module)
```

### Extending Existing Modules

#### Extending AI Engine

Add custom NLP processing:

```python
from ai.ai_engine import AIEngine

class ExtendedAIEngine(AIEngine):
    def custom_processing(self, text: str) -> Dict[str, Any]:
        """Add custom processing logic"""
        result = self.process_natural_language(text)
        # Add custom processing
        result["custom_metric"] = self._calculate_custom_metric(text)
        return result
    
    def _calculate_custom_metric(self, text: str) -> float:
        """Calculate custom metric"""
        # Your custom logic
        return 0.95
```

#### Extending Blockchain

Add custom transaction types:

```python
from blockchain.aielonchain338 import AielonChain338, Transaction

class SmartContractTransaction(Transaction):
    def __init__(self, sender: str, contract_address: str, 
                 amount: float, contract_data: Dict[str, Any]):
        super().__init__(sender, contract_address, amount, "smart_contract")
        self.contract_data = contract_data
    
    def execute_contract(self) -> Any:
        """Execute smart contract logic"""
        pass
```

#### Creating Custom Plugins

```python
from plugins.plugin_system import Plugin, PluginEvent

class MyCustomPlugin(Plugin):
    def __init__(self):
        super().__init__(
            plugin_id="my_custom_plugin",
            name="My Custom Plugin",
            version="1.0.0"
        )
        self.dependencies = ["core_plugin"]  # If depends on other plugins
    
    def initialize(self, config: Dict[str, Any] = None) -> bool:
        """Initialize plugin"""
        super().initialize(config)
        
        # Register event handlers
        self.register_event_handler("custom_event", self.handle_custom_event)
        
        return True
    
    def handle_custom_event(self, event: PluginEvent) -> None:
        """Handle custom event"""
        print(f"Received event: {event.event_type}")
        # Process event data
    
    def shutdown(self) -> None:
        """Clean up resources"""
        super().shutdown()
```

#### Creating Custom Widgets

```python
from ui.ui_framework import Widget

class AdvancedChartWidget(Widget):
    def __init__(self, widget_id: str):
        super().__init__(widget_id, "advanced_chart")
        self.chart_data = []
    
    def add_data_point(self, timestamp: str, value: float) -> None:
        """Add data point to chart"""
        self.chart_data.append({"timestamp": timestamp, "value": value})
        self.update_data({"chart_data": self.chart_data})
    
    def render(self) -> Dict[str, Any]:
        """Custom rendering logic"""
        render_data = super().render()
        render_data["chart_type"] = "line"
        render_data["data_points"] = len(self.chart_data)
        return render_data
```

## API Development

### Adding New Endpoints

```python
from api.api_gateway import APIGateway, APIRequest, APIResponse

def custom_endpoint_handler(request: APIRequest) -> APIResponse:
    """
    Handle custom endpoint request
    
    Args:
        request: API request object
    
    Returns:
        APIResponse: API response
    """
    try:
        # Validate request
        if not request.data.get("required_param"):
            return APIResponse(400, error="Missing required_param")
        
        # Process request
        result = process_logic(request.data)
        
        # Return success response
        return APIResponse(200, data=result, message="Success")
        
    except Exception as e:
        return APIResponse(500, error=f"Internal error: {str(e)}")

# Register endpoint
gateway = APIGateway()
gateway.register_endpoint(
    "/custom/endpoint",
    "POST",
    custom_endpoint_handler,
    requires_auth=True,
    rate_limit=50
)
```

### Adding Middleware

```python
def logging_middleware(request: APIRequest) -> Optional[APIResponse]:
    """
    Log all API requests
    
    Args:
        request: API request
    
    Returns:
        APIResponse or None: Return response to block request, None to continue
    """
    print(f"[API] {request.method} {request.endpoint}")
    
    # Continue processing (return None)
    return None

def auth_middleware(request: APIRequest) -> Optional[APIResponse]:
    """
    Check authentication
    
    Args:
        request: API request
    
    Returns:
        APIResponse or None: Unauthorized response or None
    """
    token = request.headers.get("Authorization")
    
    if not token:
        return APIResponse(401, error="Unauthorized")
    
    # Verify token
    # If valid, return None to continue
    return None

# Add middleware
gateway.add_middleware(logging_middleware)
gateway.add_middleware(auth_middleware)
```

## Testing Best Practices

### Test Structure

```python
class TestFeature(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up once for all tests"""
        pass
    
    def setUp(self):
        """Set up before each test"""
        self.instance = YourClass()
    
    def test_basic_functionality(self):
        """Test basic functionality"""
        result = self.instance.method()
        self.assertTrue(result)
    
    def test_edge_cases(self):
        """Test edge cases"""
        # Test with empty input
        result = self.instance.method("")
        self.assertIsNone(result)
        
        # Test with invalid input
        with self.assertRaises(ValueError):
            self.instance.method(invalid_input)
    
    def test_integration(self):
        """Test integration with other components"""
        pass
    
    def tearDown(self):
        """Clean up after each test"""
        pass
    
    @classmethod
    def tearDownClass(cls):
        """Clean up once after all tests"""
        pass
```

### Mocking Dependencies

```python
from unittest.mock import Mock, patch, MagicMock

class TestWithMocks(unittest.TestCase):
    def test_with_mock(self):
        """Test using mock objects"""
        # Create mock
        mock_dependency = Mock()
        mock_dependency.method.return_value = "mocked_value"
        
        # Use mock
        instance = YourClass(dependency=mock_dependency)
        result = instance.use_dependency()
        
        # Verify mock was called
        mock_dependency.method.assert_called_once()
        self.assertEqual(result, "expected_value")
    
    @patch('your_module.external_service')
    def test_with_patch(self, mock_service):
        """Test using patch decorator"""
        mock_service.return_value = "mocked_response"
        
        result = function_using_external_service()
        
        self.assertEqual(result, "expected_result")
```

## Performance Optimization

### Profiling Code

```python
import cProfile
import pstats

def profile_function():
    """Profile a function"""
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Code to profile
    your_function()
    
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats(10)  # Top 10 functions
```

### Memory Optimization

```python
import sys

def check_memory_usage(obj):
    """Check memory usage of object"""
    size = sys.getsizeof(obj)
    print(f"Memory usage: {size} bytes ({size / 1024:.2f} KB)")
```

### Caching

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_computation(param):
    """Cache results of expensive computation"""
    # Expensive operation
    return result
```

## Security Guidelines

### Input Validation

```python
def validate_input(data: Dict[str, Any]) -> bool:
    """
    Validate user input
    
    Args:
        data: Input data to validate
    
    Returns:
        bool: True if valid
    """
    # Check required fields
    required_fields = ["username", "email"]
    if not all(field in data for field in required_fields):
        return False
    
    # Validate email format
    import re
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, data["email"]):
        return False
    
    # Sanitize strings
    for key, value in data.items():
        if isinstance(value, str):
            # Remove potentially dangerous characters
            data[key] = value.replace("<", "").replace(">", "")
    
    return True
```

### Secure Coding Practices

1. **Never hardcode secrets**
   - Use environment variables
   - Use configuration files (not in version control)
   - Use secret management systems

2. **Validate all inputs**
   - Check types
   - Check ranges
   - Sanitize strings

3. **Use parameterized queries**
   - Never concatenate SQL queries
   - Use prepared statements

4. **Implement proper error handling**
   - Don't expose internal errors to users
   - Log errors securely
   - Return generic error messages

## Debugging

### Logging

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Use logging
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
```

### Debugging Tools

```python
# Python debugger
import pdb

def debug_function():
    x = 10
    pdb.set_trace()  # Breakpoint
    y = x * 2
    return y
```

## Continuous Integration

### GitHub Actions Example

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest pytest-cov
    
    - name: Run tests
      run: |
        pytest tests/ --cov=src --cov-report=xml
    
    - name: Upload coverage
      uses: codecov/codecov-action@v2
```

## Release Process

1. **Update version numbers**
   - Update version in code
   - Update CHANGELOG.md

2. **Run full test suite**
   ```bash
   pytest tests/ -v
   ```

3. **Update documentation**
   - Update README.md
   - Update API documentation
   - Update user guides

4. **Create release tag**
   ```bash
   git tag -a v2.0.0 -m "Release version 2.0.0"
   git push origin v2.0.0
   ```

5. **Build and publish**
   ```bash
   python setup.py sdist bdist_wheel
   ```

## Common Issues and Solutions

### Issue: Import Errors

**Solution**: Ensure PYTHONPATH includes src directory
```bash
export PYTHONPATH="${PYTHONPATH}:${PWD}/src"
```

### Issue: Test Failures

**Solution**: Check test isolation
- Ensure tests don't depend on execution order
- Clean up resources in tearDown
- Use fresh instances for each test

### Issue: Performance Degradation

**Solution**: Profile and optimize
- Use cProfile to find bottlenecks
- Implement caching
- Optimize database queries
- Reduce object creation

## Resources

- **Python Documentation**: https://docs.python.org/3/
- **Pytest Documentation**: https://docs.pytest.org/
- **PEP 8 Style Guide**: https://pep8.org/
- **Type Hints**: https://docs.python.org/3/library/typing.html

## Getting Help

- **Documentation**: Check `/docs` directory
- **Issues**: Open GitHub issue
- **Examples**: See `example.py` and test files

## Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Update documentation
6. Submit a pull request

Thank you for contributing to AiElon Living OS!
