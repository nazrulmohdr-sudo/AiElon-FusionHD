/**
 * Ummah Hub - Community and Social Networking Module
 * Islamic community platform for connection and collaboration
 */

import { globalState } from '../../core/StateManager.js';
import { securityManager } from '../../security/SecurityManager.js';

export class UmmahHub {
  constructor() {
    this.users = new Map();
    this.posts = [];
    this.groups = new Map();
    this.events = [];
    this.connections = new Map();
  }

  /**
   * Register a new user
   * @param {Object} userInfo - User information
   * @returns {Object} Registration result
   */
  registerUser(userInfo) {
    const { username, email, location } = userInfo;
    
    const userId = this.generateUserId();
    const user = {
      id: userId,
      username,
      email: securityManager.encrypt(email),
      location,
      joinedAt: Date.now(),
      posts: [],
      followers: [],
      following: [],
      reputation: 100
    };
    
    this.users.set(userId, user);
    globalState.set('totalUmmahUsers', this.users.size);
    
    return {
      success: true,
      userId,
      username
    };
  }

  /**
   * Create a new post
   * @param {string} userId - User ID
   * @param {Object} postData - Post content
   * @returns {Object} Post result
   */
  createPost(userId, postData) {
    const user = this.users.get(userId);
    if (!user) {
      return { success: false, error: 'User not found' };
    }
    
    // Validate content for appropriate community standards
    const validation = this.validateContent(postData.content);
    if (!validation.appropriate) {
      return {
        success: false,
        error: 'Content does not meet community standards'
      };
    }
    
    const post = {
      id: this.generatePostId(),
      userId,
      username: user.username,
      content: postData.content,
      type: postData.type || 'text',
      tags: postData.tags || [],
      timestamp: Date.now(),
      likes: 0,
      comments: [],
      shares: 0
    };
    
    this.posts.push(post);
    user.posts.push(post.id);
    
    return {
      success: true,
      post
    };
  }

  /**
   * Validate content for community standards
   * @private
   */
  validateContent(content) {
    // Check for inappropriate content
    const inappropriateWords = ['hate', 'violence', 'discrimination'];
    const lowerContent = content.toLowerCase();
    
    for (const word of inappropriateWords) {
      if (lowerContent.includes(word)) {
        return { appropriate: false, reason: `Contains inappropriate content` };
      }
    }
    
    return { appropriate: true };
  }

  /**
   * Create a community group
   * @param {string} creatorId - Creator user ID
   * @param {Object} groupData - Group information
   * @returns {Object} Group result
   */
  createGroup(creatorId, groupData) {
    const creator = this.users.get(creatorId);
    if (!creator) {
      return { success: false, error: 'User not found' };
    }
    
    const groupId = this.generateGroupId();
    const group = {
      id: groupId,
      name: groupData.name,
      description: groupData.description,
      category: groupData.category || 'general',
      creatorId,
      createdAt: Date.now(),
      members: [creatorId],
      posts: [],
      privacy: groupData.privacy || 'public'
    };
    
    this.groups.set(groupId, group);
    
    return {
      success: true,
      group
    };
  }

  /**
   * Join a group
   * @param {string} userId - User ID
   * @param {string} groupId - Group ID
   * @returns {Object} Join result
   */
  joinGroup(userId, groupId) {
    const user = this.users.get(userId);
    const group = this.groups.get(groupId);
    
    if (!user) {
      return { success: false, error: 'User not found' };
    }
    
    if (!group) {
      return { success: false, error: 'Group not found' };
    }
    
    if (group.members.includes(userId)) {
      return { success: false, error: 'Already a member' };
    }
    
    group.members.push(userId);
    
    return {
      success: true,
      message: `Joined ${group.name} successfully`
    };
  }

  /**
   * Create a community event
   * @param {string} organizerId - Organizer user ID
   * @param {Object} eventData - Event information
   * @returns {Object} Event result
   */
  createEvent(organizerId, eventData) {
    const organizer = this.users.get(organizerId);
    if (!organizer) {
      return { success: false, error: 'User not found' };
    }
    
    const event = {
      id: this.generateEventId(),
      title: eventData.title,
      description: eventData.description,
      organizerId,
      startTime: eventData.startTime,
      endTime: eventData.endTime,
      location: eventData.location,
      category: eventData.category || 'community',
      attendees: [organizerId],
      createdAt: Date.now(),
      status: 'upcoming'
    };
    
    this.events.push(event);
    
    return {
      success: true,
      event
    };
  }

