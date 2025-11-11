#!/usr/bin/env python3
"""
Trade138 - Trading System
Advanced trading platform with real-time analytics
"""

import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
from enum import Enum
from decimal import Decimal


class OrderType(Enum):
    """Order types for trading"""
    BUY = "buy"
    SELL = "sell"
    LIMIT = "limit"
    MARKET = "market"


class OrderStatus(Enum):
    """Order status enumeration"""
    PENDING = "pending"
    EXECUTED = "executed"
    CANCELLED = "cancelled"
    FAILED = "failed"


class Order:
    """Trading order structure"""
    
    def __init__(self, order_id: str, user_id: str, order_type: OrderType,
                 asset: str, quantity: Decimal, price: Optional[Decimal] = None):
        self.order_id = order_id
        self.user_id = user_id
        self.order_type = order_type
        self.asset = asset
        self.quantity = quantity
        self.price = price
        self.status = OrderStatus.PENDING
        self.timestamp = datetime.now().isoformat()
        self.executed_at = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert order to dictionary"""
        return {
            'order_id': self.order_id,
            'user_id': self.user_id,
            'order_type': self.order_type.value,
            'asset': self.asset,
            'quantity': str(self.quantity),
            'price': str(self.price) if self.price else None,
            'status': self.status.value,
            'timestamp': self.timestamp,
            'executed_at': self.executed_at
        }


class Trade138:
    """
    Trade138 - Advanced Trading Platform
    Provides secure trading capabilities with compliance
    """
    
    def __init__(self):
        self.orders: Dict[str, Order] = {}
        self.portfolios: Dict[str, Dict[str, Decimal]] = {}
        self.market_data: Dict[str, Decimal] = {}
        self.trade_history: List[Dict[str, Any]] = []
        self.logger = logging.getLogger('Trade138')
        self.order_counter = 0
        
        # Initialize default market data
        self._initialize_market_data()
    
    def _initialize_market_data(self):
        """Initialize default market prices"""
        self.market_data = {
            'BTC': Decimal('50000.00'),
            'ETH': Decimal('3000.00'),
            'AEC': Decimal('138.00'),  # AiElon Coin
            'USDT': Decimal('1.00')
        }
        self.logger.info("Market data initialized")
    
    def create_portfolio(self, user_id: str) -> bool:
        """Create a new user portfolio"""
        try:
            if user_id not in self.portfolios:
                self.portfolios[user_id] = {
                    'USDT': Decimal('10000.00')  # Starting balance
                }
                self.logger.info(f"Portfolio created for user: {user_id}")
                return True
            return False
        except Exception as e:
            self.logger.error(f"Failed to create portfolio: {e}")
            return False
    
    def get_portfolio(self, user_id: str) -> Optional[Dict[str, Decimal]]:
        """Get user portfolio"""
        return self.portfolios.get(user_id)
    
    def place_order(self, user_id: str, order_type: OrderType, 
                   asset: str, quantity: Decimal, 
                   price: Optional[Decimal] = None) -> Optional[str]:
        """Place a trading order"""
        try:
            # Create portfolio if doesn't exist
            if user_id not in self.portfolios:
                self.create_portfolio(user_id)
            
            # Generate order ID
            self.order_counter += 1
            order_id = f"ORD{self.order_counter:06d}"
            
            # Create order
            order = Order(order_id, user_id, order_type, asset, quantity, price)
            self.orders[order_id] = order
            
            self.logger.info(f"Order placed: {order_id}")
            
            # Execute market orders immediately
            if order_type == OrderType.MARKET:
                self.execute_order(order_id)
            
            return order_id
            
        except Exception as e:
            self.logger.error(f"Failed to place order: {e}")
            return None
    
    def execute_order(self, order_id: str) -> bool:
        """Execute a trading order"""
        try:
            order = self.orders.get(order_id)
            if not order:
                self.logger.error(f"Order not found: {order_id}")
                return False
            
            if order.status != OrderStatus.PENDING:
                self.logger.warning(f"Order {order_id} already processed")
                return False
            
            portfolio = self.portfolios[order.user_id]
            market_price = self.market_data.get(order.asset, Decimal('0'))
            
            if order.order_type in [OrderType.BUY, OrderType.MARKET]:
                # Calculate cost
                cost = market_price * order.quantity
                
                # Check if user has sufficient balance
                if portfolio.get('USDT', Decimal('0')) >= cost:
                    portfolio['USDT'] -= cost
                    portfolio[order.asset] = portfolio.get(order.asset, Decimal('0')) + order.quantity
                    order.status = OrderStatus.EXECUTED
                    order.executed_at = datetime.now().isoformat()
                    
                    # Record trade
                    self.trade_history.append({
                        'order_id': order_id,
                        'user_id': order.user_id,
                        'type': 'buy',
                        'asset': order.asset,
                        'quantity': str(order.quantity),
                        'price': str(market_price),
                        'timestamp': order.executed_at
                    })
                    
                    self.logger.info(f"Order {order_id} executed successfully")
                    return True
                else:
                    order.status = OrderStatus.FAILED
                    self.logger.error(f"Insufficient balance for order {order_id}")
                    return False
            
            elif order.order_type == OrderType.SELL:
                # Check if user has sufficient assets
                if portfolio.get(order.asset, Decimal('0')) >= order.quantity:
                    portfolio[order.asset] -= order.quantity
                    proceeds = market_price * order.quantity
                    portfolio['USDT'] = portfolio.get('USDT', Decimal('0')) + proceeds
                    order.status = OrderStatus.EXECUTED
                    order.executed_at = datetime.now().isoformat()
                    
                    # Record trade
                    self.trade_history.append({
                        'order_id': order_id,
                        'user_id': order.user_id,
                        'type': 'sell',
                        'asset': order.asset,
                        'quantity': str(order.quantity),
                        'price': str(market_price),
                        'timestamp': order.executed_at
                    })
                    
                    self.logger.info(f"Order {order_id} executed successfully")
                    return True
                else:
                    order.status = OrderStatus.FAILED
                    self.logger.error(f"Insufficient assets for order {order_id}")
                    return False
            
            return False
            
        except Exception as e:
            self.logger.error(f"Failed to execute order: {e}")
            return False
    
    def get_market_data(self) -> Dict[str, str]:
        """Get current market data"""
        return {asset: str(price) for asset, price in self.market_data.items()}
    
    def get_trade_statistics(self) -> Dict[str, Any]:
        """Get trading statistics"""
        return {
            'total_orders': len(self.orders),
            'executed_orders': sum(1 for o in self.orders.values() if o.status == OrderStatus.EXECUTED),
            'pending_orders': sum(1 for o in self.orders.values() if o.status == OrderStatus.PENDING),
            'total_trades': len(self.trade_history),
            'active_users': len(self.portfolios)
        }
    
    def initialize(self):
        """Initialize Trade138 system"""
        self.logger.info("Trade138 initialized")
    
    def health_check(self) -> Dict[str, Any]:
        """Perform health check"""
        stats = self.get_trade_statistics()
        return {
            'status': 'operational',
            'total_orders': stats['total_orders'],
            'active_users': stats['active_users'],
            'market_assets': len(self.market_data)
        }


if __name__ == "__main__":
    # Test Trade138
    trade_system = Trade138()
    trade_system.create_portfolio('user001')
    order_id = trade_system.place_order('user001', OrderType.MARKET, 'BTC', Decimal('0.1'))
    print(f"Order placed: {order_id}")
    print(f"Portfolio: {trade_system.get_portfolio('user001')}")
