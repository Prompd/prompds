<!-- PROMPD METADATA
author: null
context: null
description: Builds comprehensive REST APIs with security, documentation, and best
  practices
id: rest-api-builder
inherits: null
inputs: {}
name: REST API Builder
parameters:
- default: null
  description: Name of the API being built
  error_message: null
  example: null
  max_value: null
  min_value: null
  name: api_name
  pattern: null
  required: true
  type: !!python/object/apply:builtins.getattr
  - &id001 !!python/name:prompd.models.ParameterType ''
  - STRING
- default: null
  description: Main resource (e.g., "user", "order", "product")
  error_message: null
  example: null
  max_value: null
  min_value: null
  name: resource_name
  pattern: null
  required: true
  type: !!python/object/apply:builtins.getattr
  - *id001
  - STRING
- default: express
  description: Backend framework
  error_message: null
  example: null
  max_value: null
  min_value: null
  name: framework
  pattern: null
  required: false
  type: !!python/object/apply:builtins.getattr
  - *id001
  - STRING
- default: postgresql
  description: Database system
  error_message: null
  example: null
  max_value: null
  min_value: null
  name: database
  pattern: null
  required: false
  type: !!python/object/apply:builtins.getattr
  - *id001
  - STRING
- default: jwt
  description: Authentication method
  error_message: null
  example: null
  max_value: null
  min_value: null
  name: auth_method
  pattern: null
  required: false
  type: !!python/object/apply:builtins.getattr
  - *id001
  - STRING
- default:
  - crud
  - pagination
  description: API features to implement
  error_message: null
  example: null
  max_value: null
  min_value: null
  name: features
  pattern: null
  required: false
  type: !!python/object/apply:builtins.getattr
  - *id001
  - ARRAY
requires: []
response: null
system: null
tags: []
user: null
using: []
version: 1.0.0

-->

# Main Prompt Content

# {{imports.system}} REST API Implementation

## API Specification: {E-commerce API}

Building a comprehensive REST API for **{product}** using {express} and {postgresql} with {jwt} authentication.

### Architecture Overview

{{imports.context.rest-best-practices}}