  /**
   * Follow another user
   * @param {string} followerId - Follower user ID
   * @param {string} followeeId - User to follow
   * @returns {Object} Follow result
   */
  followUser(followerId, followeeId) {
    const follower = this.users.get(followerId);
    const followee = this.users.get(followeeId);
    
    if (!follower || !followee) {
      return { success: false, error: 'User not found' };
    }
    
    if (followerId === followeeId) {
      return { success: false, error: 'Cannot follow yourself' };
    }
    
    if (follower.following.includes(followeeId)) {
      return { success: false, error: 'Already following' };
    }
    
    follower.following.push(followeeId);
    followee.followers.push(followerId);
    
    return {
      success: true,
      message: `Now following ${followee.username}`
    };
  }

  /**
   * Get user feed
   * @param {string} userId - User ID
   * @param {number} limit - Number of posts to retrieve
   * @returns {Array} Feed posts
   */
  getFeed(userId, limit = 20) {
    const user = this.users.get(userId);
    if (!user) {
      return [];
    }
    
    // Get posts from followed users and own posts
    const relevantUserIds = [userId, ...user.following];
    const feed = this.posts
      .filter(post => relevantUserIds.includes(post.userId))
      .sort((a, b) => b.timestamp - a.timestamp)
      .slice(0, limit);
    
    return feed;
  }

  /**
   * Like a post
   * @param {string} userId - User ID
   * @param {string} postId - Post ID
   * @returns {Object} Like result
   */
  likePost(userId, postId) {
    const post = this.posts.find(p => p.id === postId);
    if (!post) {
      return { success: false, error: 'Post not found' };
    }
    
    post.likes++;
    
    return {
      success: true,
      likes: post.likes
    };
  }

  /**
   * Add comment to post
   * @param {string} userId - User ID
   * @param {string} postId - Post ID
   * @param {string} content - Comment content
   * @returns {Object} Comment result
   */
  addComment(userId, postId, content) {
    const user = this.users.get(userId);
    const post = this.posts.find(p => p.id === postId);
    
    if (!user || !post) {
      return { success: false, error: 'User or post not found' };
    }
    
    const comment = {
      id: this.generateCommentId(),
      userId,
      username: user.username,
      content,
      timestamp: Date.now()
    };
    
    post.comments.push(comment);
    
    return {
      success: true,
      comment
    };
  }

  /**
   * Get user profile
   * @param {string} userId - User ID
   * @returns {Object} User profile
   */
  getUserProfile(userId) {
    const user = this.users.get(userId);
    if (!user) {
      return { error: 'User not found' };
    }
    
    return {
      id: user.id,
      username: user.username,
      location: user.location,
      joinedAt: user.joinedAt,
      reputation: user.reputation,
      stats: {
        posts: user.posts.length,
        followers: user.followers.length,
        following: user.following.length
      }
    };
  }

  /**
   * Generate user ID
   * @private
   */
  generateUserId() {
    return `USR${Date.now()}${Math.floor(Math.random() * 1000)}`;
  }

  /**
   * Generate post ID
   * @private
   */
  generatePostId() {
    return `POST${Date.now()}${Math.floor(Math.random() * 1000)}`;
  }

  /**
   * Generate group ID
   * @private
   */
  generateGroupId() {
    return `GRP${Date.now()}${Math.floor(Math.random() * 1000)}`;
  }

  /**
   * Generate event ID
   * @private
   */
  generateEventId() {
    return `EVT${Date.now()}${Math.floor(Math.random() * 1000)}`;
  }

  /**
   * Generate comment ID
   * @private
   */
  generateCommentId() {
    return `CMT${Date.now()}${Math.floor(Math.random() * 1000)}`;
  }

  /**
   * Get community statistics
   * @returns {Object} Statistics
   */
  getStatistics() {
    return {
      totalUsers: this.users.size,
      totalPosts: this.posts.length,
      totalGroups: this.groups.size,
      totalEvents: this.events.length,
      upcomingEvents: this.events.filter(e => e.status === 'upcoming').length
    };
  }
}

export const ummahHub = new UmmahHub();
