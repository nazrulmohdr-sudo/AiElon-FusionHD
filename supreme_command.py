"""
Supreme Command Mutlak Module

This module implements the Supreme Command Mutlak capabilities with:
- Command execution and control
- System orchestration
- Integration with Supreme GodMode
"""

from typing import Dict, Any, List, Callable
from enum import Enum
import time


class CommandPriority(Enum):
    """Command priority levels"""
    CRITICAL = 1
    HIGH = 2
    NORMAL = 3
    LOW = 4


class CommandStatus(Enum):
    """Command execution status"""
    PENDING = "pending"
    EXECUTING = "executing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class Command:
    """Represents a single command in the system"""
    
    def __init__(self, name: str, action: Callable, priority: CommandPriority = CommandPriority.NORMAL):
        """
        Initialize a command
        
        Args:
            name: Command name
            action: Callable function to execute
            priority: Command priority level
        """
        self.name = name
        self.action = action
        self.priority = priority
        self.status = CommandStatus.PENDING
        self.result = None
        self.error = None
        self.timestamp = time.time()
        
    def execute(self) -> Any:
        """
        Execute the command
        
        Returns:
            Result of command execution
        """
        try:
            self.status = CommandStatus.EXECUTING
            self.result = self.action()
            self.status = CommandStatus.COMPLETED
            return self.result
        except Exception as e:
            self.status = CommandStatus.FAILED
            self.error = str(e)
            raise
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert command to dictionary representation"""
        return {
            'name': self.name,
            'priority': self.priority.name,
            'status': self.status.value,
            'result': self.result,
            'error': self.error,
            'timestamp': self.timestamp
        }


class SupremeCommand:
    """
    Supreme Command Mutlak - Ultimate command and control system
    
    Provides:
    - Command queue management
    - Priority-based execution
    - System orchestration
    - Integration with Supreme GodMode
    """
    
    def __init__(self):
        """Initialize Supreme Command system"""
        self.commands: List[Command] = []
        self.command_history: List[Command] = []
        self.active = True
        
    def register_command(self, name: str, action: Callable, 
                        priority: CommandPriority = CommandPriority.NORMAL) -> Command:
        """
        Register a new command
        
        Args:
            name: Command name
            action: Callable function to execute
            priority: Command priority level
            
        Returns:
            Created Command object
        """
        command = Command(name, action, priority)
        self.commands.append(command)
        return command
    
    def execute_command(self, command: Command) -> Any:
        """
        Execute a specific command
        
        Args:
            command: Command to execute
            
        Returns:
            Command execution result
        """
        if not self.active:
            raise RuntimeError("Supreme Command system is not active")
        
        result = command.execute()
        self.command_history.append(command)
        
        # Remove from pending commands
        if command in self.commands:
            self.commands.remove(command)
            
        return result
    
    def execute_by_name(self, name: str) -> Any:
        """
        Execute a command by name
        
        Args:
            name: Name of the command to execute
            
        Returns:
            Command execution result
        """
        for command in self.commands:
            if command.name == name:
                return self.execute_command(command)
        raise ValueError(f"Command '{name}' not found")
    
    def execute_all(self) -> List[Dict[str, Any]]:
        """
        Execute all pending commands in priority order
        
        Returns:
            List of command execution results
        """
        # Sort by priority
        sorted_commands = sorted(self.commands, key=lambda c: c.priority.value)
        results = []
        
        for command in sorted_commands[:]:  # Use slice to avoid modification during iteration
            try:
                self.execute_command(command)
                results.append(command.to_dict())
            except Exception as e:
                results.append({
                    'name': command.name,
                    'status': 'failed',
                    'error': str(e)
                })
        
        return results
    
    def get_pending_commands(self) -> List[Dict[str, Any]]:
        """
        Get list of pending commands
        
        Returns:
            List of pending command information
        """
        return [cmd.to_dict() for cmd in self.commands if cmd.status == CommandStatus.PENDING]
    
    def get_command_history(self) -> List[Dict[str, Any]]:
        """
        Get command execution history
        
        Returns:
            List of historical command information
        """
        return [cmd.to_dict() for cmd in self.command_history]
    
    def clear_pending(self) -> int:
        """
        Clear all pending commands
        
        Returns:
            Number of commands cleared
        """
        count = len(self.commands)
        self.commands.clear()
        return count
    
    def clear_history(self) -> int:
        """
        Clear command history
        
        Returns:
            Number of history entries cleared
        """
        count = len(self.command_history)
        self.command_history.clear()
        return count
    
    def get_system_status(self) -> Dict[str, Any]:
        """
        Get Supreme Command system status
        
        Returns:
            Dictionary with system information
        """
        return {
            'command': 'Supreme Command Mutlak',
            'active': self.active,
            'pending_commands': len(self.commands),
            'history_count': len(self.command_history),
            'version': '1.0.0'
        }
    
    def shutdown(self) -> None:
        """Shutdown Supreme Command system"""
        self.active = False
        self.commands.clear()
    
    def activate(self) -> None:
        """Activate Supreme Command system"""
        self.active = True


# Singleton instance
_command_instance = None


def get_command_instance() -> SupremeCommand:
    """Get or create singleton instance of SupremeCommand"""
    global _command_instance
    if _command_instance is None:
        _command_instance = SupremeCommand()
    return _command_instance