**Technology Stack:**
- Framework: {express}
- Database: {postgresql}
- Authentication: {jwt}
- Features: {{#each features}}{{this}}{{#unless @last}}, {{/unless}}{{/each}}

## Implementation Plan

### 1. API Design & Documentation

{{imports.templates.openapi-template}}

**OpenAPI Specification for {E-commerce API}:**
```yaml
openapi: 3.0.3
info:
  title: {E-commerce API}
  version: 1.0.0
  description: REST API for {product} management

paths:
{{#if (includes features "crud")}}
  /{product}s:
    get:
      summary: List {product}s
      parameters:
        {{#if (includes features "pagination")}}
        - name: page
          in: query
          schema:
            type: integer
            default: 1
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
        {{/if}}
        {{#if (includes features "filtering")}}
        - name: filter
          in: query
          schema:
            type: string
        {{/if}}
      responses:
        '200':
          description: List of {product}s
    post:
      summary: Create {product}
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/{product}'
      responses:
        '201':
          description: {product} created

  /{product}s/{id}:
    get:
      summary: Get {product} by ID
    put:
      summary: Update {product}
    delete:
      summary: Delete {product}
{{/if}}
```

### 2. Security Implementation

{{imports.security}}

**Authentication & Authorization for {jwt}:**

{{#switch auth_method}}
{{#case "jwt"}}
```javascript
// JWT Authentication Middleware
const jwt = require('jsonwebtoken');

const authenticateToken = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];
  
  if (!token) {
    return res.status(401).json({ error: 'Access token required' });
  }
  
  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) {
      return res.status(403).json({ error: 'Invalid token' });
    }
    req.user = user;
    next();
  });
};
```
{{/case}}
{{#case "oauth2"}}
```javascript
// OAuth 2.0 Integration
const passport = require('passport');
const OAuth2Strategy = require('passport-oauth2');

passport.use(new OAuth2Strategy({
  authorizationURL: process.env.OAUTH_AUTH_URL,
  tokenURL: process.env.OAUTH_TOKEN_URL,
  clientID: process.env.OAUTH_CLIENT_ID,
  clientSecret: process.env.OAUTH_CLIENT_SECRET,
  callbackURL: "/auth/callback"
}, (accessToken, refreshToken, profile, done) => {
  // Verify and create user session
  return done(null, profile);
}));
```
{{/case}}
{{/switch}}

**Input Validation & Sanitization:**
```javascript
const Joi = require('joi');

const {product}Schema = Joi.object({
  // Define validation schema for {product}
  name: Joi.string().min(1).max(255).required(),
  email: Joi.string().email().required(),
  // Add other fields as needed
});

const validateRequest = (schema) => (req, res, next) => {
  const { error } = schema.validate(req.body);
  if (error) {
    return res.status(400).json({ 
      error: 'Validation failed',
      details: error.details 
    });
  }
  next();
};
```

### 3. Database Layer

**{postgresql} Integration:**

{{#switch database}}
{{#case "postgresql"}}
```javascript
// PostgreSQL with connection pooling
const { Pool } = require('pg');

const pool = new Pool({
  user: process.env.DB_USER,
  host: process.env.DB_HOST,
  database: process.env.DB_NAME,
  password: process.env.DB_PASSWORD,
  port: process.env.DB_PORT,
  ssl: process.env.NODE_ENV === 'production'
});

class {product}Repository {
  async findAll(options = {}) {
    const { page = 1, limit = 20, filter } = options;
    const offset = (page - 1) * limit;
    
    let query = 'SELECT * FROM {product}s';
    const params = [];
    
    if (filter) {
      query += ' WHERE name ILIKE $1';
      params.push(`%${filter}%`);
    }
    
    query += ' LIMIT $${params.length + 1} OFFSET $${params.length + 2}';
    params.push(limit, offset);
    
    const result = await pool.query(query, params);
    return result.rows;
  }
  
  async create(data) {
    const query = `
      INSERT INTO {product}s (name, email, created_at)
      VALUES ($1, $2, NOW())
      RETURNING *
    `;
    const result = await pool.query(query, [data.name, data.email]);
    return result.rows[0];
  }
}
```
{{/case}}
{{#case "mongodb"}}
```javascript
// MongoDB with Mongoose
const mongoose = require('mongoose');

const {product}Schema = new mongoose.Schema({
  name: { type: String, required: true, maxlength: 255 },
  email: { type: String, required: true, unique: true },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

{product}Schema.pre('save', function(next) {
  this.updatedAt = Date.now();
  next();
});

const {product} = mongoose.model('{product}', {product}Schema);

class {product}Repository {
  async findAll(options = {}) {
    const { page = 1, limit = 20, filter } = options;
    const skip = (page - 1) * limit;
    
    let query = {};
    if (filter) {
      query.name = { $regex: filter, $options: 'i' };
    }
    
    return await {product}.find(query)
      .skip(skip)
      .limit(limit)
      .sort({ createdAt: -1 });
  }
  
  async create(data) {
    const {{resource_name|lower}} = new {product}(data);
    return await {{resource_name|lower}}.save();
  }
}
```
{{/case}}
{{/switch}}

### 4. API Routes Implementation

**{express} Routes:**

```javascript
{{#switch framework}}
{{#case "express"}}
const express = require('express');
const rateLimit = require('express-rate-limit');
const helmet = require('helmet');

const app = express();
const {product}Repository = new {product}Repository();

// Security middleware
app.use(helmet());
app.use(express.json({ limit: '10mb' }));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use('/api', limiter);

{{#if (includes features "crud")}}
// GET /{product}s
app.get('/api/{product}s', authenticateToken, async (req, res) => {
  try {
    const { page, limit, filter } = req.query;
    const {product}s = await {product}Repository.findAll({ 
      page: parseInt(page), 
      limit: parseInt(limit), 
      filter 
    });
    
    res.json({
      data: {product}s,
      pagination: {
        page: parseInt(page) || 1,
        limit: parseInt(limit) || 20,
        // Add total count logic
      }
    });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// POST /{product}s
app.post('/api/{product}s', 
  authenticateToken, 
  validateRequest({product}Schema),
  async (req, res) => {
    try {
      const {{resource_name|lower}} = await {product}Repository.create(req.body);
      res.status(201).json({ data: {{resource_name|lower}} });
    } catch (error) {
      if (error.code === '23505') { // Unique violation
        res.status(409).json({ error: 'Resource already exists' });
      } else {
        res.status(500).json({ error: 'Internal server error' });
      }
    }
  }
);
{{/if}}
{{/case}}
{{/switch}}
```

### 5. Advanced Features Implementation

{{#each features}}
{{#switch this}}
{{#case "search"}}
**Full-Text Search:**
```javascript
// Elasticsearch integration for advanced search
const { Client } = require('@elastic/elasticsearch');
const client = new Client({ node: process.env.ELASTICSEARCH_URL });

app.get('/api/{{../resource_name}}s/search', async (req, res) => {
  const { q, fields } = req.query;
  
  const searchBody = {
    query: {
      multi_match: {
        query: q,
        fields: fields ? fields.split(',') : ['name', 'description']
      }
    }
  };
  
  const result = await client.search({
    index: '{{../resource_name}}s',
    body: searchBody
  });
  
  res.json({ data: result.body.hits.hits });
});
```
{{/case}}
{{#case "file-upload"}}
**File Upload with Security:**
```javascript
const multer = require('multer');
const path = require('path');

const upload = multer({
  storage: multer.diskStorage({
    destination: 'uploads/',
    filename: (req, file, cb) => {
      const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
      cb(null, file.fieldname + '-' + uniqueSuffix + path.extname(file.originalname));
    }
  }),
  fileFilter: (req, file, cb) => {
    // Whitelist file types
    const allowedTypes = /jpeg|jpg|png|pdf/;
    const extname = allowedTypes.test(path.extname(file.originalname).toLowerCase());
    const mimetype = allowedTypes.test(file.mimetype);
    
    if (mimetype && extname) {
      return cb(null, true);
    } else {
      cb(new Error('Only images and PDFs allowed'));
    }
  },
  limits: { fileSize: 5 * 1024 * 1024 } // 5MB limit
});

app.post('/api/{{../resource_name}}s/:id/upload', 
  authenticateToken, 
  upload.single('file'),
  async (req, res) => {
    // File upload logic
  }
);
```
{{/case}}
{{/switch}}
{{/each}}

### 6. Testing Strategy

**Comprehensive API Testing:**

```javascript
// Jest + Supertest for API testing
const request = require('supertest');
const app = require('./app');

describe('{product} API', () => {
  let authToken;
  
  beforeAll(async () => {
    // Setup test database and auth token
    authToken = await getTestAuthToken();
  });
  
  describe('GET /api/{product}s', () => {
    test('should return paginated {product}s', async () => {
      const response = await request(app)
        .get('/api/{product}s')
        .set('Authorization', `Bearer ${authToken}`)
        .expect(200);
      
      expect(response.body.data).toBeInstanceOf(Array);
      expect(response.body.pagination).toBeDefined();
    });
    
    test('should require authentication', async () => {
      await request(app)
        .get('/api/{product}s')
        .expect(401);
    });
  });
  
  describe('POST /api/{product}s', () => {
    test('should create new {product}', async () => {
      const {product}Data = {
        name: 'Test {product}',
        email: 'test@example.com'
      };
      
      const response = await request(app)
        .post('/api/{product}s')
        .set('Authorization', `Bearer ${authToken}`)
        .send({product}Data)
        .expect(201);
      
      expect(response.body.data.name).toBe({product}Data.name);
    });
  });
});
```

### 7. Performance & Monitoring

**Performance Optimization:**
- Database query optimization and indexing
- Response caching with Redis
- API response compression
- Connection pooling
- Lazy loading for relationships

**Monitoring & Observability:**
```javascript
// Prometheus metrics
const promClient = require('prom-client');

const httpRequestDuration = new promClient.Histogram({
  name: 'http_request_duration_seconds',
  help: 'Duration of HTTP requests in seconds',
  labelNames: ['method', 'route', 'status']
});

// Middleware to collect metrics
app.use((req, res, next) => {
  const start = Date.now();
  
  res.on('finish', () => {
    const duration = (Date.now() - start) / 1000;
    httpRequestDuration
      .labels(req.method, req.route?.path || req.path, res.statusCode)
      .observe(duration);
  });
  
  next();
});
```

## Deployment Checklist

- [ ] Environment variables configured
- [ ] Database migrations applied
- [ ] SSL/TLS certificates installed
- [ ] Rate limiting configured
- [ ] Monitoring and logging setup
- [ ] API documentation deployed
- [ ] Security headers configured
- [ ] Backup strategy implemented
- [ ] Performance testing completed
- [ ] Load balancing configured (if needed)

## Success Criteria

✅ **Functionality**: All CRUD operations work correctly
✅ **Security**: Authentication, validation, and rate limiting implemented
✅ **Performance**: Response times under 200ms for simple queries
✅ **Documentation**: OpenAPI spec with interactive docs
✅ **Testing**: 90%+ test coverage
✅ **Monitoring**: Metrics and logging in place
✅ **Scalability**: Can handle expected traffic load