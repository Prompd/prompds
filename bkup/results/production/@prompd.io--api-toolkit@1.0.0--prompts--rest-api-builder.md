# Test Results: @prompd.io\api-toolkit@1.0.0\prompts\rest-api-builder.prmd

**Source File:** `..\prompd-base\production\@prompd.io\api-toolkit@1.0.0\prompts\rest-api-builder.prmd`

**Test Date:** 2025-09-12 21:13:57

## Execution Results

- **Status:** PASS

### LLM Response

```
+---------------------------------- Response from anthropic/claude-3-haiku-20240307 -----------------------------------+
| # REST API Implementation Guide                                                                                      |
|                                                                                                                      |
| As an expert API architect with 10+ years of experience, I will guide you through the implementation of a            |
| comprehensive REST API for user management using Express and PostgreSQL with JWT authentication.                     |
|                                                                                                                      |
| ## API Specification: TestAPI                                                                                        |
|                                                                                                                      |
| ### Architecture Overview                                                                                            |
|                                                                                                                      |
| **Technology Stack:**                                                                                                |
| - Framework: Express                                                                                                 |
| - Database: PostgreSQL                                                                                               |
| - Authentication: JWT                                                                                                |
| - Features: CRUD, Pagination, Filtering                                                                              |
|                                                                                                                      |
| ## Implementation Plan                                                                                               |
|                                                                                                                      |
| ### 1. API Design & Documentation                                                                                    |
|                                                                                                                      |
| **OpenAPI Specification for TestAPI:**                                                                               |
|                                                                                                                      |
| ```yaml                                                                                                              |
| openapi: 3.0.3                                                                                                       |
| info:                                                                                                                |
|   title: TestAPI                                                                                                     |
|   version: 1.0.0                                                                                                     |
|   description: REST API for user management                                                                          |
|                                                                                                                      |
| paths:                                                                                                               |
|   /users:                                                                                                            |
|     get:                                                                                                             |
|       summary: List users                                                                                            |
|       parameters:                                                                                                    |
|         - name: page                                                                                                 |
|           in: query                                                                                                  |
|           schema:                                                                                                    |
|             type: integer                                                                                            |
|             default: 1                                                                                               |
|         - name: limit                                                                                                |
|           in: query                                                                                                  |
|           schema:                                                                                                    |
|             type: integer                                                                                            |
|             default: 20                                                                                              |
|         - name: filter                                                                                               |
|           in: query                                                                                                  |
|           schema:                                                                                                    |
|             type: string                                                                                             |
|       responses:                                                                                                     |
|         '200':                                                                                                       |
|           description: List of users                                                                                 |
|     post:                                                                                                            |
|       summary: Create user                                                                                           |
|       requestBody:                                                                                                   |
|         required: true                                                                                               |
|         content:                                                                                                     |
|           application/json:                                                                                          |
|             schema:                                                                                                  |
|               $ref: '#/components/schemas/user'                                                                      |
|       responses:                                                                                                     |
|         '201':                                                                                                       |
|           description: user created                                                                                  |
|                                                                                                                      |
|   /users/{id}:                                                                                                       |
|     get:                                                                                                             |
|       summary: Get user by ID                                                                                        |
|     put:                                                                                                             |
|       summary: Update user                                                                                           |
|     delete:                                                                                                          |
|       summary: Delete user                                                                                           |
|                                                                                                                      |
| components:                                                                                                          |
|   schemas:                                                                                                           |
|     user:                                                                                                            |
|       type: object                                                                                                   |
|       properties:                                                                                                    |
|         name:                                                                                                        |
|           type: string                                                                                               |
|         email:                                                                                                       |
|           type: string                                                                                               |
| ```                                                                                                                  |
|                                                                                                                      |
| ### 2. Security Implementation                                                                                       |
|                                                                                                                      |
| **Authentication & Authorization for JWT:**                                                                          |
|                                                                                                                      |
| ```javascript                                                                                                        |
| // JWT Authentication Middleware                                                                                     |
| const jwt = require('jsonwebtoken');                                                                                 |
|                                                                                                                      |
| const authenticateToken = (req, res, next) => {                                                                      |
|   const authHeader = req.headers['authorization'];                                                                   |
|   const token = authHeader && authHeader.split(' ')[1];                                                              |
|                                                                                                                      |
|   if (!token) {                                                                                                      |
|     return res.status(401).json({ error: 'Access token required' });                                                 |
|   }                                                                                                                  |
|                                                                                                                      |
|   jwt.verify(token, process.env.JWT_SECRET, (err, user) => {                                                         |
|     if (err) {                                                                                                       |
|       return res.status(403).json({ error: 'Invalid token' });                                                       |
|     }                                                                                                                |
|     req.user = user;                                                                                                 |
|     next();                                                                                                          |
|   });                                                                                                                |
| };                                                                                                                   |
| ```                                                                                                                  |
|                                                                                                                      |
| **Input Validation & Sanitization:**                                                                                 |
|                                                                                                                      |
| ```javascript                                                                                                        |
| const Joi = require('joi');                                                                                          |
|                                                                                                                      |
| const userSchema = Joi.object({                                                                                      |
|   name: Joi.string().min(1).max(255).required(),                                                                     |
|   email: Joi.string().email().required(),                                                                            |
| });                                                                                                                  |
|                                                                                                                      |
| const validateRequest = (schema) => (req, res, next) => {                                                            |
|   const { error } = schema.validate(req.body);                                                                       |
|   if (error) {                                                                                                       |
|     return res.status(400).json({                                                                                    |
|       error: 'Validation failed',                                                                                    |
|       details: error.details                                                                                         |
|     });                                                                                                              |
|   }                                                                                                                  |
|   next();                                                                                                            |
| };                                                                                                                   |
| ```                                                                                                                  |
|                                                                                                                      |
| ### 3. Database Layer                                                                                                |
|                                                                                                                      |
| **PostgreSQL Integration:**                                                                                          |
|                                                                                                                      |
| ```javascript                                                                                                        |
| // PostgreSQL with connection pooling                                                                                |
| const { Pool } = require('pg');                                                                                      |
|                                                                                                                      |
| const pool = new Pool({                                                                                              |
|   user: process.env.DB_USER,                                                                                         |
|   host: process.env.DB_HOST,                                                                                         |
|   database: process.env.DB_NAME,                                                                                     |
|   password: process.env.DB_PASSWORD,                                                                                 |
|   port: process.env.DB_PORT,                                                                                         |
|   ssl: process.env.NODE_ENV === 'production'                                                                         |
| });                                                                                                                  |
|                                                                                                                      |
| class userRepository {                                                                                               |
|   async findAll(options = {}) {                                                                                      |
|     const { page = 1, limit = 20, filter } = options;                                                                |
|     const offset = (page - 1) * limit;                                                                               |
|                                                                                                                      |
|     let query = 'SELECT * FROM users';                                                                               |
|     const params = [];                                                                                               |
|                                                                                                                      |
|     if (filter) {                                                                                                    |
|       query += ' WHERE name ILIKE $1';                                                                               |
|       params.push(`%${filter}%`);                                                                                    |
|     }                                                                                                                |
|                                                                                                                      |
|     query += ` LIMIT $${params.length + 1} OFFSET $${params.length + 2}`;                                            |
|     params.push(limit, offset);                                                                                      |
|                                                                                                                      |
|     const result = await pool.query(query, params);                                                                  |
|     return result                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------+

```

